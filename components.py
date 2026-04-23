import importlib
from pathlib import Path

import streamlit as st
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.prebuilt import create_react_agent

try:
    from practica_final.config import AGENT_MODEL, EMBEDDING_MODEL
except ModuleNotFoundError:
    from config import AGENT_MODEL, EMBEDDING_MODEL


@st.cache_resource(show_spinner=False)
def crear_componentes(pdf_dir: str, chroma_dir: str, agent_temperature: float):
    pdf_path = Path(pdf_dir)
    chroma_path = Path(chroma_dir)
    chroma_path.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(pdf_path.glob("*.pdf"))
    if not pdf_files:
        raise FileNotFoundError(
            f"No se encontraron PDFs en {pdf_path}. Coloca al menos un .pdf en esa carpeta."
        )

    all_docs = []
    for file in pdf_files:
        loader = PyPDFLoader(str(file))
        docs = loader.load()
        for doc in docs:
            doc.metadata["source"] = file.name
        all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
    chunks = splitter.split_documents(all_docs)

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="practica_final_rag",
        persist_directory=str(chroma_path),
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    @tool
    def buscar_en_documento(consulta: str) -> str:
        """Busca informacion relevante en los PDF indexados del dominio."""
        docs = retriever.invoke(consulta)
        if not docs:
            return "No encontre contenido relevante en los documentos."

        partes = []
        for i, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "desconocido")
            page = doc.metadata.get("page")
            page_txt = f"p.{page + 1}" if isinstance(page, int) else "p.?"
            partes.append(f"[fragmento {i} | {source} | {page_txt}]\n{doc.page_content}")

        return "\n\n".join(partes)

    @tool
    def buscar_en_internet(consulta: str) -> str:
        """Busca informacion actual en internet cuando el documento no alcance."""
        try:
            ddgs_module = importlib.import_module("ddgs")
            ddgs_cls = getattr(ddgs_module, "DDGS")
        except Exception:
            return (
                "No se pudo usar la busqueda web porque falta la dependencia 'ddgs'. "
                "Instala dependencias con: uv sync"
            )

        resultados = []
        with ddgs_cls() as buscador:
            for item in buscador.text(consulta, max_results=5):
                titulo = item.get("title", "Sin titulo")
                enlace = item.get("href", "Sin enlace")
                resumen = item.get("body", "")
                resultados.append(f"- {titulo}\n  {enlace}\n  {resumen}")

        if not resultados:
            return "No encontre resultados en internet para esa consulta."

        return "\n\n".join(resultados)

    llm_guard = ChatOpenAI(model=AGENT_MODEL, temperature=0)
    llm_agent = ChatOpenAI(model=AGENT_MODEL, temperature=agent_temperature)

    domain_excerpt = "\n\n".join(chunk.page_content[:500] for chunk in chunks[:6])

    agent_prompt = (
        "Eres un asistente especializado en la tematica de los documentos indexados. "
        "Debes seguir esta estrategia: "
        "(1) Primero intenta responder con buscar_en_documento. "
        "(2) Solo usa buscar_en_internet si el documento no es suficiente o si la pregunta requiere actualidad. "
        "(3) En la respuesta final, se claro y conciso, y menciona de forma breve en que fuente te basaste."
    )

    agent = create_react_agent(
        llm_agent,
        tools=[buscar_en_documento, buscar_en_internet],
        prompt=agent_prompt,
    )

    return {
        "agent": agent,
        "guard_llm": llm_guard,
        "domain_excerpt": domain_excerpt,
    }

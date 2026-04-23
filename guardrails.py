from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def _normalizar_etiqueta_guardarrail(raw: str) -> str:
    text = (raw or "").strip().lower()
    first = text.split()[0].strip(".,;:!?\"'") if text else ""
    if first == "relevante":
        return "relevante"
    if first == "irrelevante":
        return "irrelevante"
    return "irrelevante"


def es_pregunta_relevante(guard_llm: ChatOpenAI, domain_excerpt: str, question: str) -> bool:
    system_prompt = (
        "Eres un clasificador de relevancia tematica. "
        "Tu tarea es evaluar si la pregunta del usuario esta dentro del dominio de los documentos. "
        "Responde unicamente con una palabra exacta: relevante o irrelevante. "
        "No expliques nada.\n\n"
        "Fragmento del dominio de referencia:\n"
        f"{domain_excerpt}\n"
    )

    response = guard_llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=question),
    ])
    etiqueta = _normalizar_etiqueta_guardarrail(str(response.content))
    return etiqueta == "relevante"

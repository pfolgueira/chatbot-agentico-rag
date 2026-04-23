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
        "Eres un experto en clasificación de dominios deportivos. "
        "Tu tarea es determinar si la pregunta del usuario pertenece al mundo del FÚTBOL.\n\n"
        "REGLAS CRÍTICAS:\n"
        "1. El 'Fragmento de referencia' es solo una muestra técnica de nuestra base de datos.\n"
        "2. Debes marcar como RELEVANTE cualquier pregunta sobre fútbol: historia, jugadores, "
        "táctica, reglas, mundiales, equipos, ligas o actualidad futbolística.\n"
        "3. Marca como IRRELEVANTE solo si el tema no tiene nada que ver con fútbol "
        "(ej. cocina, política general, matemáticas, otros deportes como baloncesto).\n\n"
        "Responde ÚNICAMENTE con la palabra 'relevante' o 'irrelevante'.\n\n"
        "Fragmento del dominio de referencia (ejemplos):\n"
        f"{domain_excerpt}\n"
    )

    response = guard_llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=question),
    ])
    etiqueta = _normalizar_etiqueta_guardarrail(str(response.content))
    return etiqueta == "relevante"

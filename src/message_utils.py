from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage


def to_lc_messages(messages: list[dict[str, str]]) -> list[BaseMessage]:
    lc_messages: list[BaseMessage] = []
    for message in messages:
        role = message.get("role")
        content = message.get("content", "")
        if role == "user":
            lc_messages.append(HumanMessage(content=content))
        elif role == "assistant":
            lc_messages.append(AIMessage(content=content))
    return lc_messages


def extraer_respuesta_final(messages: list[BaseMessage]) -> str:
    for message in reversed(messages):
        if isinstance(message, AIMessage) and message.content:
            if isinstance(message.content, str):
                return message.content
            if isinstance(message.content, list):
                return "\n".join(str(x) for x in message.content)
    return "No pude generar una respuesta en este turno."


def extraer_fuentes(messages: list[BaseMessage]) -> list[str]:
    fuentes: set[str] = set()
    for message in messages:
        if isinstance(message, ToolMessage):
            tool_name = message.name or ""
            if tool_name == "buscar_en_documento":
                fuentes.add("documento")
            elif tool_name == "buscar_en_internet":
                fuentes.add("internet")
    return sorted(fuentes)

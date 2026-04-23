import os

import streamlit as st

try:
    from practica_final.components import crear_componentes
    from practica_final.config import DEFAULT_CHROMA_DIR, DEFAULT_PDF_DIR
    from practica_final.guardrails import es_pregunta_relevante
    from practica_final.message_utils import extraer_fuentes, extraer_respuesta_final, to_lc_messages
except ModuleNotFoundError:
    from components import crear_componentes
    from config import DEFAULT_CHROMA_DIR, DEFAULT_PDF_DIR
    from guardrails import es_pregunta_relevante
    from message_utils import extraer_fuentes, extraer_respuesta_final, to_lc_messages


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def main() -> None:
    st.set_page_config(page_title="Practica Final - Chatbot Agentico", page_icon="AI", layout="wide")

    st.title("Practica Final: Chatbot Agentico con RAG y Web")
    st.caption("Guardarrailes tematicos + Agente ReAct + Chroma + DuckDuckGo")

    with st.sidebar:
        st.header("Configuracion")
        temperatura = st.slider("Temperatura del agente", min_value=0.0, max_value=1.5, value=0.0, step=0.1)

    init_session_state()

    if not os.getenv("OPENAI_API_KEY"):
        st.error("Falta OPENAI_API_KEY. Configura .env antes de ejecutar la app.")
        st.stop()

    with st.spinner("Inicializando RAG, herramientas y agente..."):
        try:
            components = crear_componentes(str(DEFAULT_PDF_DIR), str(DEFAULT_CHROMA_DIR), temperatura)
        except Exception as exc:
            st.error(f"Error al inicializar componentes: {exc}")
            st.stop()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and msg.get("sources"):
                st.caption("Fuentes: " + ", ".join(msg["sources"]))

    user_input = st.chat_input("Escribe tu pregunta...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Evaluando guardarrailes..."):
                relevante = es_pregunta_relevante(
                    guard_llm=components["guard_llm"],
                    domain_excerpt=components["domain_excerpt"],
                    question=user_input,
                )

            if not relevante:
                rechazo = (
                    "Puedo ayudarte con preguntas relacionadas con los documentos indexados. "
                    "Si quieres, reformula tu pregunta para enfocarla en esa tematica."
                )
                st.markdown(rechazo)
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": rechazo,
                        "sources": ["guardarrail"],
                    }
                )
            else:
                with st.spinner("Pensando y consultando fuentes..."):
                    conversational_messages = to_lc_messages(st.session_state.messages)
                    result = components["agent"].invoke({"messages": conversational_messages})

                result_messages = result.get("messages", [])
                final_answer = extraer_respuesta_final(result_messages)
                sources = extraer_fuentes(result_messages)

                st.markdown(final_answer)
                if sources:
                    st.caption("Fuentes: " + ", ".join(sources))

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": final_answer,
                        "sources": sources or ["sin_fuente_detectada"],
                    }
                )


if __name__ == "__main__":
    main()
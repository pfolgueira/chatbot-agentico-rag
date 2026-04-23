import os
from pathlib import Path

import streamlit as st

from components import crear_componentes
from config import DEFAULT_CHROMA_DIR, DEFAULT_PDF_DIR
from guardrails import es_pregunta_relevante
from message_utils import extraer_fuentes, extraer_respuesta_final, to_lc_messages


def init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


# Avatares desde la carpeta assets en la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]
USER_AVATAR = str(BASE_DIR / "assets" / "user.png")
ASSISTANT_AVATAR = str(BASE_DIR / "assets" / "assistant.png")


def main() -> None:
    st.set_page_config(page_title="Chatbot Agéntico con RAG, Búsqueda Web y Guardarraíles", page_icon="AI", layout="wide")

    st.title("🤖 Chatbot Agéntico con RAG, Búsqueda Web y Guardarraíles")
    st.caption("Guardarraíles tematicos + Agente ReAct + Chroma + DuckDuckGo")

    # Inject custom CSS for chat border and minor slider tweaks.
    st.markdown(
        """
        <style>
        /* Ensure primary color (theme) is used for inputs; fallback for slider thumb */
        input[type=range]::-webkit-slider-thumb { background: #0b3d91 !important; }
        input[type=range]::-moz-range-thumb { background: #0b3d91 !important; }

        /* Chat message border / bubble visual */
        [data-testid="stChatMessage"] {
            border: 1px solid #0b3d91 !important;
            border-radius: 10px !important;
            padding: 6px !important;
        }

        /* Slightly tint the assistant bubble background */
        [data-testid="stChatMessage"]:has(img[alt="assistant"]) {
            background-color: rgba(11,61,145,0.04) !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

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
        avatar = ASSISTANT_AVATAR if msg.get("role") == "assistant" else USER_AVATAR
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and msg.get("sources"):
                st.caption("Fuentes: " + ", ".join(msg["sources"]))

    user_input = st.chat_input("Escribe tu pregunta...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
            with st.spinner("Analizando tu jugada... 📊"):
                relevante = es_pregunta_relevante(
                    guard_llm=components["guard_llm"],
                    domain_excerpt=components["domain_excerpt"],
                    question=user_input,
                )

            if not relevante:
                rechazo = (
                    "¡Vaya! Parece que nos hemos salido del campo de juego. 😅\n\n"
                    "Soy un **experto** en todo lo relacionado con el **fútbol** (historia, táctica, mundiales, fútbol femenino y más). "
                    "Para poder ayudarte mejor, ¡prueba a hacerme una pregunta sobre ese tema!"
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
                with st.spinner("Consultando la pizarra táctica... ⚽"):
                    conversational_messages = to_lc_messages(st.session_state.messages)
                    result = components["agent"].invoke({"messages": conversational_messages})

                result_messages = result.get("messages", [])
                final_answer = extraer_respuesta_final(result_messages)
                sources = extraer_fuentes(result_messages)

                st.markdown(final_answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": final_answer,
                        "sources": sources or ["sin_fuente_detectada"],
                    }
                )


if __name__ == "__main__":
    main()
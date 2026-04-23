import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]

DEFAULT_PDF_DIR = Path(
	os.getenv("PRACTICA_FINAL_PDF_DIR", str(BASE_DIR / "datos"))
).expanduser()
DEFAULT_CHROMA_DIR = Path(
	os.getenv("PRACTICA_FINAL_CHROMA_DIR", str(BASE_DIR / ".chroma_practica_final"))
).expanduser()
AGENT_MODEL = os.getenv("PRACTICA_FINAL_AGENT_MODEL", "gpt-5.4-nano")
EMBEDDING_MODEL = os.getenv("PRACTICA_FINAL_EMBEDDING_MODEL", "text-embedding-3-small")

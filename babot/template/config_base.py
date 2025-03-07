from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

class Config:
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")
    OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", 0.7))  # Reducir creatividad/razonamiento
    OLLAMA_TOP_P = float(os.getenv("OLLAMA_TOP_P", 0.9))  # Filtrar tokens menos relevantes

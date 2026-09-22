"""Shared configuration: chooses the LLM provider and holds the canteen data."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads the .env file in this folder

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "ollama":
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")
elif PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")
elif PROVIDER == "huggingface":
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
else:
    raise SystemExit(f"Unknown PROVIDER '{PROVIDER}'. Use ollama, groq or huggingface.")

if not API_KEY:
    raise SystemExit(f"No API key found for PROVIDER={PROVIDER}. Check your .env file.")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

# Private canteen data that no public LLM has ever seen
MENU_PRICES = {"SAMOSA": 15, "TEA": 10, "COFFEE": 20, "SANDWICH": 40, "MEALS": 60}

QUESTIONS = [
    "What is the price of a sandwich?",
    "What is the total cost of meals and coffee with a 20% student discount?",
    "Is meals more expensive than a sandwich, and by how much?",
    "Write a two-line message welcoming students to the canteen.",
]

def banner(system_name):
    print(f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n")
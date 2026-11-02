import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
CDP_URL = os.getenv("EDGE_CDP_URL", "http://127.0.0.1:9222").strip()

# Safety guard: this starter is for practice/mock pages you own or are
# explicitly authorized to automate. Keep submission manual.
PRACTICE_MODE = os.getenv("PRACTICE_MODE", "false").lower() == "true"

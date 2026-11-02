import json
from pathlib import Path

def save_report(data, path: Path):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

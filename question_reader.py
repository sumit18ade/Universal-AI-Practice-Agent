import re

def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()

async def read_visible_text(page):
    return await page.locator("body").inner_text(timeout=15000)

def extract_candidates(raw_text):
    """Heuristic text capture only; it does not infer DOM answer controls."""
    lines = [clean(x) for x in raw_text.splitlines()]
    lines = [x for x in lines if x]
    lines = [re.sub(r"^slide:\s*", "", x, flags=re.I) for x in lines]

    question = next(
        (x for x in lines if "?" in x and len(x) > 20),
        ""
    )
    if not question:
        question = next((x for x in lines if len(x) > 25), "")

    ignored = (
        "SUBMIT", "NEXT", "PREVIOUS", "KEYBOARD NAVIGATION",
        "SKIP NAVIGATION", "NUMBER CORRECT"
    )
    options = []
    qkey = clean(question).lower()

    for line in lines:
        line = re.sub(r"^\d+[\.\)]\s*", "", line).strip()
        if not line or line.lower() == qkey:
            continue
        if any(word in line.upper() for word in ignored):
            continue
        if "?" in line or len(line) > 180 or len(line) < 2:
            continue
        if line not in options:
            options.append(line)

    return {"question": question, "options": options, "raw_text": raw_text}

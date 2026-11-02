from question_reader import read_visible_text, extract_candidates

async def capture_page(page):
    raw = await read_visible_text(page)
    return extract_candidates(raw)

async def run_practice_assistant(page, client, report_path):
    """
    Captures visible question text and writes AI explanations.
    Deliberately does not click answer controls or submit the page.
    """
    import json
    from datetime import datetime
    from ai_engine import explain_question

    raw = await read_visible_text(page)
    data = extract_candidates(raw)

    if not data["question"]:
        raise RuntimeError("Could not confidently identify a question. See raw page capture.")

    explanation = await explain_question(
        client, data["question"], data["options"]
    )

    result = {
        "url": page.url,
        "captured_at": datetime.now().isoformat(),
        "question": data["question"],
        "options": data["options"],
        "explanation": explanation,
        "note": "Study assistance only. No answer was clicked and nothing was submitted."
    }

    report_path.write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    return result

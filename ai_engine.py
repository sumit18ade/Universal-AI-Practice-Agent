import asyncio
from google import genai
from google.genai import types
from config import API_KEY, MODEL

def make_client():
    if not API_KEY:
        raise RuntimeError("GEMINI_API_KEY missing. Copy .env.example to .env and add your key.")
    return genai.Client(
        api_key=API_KEY,
        http_options=types.HttpOptions(timeout=120000)
    )

async def explain_question(client, question, options):
    prompt = f"""
You are a study tutor. Explain this practice question without interacting
with any website and without submitting anything.

Question: {question}

Options:
{chr(10).join(f"- {x}" for x in options)}

Explain the concept, how to reason through the options, and a memory tip.
If the question is ambiguous or the options are incomplete, say so.
"""
    last_error = None
    for attempt in range(2):
        try:
            response = await asyncio.to_thread(
                client.models.generate_content,
                model=MODEL,
                contents=prompt
            )
            return response.text or "The model returned an empty response."
        except Exception as exc:
            last_error = exc
            await asyncio.sleep(3 * (attempt + 1))
    return f"AI temporarily unavailable: {last_error}"

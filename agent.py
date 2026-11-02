import asyncio
from config import REPORTS, PRACTICE_MODE
from browser import BrowserSession
from ai_engine import make_client
from practice_runner import run_practice_assistant

async def main():
    print("=" * 48)
    print(" UNIVERSAL PRACTICE STUDY ASSISTANT")
    print("=" * 48)

    if not PRACTICE_MODE:
        print("[INFO] Practice mode is OFF.")
        print("For your own authorized mock/practice page, set PRACTICE_MODE=true in .env.")
        print("This assistant explains questions; it does not click answers or submit tests.")
        return

    client = make_client()
    session = BrowserSession()

    try:
        browser = await session.connect()
        print("[OK] Connected to Edge.")

        pages = session.pages()
        if not pages:
            print("[ERROR] No Edge tabs found.")
            return

        for i, page in enumerate(pages):
            print(f"{i + 1}. {page.title()} | {page.url}")

        raw_choice = input("Choose the practice/mock-test tab number: ").strip()
        if not raw_choice.isdigit() or not (1 <= int(raw_choice) <= len(pages)):
            print("[ERROR] Invalid tab selection.")
            return

        page = pages[int(raw_choice) - 1]
        output = REPORTS / "practice_analysis.json"

        result = await run_practice_assistant(page, client, output)

        print("\n[QUESTION]")
        print(result["question"])
        print("\n[OPTIONS]")
        for idx, option in enumerate(result["options"], 1):
            print(f"{idx}. {option}")

        print("\n[AI EXPLANATION]")
        print(result["explanation"])
        print(f"\n[SAVED] {output}")
        print("[INFO] No answer was clicked and the test was not submitted.")

    finally:
        await session.close()

if __name__ == "__main__":
    asyncio.run(main())

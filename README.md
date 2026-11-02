# Universal Practice Study Assistant

A Windows/Python starter that connects to an already-open Microsoft Edge session,
captures visible question text from a selected tab, asks Gemini for a study
explanation, and saves a JSON report.

## Setup (PowerShell)

1. Extract this folder.
2. Open PowerShell in this folder.
3. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

4. Copy `.env.example` to `.env` and add your Gemini API key locally.
5. Add this line to `.env` for your own authorized practice/mock pages:

```env
PRACTICE_MODE=true
```

6. Start Edge with remote debugging (close other Edge instances first if needed):

```powershell
& "$env:ProgramFiles(x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="$env:LOCALAPPDATA\EdgePracticeAgent"
```

If Edge is installed elsewhere, adjust the executable path. Open your authorized
practice/mock page in that Edge window.

7. Run:

```powershell
python agent.py
```

Choose the tab number when prompted.

## Output

The `reports/practice_analysis.json` file contains the captured question,
candidate options, AI explanation, page URL, and timestamp.

## Important

This starter is intentionally a study assistant: it does not select answers,
click quiz controls, or submit tests. Use it only on pages you own or are
authorized to access. Heuristic text extraction may need site-specific tuning.
Gemini model availability can vary; a 503/504 response is a provider-side
availability/deadline issue, not proof that the browser code is broken.

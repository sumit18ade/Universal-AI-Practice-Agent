# 🚀 Universal AI Practice Agent

### Your Intelligent AI-Powered Learning & Practice Companion

An AI-powered practice assistant designed to help students understand questions, explore concepts, generate explanations, and analyze their practice performance using Google's Gemini AI.

Built with Python, Playwright, and Gemini AI, this project aims to make self-learning smarter, more interactive, and accessible.

<p align="center">

  **Learn Smarter. Practice Better. Improve Faster.**

</p>

---

## 📌 Overview

**Universal AI Practice Agent** is an intelligent learning assistant that helps students during practice and mock-test sessions.

It reads visible question content from a selected browser tab, processes the questions using AI, generates explanations, and analyzes practice performance.

Instead of simply focusing on answers, the system emphasizes understanding concepts and improving learning outcomes.

> Designed for educational practice, mock tests, and self-learning. It is not intended to automate graded examinations or bypass assessment rules.

---

## ✨ Key Features

- 🤖 **AI-Powered Intelligence** – Uses Google Gemini AI to understand practice questions and generate explanations.
- 🌐 **Browser Integration** – Connects to a Microsoft Edge browser session using Playwright.
- 📖 **Question Understanding** – Reads visible question content from the selected browser tab.
- 💡 **Concept Explanations** – Helps learners understand the concepts behind questions.
- 📊 **Performance Analysis** – Analyzes practice results and learning performance.
- 📝 **Report Generation** – Saves practice analysis in JSON format.
- ⚙️ **Configurable Environment** – Supports environment-based configuration.
- 🔒 **API Key Protection** – Keeps credentials in a local `.env` file.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Google Gemini AI | AI-powered question understanding |
| Playwright | Browser automation and interaction |
| Microsoft Edge | Browser session integration |
| JSON | Practice reports and structured data |
| Python-dotenv | Environment configuration |

---

## 🏗️ Project Architecture

```text
Universal-AI-Practice-Agent/
│
├── agent.py              # Main application entry point
├── ai_engine.py          # AI processing and Gemini integration
├── browser.py            # Browser connection and interaction
├── config.py             # Application configuration
├── practice_runner.py    # Practice workflow execution
├── question_reader.py    # Question content extraction
├── result_analyzer.py    # Practice result analysis
│
├── reports/              # Generated practice reports
│
├── .env.example          # Environment variable template
├── .gitignore            # Git ignored files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚡ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/sumit18ade/Universal-AI-Practice-Agent.git
```

### 2. Navigate to the Project

```bash
cd Universal-AI-Practice-Agent
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.8-flash
EDGE_CDP_URL=http://127.0.0.1:9222
PRACTICE_MODE=true
```

Replace `your_gemini_api_key` with your own Gemini API key.

**Important:** Never upload your `.env` file or API credentials to GitHub.

### 7. Run the Application

```bash
python agent.py
```

---

## 🔄 How It Works

1. **Environment Setup:** Loads application settings and API credentials.
2. **Browser Connection:** Connects to the configured Microsoft Edge debugging session.
3. **Question Extraction:** Reads visible question content from the selected browser tab.
4. **AI Processing:** Sends the extracted content to Gemini AI for understanding and explanation.
5. **Practice Analysis:** Processes the practice workflow and analyzes available results.
6. **Report Generation:** Saves the generated practice report in JSON format.

---

## 🔐 Security & Responsible Usage

- Keep API keys and credentials private.
- Store sensitive configuration in `.env`.
- Never commit `.env` to a public repository.
- Use the application only for authorized educational practice.
- Do not use it to bypass examination rules, automate graded assessments, or submit answers on behalf of students.

---

## 🎯 Project Objectives

- Make AI-assisted learning easier and more accessible.
- Help students understand difficult questions.
- Improve self-practice and independent learning.
- Provide structured insights into practice performance.
- Explore practical applications of AI and browser integration.

---

## 🚀 Future Enhancements

- 📚 Support for additional learning platforms.
- 📈 Advanced performance dashboards.
- 🧠 Personalized learning recommendations.
- 🌍 Multilingual learning assistance.
- 📄 PDF and Excel report exports.
- 💬 Interactive AI learning assistant.
- 🎓 Topic-wise practice and progress tracking.

---

## 👨‍💻 Developer

**Sumit Ganesh Ade**

Computer Science & Engineering Student  
Full Stack Developer | AI/ML Enthusiast

🌐 **Portfolio:** https://sumit18x-portfolio.vercel.app/

💻 **GitHub:** https://github.com/sumit18ade

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

Your support and feedback help improve this project!

---

<p align="center">

  **Built with ❤️ using Python, Playwright & Google Gemini AI**

</p>

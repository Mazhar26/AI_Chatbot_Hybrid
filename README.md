📘 AI Chatbot Hybrid – Final Project Documentation

A hybrid AI chatbot built in Python that combines rule-based logic with Google Gemini Generative AI using the Gemini API. The system intelligently chooses between predefined responses and LLM-powered responses to provide fast and accurate outputs.

🧰 **Tech Stack
*Languages:
Python 3.10+

*Frameworks & Libraries:
google-generativeai – Gemini API integration
dotenv – environment variable management
json, datetime, regex – Python core modules
Custom rule-based logic

*Developer Tools
VS Code
Git & GitHub
Virtual Environment (venv)

Versions (Recommended)
| Component           | Version   |
| ------------------- | --------- |
| Python              | 3.10–3.12 |
| google-generativeai | ^0.3+     |
| python-dotenv       | ^1.0      |



🏗 System Architecture
Architecture Diagram

                ┌────────────────────┐
                │     User Input     │
                └─────────┬──────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  Hybrid Chatbot Logic  │
              │ (Router / Controller)  │
              └─────────┬──────────────┘
       ┌────────────────┼────────────────────┐
       │                │                    │
       ▼                ▼                    ▼
┌────────────┐   ┌─────────────┐   ┌─────────────────────────┐
│ Rule-Based │   │ Preprocessor│   │  Gemini LLM (API Call)  │
│   Engine   │   │  (Cleaning) │   │  via google-generativeai│
└────────────┘   └─────────────┘   └─────────────────────────┘
       │                │                    │
       └────────────────┴────────────────────┘
                          ▼
                ┌──────────────────────┐
                │ Final Chat Response  │
                └──────────────────────┘



Explanation:
User message is received and routed by the Hybrid Controller.
Pre-processing cleans/normalizes input.
If query matches known patterns → Rule Engine responds instantly.
Otherwise query is sent to Google GenerrativeAI model for intelligent output.
Response is formatted and displayed back to user.

✨ Core Features
✔ Hybrid Intelligence
Uses rule-based responses for simple queries and Gemini AI for advanced reasoning.
✔ Gemini API Integration
Supports models like:
gemini-pro
gemini-1.5-flash
gemini-1.5-pro
✔ Secure API Management
Uses .env to store Gemini API key safely
✔ Clean & Modular Code
Easy to expand with more logic or prompts.

Trade-offs
LLM calls require internet + API cost.
Rule-based system cannot handle complex logic alone.
Basic CLI interface (can be upgraded to web UI later).

🚀 Setup & Run Guide
🔧 Prerequisites
Python 3.10+
Gemini API Key (from Google AI Studio)
Git

1️⃣ Clone the Repo
git clone https://github.com/Mazhar26/AI_Chatbot_Hybrid.git
cd AI_Chatbot_Hybrid

2️⃣ Create Virtual Environment
python -m venv venv

Activate:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install google-generativeai python-dotenv

4️⃣ Create .env File
GEMINI_API_KEY=your_api_key_here

5️⃣ Run the Chatbot
python hybrid_chatbot.py

🗂 .env.example
# Gemini API Key
GEMINI_API_KEY=your_api_key_here

🔑 Key APIs & Components
Gemini API Initialization
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

Sending a Prompt to Gemini
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(prompt)
print(response.text)

Rule-Based Logic Example
if "hello" in user_input.lower():
    return "Hello! How can I help you today?"

🌐 Deployment
Current Status: Not deployed
Possible deployment platforms (future):
Render
Railway
Azure App Service
AWS EC2
Google Cloud Run

📈 Impact & Metrics
Rule-based processing: Instant (<0.1s)
Gemini LLM response time: 0.5–1.5 seconds
Lightweight hybrid architecture
Low CPU & memory usage
Suitable for college demos and small applications

🚧 What’s Next (Future Improvements)
Add a web-based UI (Flask / Streamlit)
Add conversation history
Add vector memory using FAISS / Pinecone
Deploy online
Add voice-to-text support
Add multi-model switching (Gemini 1.5 Flash / Pro)

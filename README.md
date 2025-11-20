📘 AI Chatbot Hybrid – Final Project Documentation

✔ A hybrid AI chatbot built in Python that combines a local offline AI model (DialoGPT) with the Gemini Generative AI API. The system intelligently switches between the local model and the cloud model based on the user’s input to provide both fast and highly accurate responses.

🧰 ✔✔Tech Stack
✔Languages:
Python 3.10+

✔Frameworks & Libraries:
google-generativeai – Gemini API integration
dotenv – environment variable management
json, datetime, regex – Python core modules

transformers – for running the local DialoGPT model
torch – required backend for DialoGPT
DialoGPT-medium – local AI model for offline conversations

✔Developer Tools
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
✔Architecture Diagram
                ┌────────────────────┐
                │     User Input     │
                └─────────┬──────────┘
                          │
                          ▼
         ┌──────────────────────────────────────┐
         │      Hybrid Controller (Router)      │
         └─────────┬────────────────────────────┘
                   │
     ┌─────────────┴───────────────────────────┐
     │                                         │
     ▼                                         ▼
┌──────────────┐                      ┌─────────────────────────────┐
│ Local Model   │                      │   Gemini LLM (Cloud AI)    │
│ DialoGPT      │                      │ models/gemini-2.5-flash     │
│ Offline AI    │                      │ via google-generativeai     │
└──────────────┘                      └─────────────────────────────┘
     │                                         │
     └─────────────────────┬───────────────────┘
                           ▼
               ┌─────────────────────────┐
               │   Final Chat Response   │
               └─────────────────────────┘



*Explanation:
✔This chatbot uses a hybrid AI system.  
✔If the user types a normal message, the program uses DialoGPT-medium (a local offline model) to generate a response.  
✔If the user types a message starting with "gemini:", the Hybrid Controller forwards the request to Google Gemini 2.5 Flash using the google-generativeai API.
✔This design combines offline speed with cloud-level intelligence.

✨ Core Features
✔ Hybrid AI System (Local + Cloud).
✔ Local Offline AI using DialoGPT (works without internet).
✔ Cloud AI using Gemini 2.5 Flash (intelligent responses).
✔ Smart model switching based on input.
✔ Secure API management with .env.
✔ Easy to extend and customize.

✔✔Trade-offs
✔ Local model has limited context and creativity.
✔ Gemini requires internet + API usage.
✔Basic CLI interface (can be upgraded to web UI later).

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

✔Activate:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install google-generativeai python-dotenv transformers torch

4️⃣ Create .env File
GEMINI_API_KEY=your_api_key_here

5️⃣ Run the Chatbot
python hybrid_chatbot.py

🗂 .env.example
# Gemini API Key
GEMINI_API_KEY=your_api_key_here

🔑 Key APIs & Components
✔Gemini API Initialization
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

✔Sending a Prompt to Gemini
gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")
prompt = "Explain AI"
response = gemini_model.generate_content(prompt)
print(response.text)

✔from transformers import AutoTokenizer, AutoModelForCausalLM
local_model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(local_model_name)
local_model = AutoModelForCausalLM.from_pretrained(local_model_name)

✔Generating a Response Using the Local DialoGPT Model:

new_input_ids = tokenizer.encode(
    user_input + tokenizer.eos_token,
    return_tensors="pt"
)

bot_input_ids = (
    torch.cat([chat_history_ids, new_input_ids], dim=-1)
    if chat_history_ids is not None
    else new_input_ids
)

chat_history_ids = local_model.generate(
    bot_input_ids,
    max_length=1000,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.8,
)

reply = tokenizer.decode(
    chat_history_ids[:, bot_input_ids.shape[-1]:][0],
    skip_special_tokens=True
)

print("Local AI:", reply)


🌐 Deployment
Current Status: Not deployed
✔Possible deployment platforms (future):
✔Render
✔Railway
✔Azure App Service
✔AWS EC2
✔Google Cloud Run

📈 Impact & Metrics
✔ Local DialoGPT processing: Instant (<0.1s)
✔ Gemini LLM response time: 0.5–1.5 seconds
✔ Lightweight hybrid architecture
✔ Low CPU & memory usage
✔ Suitable for college demos and small applications

🚧 What’s Next (Future Improvements)
✔ Add a web-based UI (Flask / Streamlit)
✔ Add conversation history
✔ Add vector memory using FAISS / Pinecone
✔ Deploy online
✔ Add voice-to-text support
✔ Add advanced model switching between more Gemini models
(e.g., Gemini 2.5 Pro, Gemini 2.5 Flash-L, etc.)

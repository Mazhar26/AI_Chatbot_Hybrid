📘 AI Chatbot Hybrid – Final Project Documentation

## AI-Powered Hybrid Chatbot

AI-Powered Hybrid Chatbot is a Python-based CLI application that dynamically routes user queries between a local DialoGPT model and the Gemini Generative AI API, balancing offline speed with cloud-level intelligence.

## What You’ll See in This Repo:
- hybrid_chatbot.py — Main program
- README.md — Documentation
- .env.example — Environment setup


### Tech Stack

### Languages
- Python 3.10+

### Frameworks & Libraries
- google-generativeai (Gemini API)
- python-dotenv
- transformers
- torch
- DialoGPT-medium

### Developer Tools
- VS Code
- Git & GitHub
- Virtual Environment (venv)

Versions (Recommended)
| Component           | Version   |
| ------------------- | --------- |
| Python              | 3.10–3.12 |
| google-generativeai | ^0.3+     |
| python-dotenv       | ^1.0      |



### System Architecture
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



## Explanation
- This chatbot uses a hybrid AI system.
- If the user types a normal message, the program uses DialoGPT-medium (a local offline model).
- If the user types a message starting with "gemini:", the request is forwarded to Google Gemini 2.5 Flash via the API.
- This design combines offline speed with cloud-level intelligence.

## Core Features
- Hybrid AI System (Local + Cloud).
- Local Offline AI using DialoGPT (works without internet).
- Cloud AI using Gemini 2.5 Flash (intelligent responses).
- Smart model switching based on input.
- Secure API management with .env.
- Easy to extend and customize.

### Trade-offs
- Local model has limited context and creativity.
- Gemini requires internet + API usage.
- Basic CLI interface (can be upgraded to web UI later).

## Setup & Run Guide

### Prerequisites
- Python 3.10+
- Gemini API Key (from Google AI Studio)
- Git

1️⃣  Clone the Repository
git clone https://github.com/Mazhar26/AI_Chatbot_Hybrid.git
cd AI_Chatbot_Hybrid

2️⃣ Create Virtual Environment
python -m venv venv

### Activate:
***Windows***
bash
venv\Scripts\activate

***Linux/macOs***
bash
source venv/bin/activate

3️⃣ Install Dependencies
pip install google-generativeai python-dotenv transformers torch

4️⃣ Create .env File
GEMINI_API_KEY=your_api_key_here

5️⃣ Run the Chatbot
python hybrid_chatbot.py

.env.example
GEMINI_API_KEY=your_api_key_here

### Key Components
- Gemini API integration using google-generativeai
- Local inference using DialoGPT via Hugging Face Transformers
- Secure API key management using environment variables

### Sending a Prompt to Gemini
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")
prompt = "Explain AI"
response = gemini_model.generate_content(prompt)
print(response.text)


### Local Model Setup(DialoGPT)
from transformers import AutoTokenizer, AutoModelForCausalLM

local_model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(local_model_name)
local_model = AutoModelForCausalLM.from_pretrained(local_model_name)


### Generating a Response Using the Local DialoGPT Model:
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



### Deployment
Current Status: Not deployed

Possible deployment platforms (future):
-Render
-Railway
-Azure App Service
-AWS EC2
-Google Cloud Run

## Performance Notes
- Local DialoGPT responses are near-instant for simple queries
- Cloud-based Gemini responses depend on network latency
- Lightweight architecture suitable for small applications and demos

## Possible Extensions
- Add a web-based UI (Flask / Streamlit)
- Add conversation history
- Add vector memory using FAISS / Pinecone
- Deploy online
- Add voice-to-text support
- Add advanced model switching between more Gemini models
  (e.g., Gemini 2.5 Pro, Gemini 2.5 Flash-L, etc.)

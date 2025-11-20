import os
from dotenv import load_dotenv
import google.generativeai as genai
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Model
gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")

# Load local DialoGPT
print("Loading DialoGPT model...")
local_model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(local_model_name)
local_model = AutoModelForCausalLM.from_pretrained(local_model_name)

chat_history_ids = None

print("\nHybrid Chatbot Ready!")
print("Type 'gemini:' before a message to use the Gemini API.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # Gemini mode
    if user_input.lower().startswith("gemini:"):
        prompt = user_input.replace("gemini:", "").strip()

        try:
            response = gemini_model.generate_content(prompt)
            print("Gemini:", response.text)
        except Exception as e:
            print("Gemini Error:", e)

        continue

    # Local AI mode
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
        pad_token_id=tokenizer.eos_token_id
    )

    local_reply = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print("Local AI:", local_reply)

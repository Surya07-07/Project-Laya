import json
from datetime import datetime
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# Load DNA
def load_dna():
    with open("dna.json", "r") as f:
        return json.load(f)

# Log system
def log_action(text):
    with open("trust_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {text}\n")

# Memory
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

# 🧠 AI Brain
def ask_ai(user_input, dna, memory):

    system_prompt = f"""
You are Laya, a private AI assistant.

Rules (DNA):
- Owner: {dna['owner']}
- Privacy first
- Always honest
- Always explain
- Never hide actions
- Ask when unsure

Memory:
{memory}

User request:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content

# Main logic
def main():
    dna = load_dna()
    memory = load_memory()

    print("🧬 Laya v0.2 started (AI Brain Active)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        log_action(user_input)

        # memory command
        if "remember" in user_input.lower():
            memory["note"] = user_input
            save_memory(memory)
            print("Laya: Stored in memory.")
            continue

        if "what did you remember" in user_input.lower():
            print("Laya:", memory.get("note", "Nothing stored."))
            continue

        # AI response
        reply = ask_ai(user_input, dna, memory)
        print("Laya:", reply)

        log_action("Laya responded")

if __name__ == "__main__":
    main()

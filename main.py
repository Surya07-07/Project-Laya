import json
from datetime import datetime

# Load DNA
def load_dna():
    with open("dna.json", "r") as f:
        return json.load(f)

# Trust log
def log_action(text):
    with open("trust_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {text}\n")

# Simple memory
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

# Core Laya response logic
def laya_response(user_input, memory, dna):
    
    log_action(f"User said: {user_input}")

    # simple identity check (v0.1)
    if dna["security"]["require_identity"]:
        if "surya" not in user_input.lower():
            return "Identity not verified. Please include your name."

    # memory feature
    if "remember" in user_input.lower():
        memory["last_note"] = user_input
        save_memory(memory)
        return "I have stored this in memory."

    if "what did you remember" in user_input.lower():
        return memory.get("last_note", "I don't remember anything yet.")

    # default response
    return f"You said: {user_input}"

# Main loop
def main():
    dna = load_dna()
    memory = load_memory()

    print("Laya v0.1 started. Type 'exit' to stop.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = laya_response(user_input, memory, dna)
        print("Laya:", response)

if __name__ == "__main__":
    main()

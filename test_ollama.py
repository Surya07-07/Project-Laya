import ollama

client = ollama.Client(host="http://127.0.0.1:11434")

print("Connecting...")

response = client.chat(
    model="llama3.2:3b", messages=[{"role": "user", "content": "Hello Laya"}]
)

print(response["message"]["content"])

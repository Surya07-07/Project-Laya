from core.ai.ollama_client import OllamaClient

client = OllamaClient()

print("Model:", client.model)

response = client.ask("Say hello in one sentence.")

print(response)

from core.context.context_engine import ContextEngine

engine = ContextEngine()

history = []

memories = {
    "Name": "Surya",
    "IDE": "VS Code"
}

prompt = engine.build(
    history,
    memories,
    "Hello"
)

print(prompt)
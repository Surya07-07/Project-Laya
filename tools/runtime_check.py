import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from core.runtime.runtime import LayaRuntime

print("=" * 60)
print("PROJECT LAYA RUNTIME CHECK")
print("=" * 60)

print()

print("Creating Runtime...")

runtime = LayaRuntime()

print("✓ Runtime Created")

print()

print("Starting Runtime...")

runtime.start()

print()

print("✓ Runtime Started Successfully")
import subprocess
import sys

tests = [
    "tests.test_agent",
]

failed = False

for test in tests:
    print("=" * 60)
    print("Running", test)
    print("=" * 60)

    result = subprocess.run([sys.executable, "-m", test])

    if result.returncode != 0:
        failed = True

print()

if failed:
    print("Some tests failed.")
    sys.exit(1)

print("All tests passed.")

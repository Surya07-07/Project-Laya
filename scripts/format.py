import subprocess
import sys

subprocess.run([sys.executable, "-m", "isort", "."])
subprocess.run([sys.executable, "-m", "black", "."])

import subprocess
import sys
import os

def app():
    script_path = os.path.join(os.path.dirname(__file__), "interface.py")
    subprocess.run([sys.executable, script_path], check=True)

if __name__ == "__main__":
    app()
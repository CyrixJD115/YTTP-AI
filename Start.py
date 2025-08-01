#!/usr/bin/env python3
import sys
import os
import platform
import subprocess
import shutil
from pathlib import Path

# List of required packages for the Tkinter GUI version.
REQUIREMENTS = [
    "youtube-transcript-api",
    "python-docx>=1.1.0",
    "requests>=2.31.0"
]

def validate_python():
    """Ensure Python 3.7+ is used."""
    if sys.version_info < (3, 7):
        print("\n[ERROR] Python 3.7+ is required.")
        sys.exit(1)

def create_venv():
    """Create a virtual environment in the local 'venv' directory if it doesn't exist."""
    venv_dir = Path("venv")
    if venv_dir.exists():
        print("[INFO] Virtual environment already exists. Skipping creation.")
    else:
        try:
            print("[INFO] Creating virtual environment...")
            subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
            print("[INFO] Virtual environment created successfully.")
        except Exception as e:
            print(f"\n[ERROR] Failed to create virtual environment: {e}")
            sys.exit(1)

def install_dependencies():
    """Install required packages into the virtual environment (if not already installed)."""
    is_windows = platform.system() == "Windows"
    pip_exe = Path("venv") / ("Scripts" if is_windows else "bin") / ("pip.exe" if is_windows else "pip")
    print("[INFO] Installing dependencies (if not already installed)...")
    try:
        subprocess.run([str(pip_exe), "install"] + REQUIREMENTS, check=True)
        print("[INFO] Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("\n[ERROR] Dependency installation failed.")
        sys.exit(1)

def check_wkhtmltopdf():
    """Warn if wkhtmltopdf is not found (PDF export will be disabled)."""
    if not shutil.which("wkhtmltopdf"):
        print("\n[WARNING] wkhtmltopdf not found – PDF export will be disabled.")
        print("Installation instructions:")
        print("  Windows: https://wkhtmltopdf.org/downloads.html")
        print("  Linux:   sudo apt install wkhtmltopdf")
        print("  macOS:   brew install wkhtmltopdf")
    else:
        print("[INFO] wkhtmltopdf found.")

def launch_app():
    """Launch the main Tkinter GUI application using the virtual environment."""
    is_windows = platform.system() == "Windows"
    python_exe = Path("venv") / ("Scripts" if is_windows else "bin") / ("python.exe" if is_windows else "python")
    print("[INFO] Launching GUI application...")
    try:
        subprocess.run([str(python_exe), "main.py"], check=True)
    except KeyboardInterrupt:
        print("\n[INFO] User terminated the application.")
    except Exception as e:
        print(f"\n[ERROR] Failed to launch the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_python()
    create_venv()
    install_dependencies()
    check_wkhtmltopdf()
    print("\n[INFO] Environment ready! Launching application...\n")
    launch_app()

"""Installs pytest so you can check your exercise answers.

Run this file once. From an exercise folder, such as 01-counting-sheep:

    macOS:    python3 ../../setup_exercises.py
    Windows:  python ../../setup_exercises.py
"""

import subprocess
import sys

MINIMUM_PYTHON = (3, 9)


def pip_install(*extra_options):
    return subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pytest", *extra_options],
        capture_output=True,
        text=True,
    )


def main():
    version = ".".join(str(part) for part in sys.version_info[:3])
    print(f"Using Python {version}")

    if sys.version_info < MINIMUM_PYTHON:
        print(f"These exercises need Python {MINIMUM_PYTHON[0]}.{MINIMUM_PYTHON[1]} or newer.")
        print("Please install a newer Python from https://www.python.org/downloads/")
        sys.exit(1)

    print("Installing pytest. This can take a minute...")
    result = pip_install()
    messages = result.stdout + result.stderr

    if result.returncode != 0 and "No module named pip" in messages:
        print("pip is missing. Installing pip first...")
        subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade"], capture_output=True, text=True)
        result = pip_install()
        messages = result.stdout + result.stderr

    if result.returncode != 0 and "externally-managed-environment" in messages:
        # Python from Homebrew blocks global installs, so install for this user only.
        print("This Python does not allow global installs. Installing pytest for your user instead...")
        result = pip_install("--user", "--break-system-packages")
        messages = result.stdout + result.stderr

    if result.returncode != 0:
        print(messages)
        print("Setup did not work. Show the message above to a teacher.")
        sys.exit(1)

    check = subprocess.run([sys.executable, "-m", "pytest", "--version"], capture_output=True, text=True)
    if check.returncode != 0:
        print(check.stdout + check.stderr)
        print("pytest was installed, but it does not start. Show the message above to a teacher.")
        sys.exit(1)

    print(f"Done! {(check.stdout + check.stderr).strip()} is installed.")
    print("You can now check your answers from any exercise folder:")
    print("    macOS:    python3 -m pytest")
    print("    Windows:  python -m pytest")


if __name__ == "__main__":
    main()

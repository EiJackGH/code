# Troubleshooting Installation Errors

This guide provides solutions to common installation and environment setup errors encountered when running the **Bitcoin Trading Simulation** or the C++ experimental projects in this repository.

---

## 1. Python Environment & Dependency Issues

### Error: `ModuleNotFoundError: No module named '...'` (e.g., `requests`, `pandas`, `numpy`, `pytest`)
This happens when the required third-party Python modules are not installed in your current active environment.

**Solution:**
Ensure you install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
If you are running tests, ensure `pytest` is installed:
```bash
pip install pytest
```

### Error: `pytest` command not found
If you run `pytest` and get a "command not found" error, it means the `pytest` executable is not in your system's PATH.

**Solution:**
You can invoke `pytest` directly through your Python interpreter, which guarantees it runs within the correct environment:
```bash
python -m pytest
```

### Error: `venv` installation failure in CI/CD or via Pip
If you encounter errors trying to install a package named `venv` via pip, or see a build failure regarding `venv` in `requirements.txt`:

**Solution:**
Do not list `venv` in `requirements.txt`. `venv` is a standard library module that comes pre-packaged with Python 3. It is not a PyPI package, so trying to install it via `pip` will fail. If it was present, remove it from `requirements.txt`.

### Permission Errors during `pip install`
If you get permission denied or access errors (especially on Linux/macOS):

**Solution:**
Avoid using `sudo pip install`. Instead, use a virtual environment (recommended) or install the packages for your user only:
```bash
pip install --user -r requirements.txt
```

---

## 2. Virtual Environment Setup Guide

Using a virtual environment is highly recommended to isolate dependencies and avoid conflicts with other Python projects on your system.

### How to Create and Activate a Virtual Environment

1. **Create the environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the environment:**
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **On Windows (PowerShell):**
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - **On Windows (Command Prompt):**
     ```bash
     .\venv\Scripts\activate.bat
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Deactivate when done:**
   ```bash
   deactivate
   ```

---

## 3. C++ Environment & Compilation Errors (e.g., NumberGuess)

The repository contains experimental C++ terminal-based projects (such as `NumberGuess`). If you run into build issues:

### Error: `g++` or `make` command not found
This occurs when the C++ compiler or building utility is not installed.

**Solution:**
- **On Debian/Ubuntu:**
  ```bash
  sudo apt update
  sudo apt install build-essential
  ```
- **On macOS (via Homebrew or Xcode):**
  ```bash
  xcode-select --install
  ```
- **On Windows:**
  Install MinGW or use MSYS2 to obtain `g++` and `make`.

### Input validation infinite loops
If the terminal-based C++ application goes into an infinite loop upon entering a non-numeric value:

**Solution:**
Validate user inputs and clear the stream error states properly in the code:
```cpp
std::cin.clear();
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```

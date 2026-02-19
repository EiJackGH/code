## 2024-05-22 - [CLI Dashboard Pattern]
**Learning:** Simple CLI outputs can be significantly improved by using ASCII box-drawing characters and padded alignment to create a "dashboard" feel. Users perceive this as more polished and professional than raw text streams. Also, ensure `--quiet` flags silence *all* intermediate output to respect user intent.
**Action:** Use Python f-string alignment (`<`, `>`, `^`) and box-drawing characters for final summary reports in CLI tools.

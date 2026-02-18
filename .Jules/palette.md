## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-05-27 - CLI Accessibility & Robustness
**Learning:** Hardcoded ANSI colors without a disable mechanism exclude users with accessibility needs or those parsing logs. A crash when disabling colors is a critical failure.
**Action:** Always implement a robust `--no-color` flag and ensure `Colors` class handles disabling correctly. Input validation preventing runtime crashes (like ZeroDivisionError or negative inputs) is critical UX.

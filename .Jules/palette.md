## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-01 - Defensive CLI Design
**Learning:** Users often mistype arguments (e.g., negative numbers). Without validation, this leads to confusing output or crashes. Friendly error messages with actionable feedback are crucial for CLI usability.
**Action:** Always implement explicit validation for CLI arguments and provide colored, clear error messages before starting any heavy processing.

## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-16 - Interactive CLI Progress Indicators
**Learning:** For long-running CLI processes that suppress verbose logging (e.g., `--quiet` mode), users can become anxious and terminate the script prematurely if there is no visual feedback.
**Action:** Implement a dynamic progress bar using `\r` and `flush=True` (conditional on `sys.stdout.isatty()`) to provide system status visibility without polluting standard output logs or breaking non-interactive environments.

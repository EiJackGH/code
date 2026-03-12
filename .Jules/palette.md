## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-12 - Silent Mode Visibility
**Learning:** For long-running CLI processes that suppress verbose logging (e.g., `--quiet`), implementing a dynamic progress bar using `\r` and `flush=True` (conditional on `sys.stdout.isatty()`) provides critical system status visibility without polluting standard output logs.
**Action:** Always include a visual progress indicator for silent, long-running CLI tasks when run interactively to prevent users from thinking the process has stalled.

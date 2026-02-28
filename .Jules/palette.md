## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2026-02-28 - Interactive Progress Bars for Suppressed Logs
**Learning:** When users pass a '--quiet' flag to suppress verbose logging in a CLI app, long-running processes can appear frozen or broken, causing confusion.
**Action:** When suppressing daily or detailed logs, implement a dynamic, single-line progress bar (guarded by checking if stdout is a TTY) to provide visual assurance that the process is still running.

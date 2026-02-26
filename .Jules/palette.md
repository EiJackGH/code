## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-05-15 - Quiet Mode Feedback
**Learning:** "Quiet" mode should not mean "silent hang". Users need reassurance that long-running processes are active.
**Action:** When using `--quiet`, suppress detailed logs but display a minimal progress bar or spinner if the session is interactive (`sys.stdout.isatty()`).

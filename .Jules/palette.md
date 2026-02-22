## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-01 - CLI Progress Feedback
**Learning:** For long-running CLI processes (simulations), users need feedback. However, simply printing logs can be spammy. A text-based progress bar that only appears in interactive sessions (`sys.stdout.isatty()`) provides the best balance of feedback vs. cleanliness.
**Action:** Use `sys.stdout.write('\r...')` with `isatty()` checks for progress indicators in CLI tools.

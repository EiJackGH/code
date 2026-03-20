## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-14 - Dynamic Progress Bars in Quiet CLI Modes
**Learning:** For long-running CLI applications that support a `--quiet` flag (which normally suppresses verbose logging), providing a dynamic progress bar using `\r` and `flush=True` (conditional on `sys.stdout.isatty()`) offers a much better UX. It gives the user necessary status visibility during long executions without polluting non-interactive environments (like CI/CD) or file redirections.
**Action:** Always consider replacing suppressed verbose output with a dynamic progress bar for long-running scripts when `--quiet` mode is active and the terminal is interactive.

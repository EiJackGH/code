## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-05 - CLI Progress Indicators
**Learning:** Running long CLI simulations with `--quiet` leads to confusing silence before the final output. Users might think the program froze. Using `\r` (carriage return) for a text-based progress bar, conditionally rendered if `sys.stdout.isatty()`, provides necessary visibility without cluttering standard output logs or CI/CD systems.
**Action:** Always add dynamic text-based progress indicators (`\r` loops) for long operations in CLI tools that suppress verbose logging. Check `sys.stdout.isatty()` to prevent log pollution.

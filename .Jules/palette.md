## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-01 - Progress Visualizations
**Learning:** For long-running CLI processes, particularly those that suppress verbose logging (e.g., `--quiet`), users can be left wondering if the program has stalled. Adding an interactive, dynamic progress bar using `\r` provides critical system status visibility without polluting standard output logs.
**Action:** When creating CLI tools with potentially long execution times or loops over large data structures (like Pandas DataFrames), implement a simple dynamic progress bar, conditional on `sys.stdout.isatty()`.

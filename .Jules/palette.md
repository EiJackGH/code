## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.
## 2024-05-20 - Dynamic Progress Bar for Quiet CLI Tasks
**Learning:** For long-running CLI processes that suppress verbose logging (e.g., `--quiet`), users lose system status visibility.
**Action:** Implemented a dynamic progress bar using `\r` and `flush=True`, conditional on `sys.stdout.isatty()`, to provide status feedback without polluting non-interactive logs.

## 2025-03-23 - Game Key Scrolling
**Learning:** Browsers natively scroll the page when users press Space or Arrow keys. When building a web-based game, this creates a frustrating UX where the game viewport jumps around while playing.
**Action:** Always call `e.preventDefault()` on keydown events for typical game controls ("Space", "ArrowUp", etc.) when the focus is on a game container or the body.

## 2026-04-10 - Thousands Separators for Numerical Output
**Learning:** Dense numerical data (like $10000.00) in CLI output is hard to parse and increases cognitive load. Adding thousands separators ($10,000.00) significantly improves readability and the perceived quality of the tool.
**Action:** Always use thousands separators (e.g., `:,.2f` in Python) when formatting large numerical or financial values in CLI outputs.

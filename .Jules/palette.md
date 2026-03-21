## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.
## 2024-05-20 - Dynamic Progress Bar for Quiet CLI Tasks
**Learning:** For long-running CLI processes that suppress verbose logging (e.g., `--quiet`), users lose system status visibility.
**Action:** Implemented a dynamic progress bar using `\r` and `flush=True`, conditional on `sys.stdout.isatty()`, to provide status feedback without polluting non-interactive logs.

## 2024-05-24 - Web Game Keyboard Controls UX
**Learning:** Using 'Space' or 'Arrow' keys to trigger interactions in web apps (like jumping in a game) without calling `e.preventDefault()` causes the browser to naturally scroll the page. This breaks the gameplay experience as the user is thrown out of context.
**Action:** Always capture and prevent default behavior on keyboard events that share bindings with native browser navigation (like Space/Arrow keys for scrolling) when implementing custom interactive widgets or games.

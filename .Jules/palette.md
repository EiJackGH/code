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

## 2026-07-02 - Web Game Keyboard Accessibility and Instructions
**Learning:** For interactive HTML5 widgets or games with custom keyboard event bindings, always provide explicit, visible instructional text so users know the required inputs. Additionally, do not place static text (like instructions) inside an `aria-live` region, as it forces screen readers to unnecessarily repeat the static text every time the dynamic content updates. Extract static text into a separate sibling element.
**Action:** When adding dynamic status updates (like scores) alongside instructions, keep them as separate elements. Add `aria-live="polite"` and `aria-atomic="true"` only to the element containing the dynamic content to maintain clean screen reader announcements.

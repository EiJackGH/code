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

## 2025-07-10 - Explicit Game Controls and aria-live Separation
**Learning:** When building interactive HTML5 widgets or games with custom keyboard event bindings, users need explicit, visible instructional text so they know the required inputs. Furthermore, it's critical to keep static instructions outside of `aria-live` regions, otherwise screen readers will unnecessarily repeat the static text every time the dynamic content updates.
**Action:** Always provide explicit instructional text for custom controls. Extract static text into a separate sibling element away from any `aria-live` regions tracking dynamic updates like scores.

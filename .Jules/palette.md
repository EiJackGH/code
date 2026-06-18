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

## 2025-05-18 - Missing Screen Reader Feedback on Dynamic Scores
**Learning:** For dynamic real-time values like game scores that update frequently without page reloads, screen reader users miss out on crucial context if live regions are not used. Adding `aria-live` is critical.
**Action:** Always include `aria-live="polite"` and `aria-atomic="true"` on scoreboards, progress indicators, or dynamic text containers in custom UI or web games to ensure announcements are properly queued and read out.

## 2025-05-18 - "Invisible" Controls in Custom Game UIs
**Learning:** Creating custom keyboard event listeners in web interfaces (like space to jump) is often totally undiscoverable to users without explicit onboarding text.
**Action:** Whenever binding custom navigation or game actions to keydown events, verify that instructional helper text is visibly rendered in the UI context so users know what inputs are expected.

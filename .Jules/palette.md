## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2026-02-11 - Accessibility in CLI Tools
**Learning:** Hardcoded ANSI colors exclude users with visual impairments or conflicting terminal themes. Providing a standard `--no-color` flag is a zero-cost accessibility win that respects user preference.
**Action:** Always wrap color codes in a configurable class and expose a disable mechanism via CLI arguments.

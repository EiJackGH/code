## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Accessibility & Pipeability
**Learning:** Hardcoded ANSI color codes in CLI tools break accessibility for screen readers and make piping output to files messy. Users need a way to disable them.
**Action:** Always implement a `--no-color` flag in CLI tools that programmatically disables all color codes.

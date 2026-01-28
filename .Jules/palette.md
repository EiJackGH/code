## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-24 - Accessibility and Control in CLI Tools
**Learning:** While rich CLI output (colors, emojis) is helpful, it can become "spammy" or inaccessible. Providing control via flags like `--quiet` (for focus) and `--no-color` (for accessibility/compatibility) is crucial for a complete UX.
**Action:** Always include flags to suppress verbose output and disable ANSI colors in CLI tools.

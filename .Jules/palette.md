## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - Accessibility and Customization in CLI Tools
**Learning:** While rich CLI output is engaging, it can be problematic for accessibility or automated parsing. Providing flags like `--no-color` and `--quiet` ensures the tool is versatile and inclusive.
**Action:** Always include `--no-color` and `--quiet` flags in CLI tools that use rich formatting.

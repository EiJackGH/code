## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - Accessibility and Control in CLI Tools
**Learning:** While color and emojis improve scannability, they can be distracting or inaccessible (e.g., for color-blind users or automated parsing). Providing `--no-color` and `--quiet` flags is essential for accessibility and flexibility.
**Action:** Always include flags to disable visual enhancements and suppress verbose output in CLI tools to respect user preferences and support automation.

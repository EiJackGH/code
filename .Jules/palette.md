## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-24 - Accessibility in CLI Tools
**Learning:** While colors and emojis improve scannability, they can be inaccessible to screen readers or users with specific terminal configurations. Providing standard flags like `--quiet` (for reducing noise) and `--no-color` (for plain text) is a critical UX pattern for CLI tools, allowing users to tailor the experience to their needs.
**Action:** Always include `--quiet` and `--no-color` flags in CLI applications to support diverse user needs and automation use cases.

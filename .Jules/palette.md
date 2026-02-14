## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Accessibility and Control
**Learning:** While color and emojis enhance UX, they can be inaccessible (color blindness) or intrusive (automation logs). Providing `--no-color` and `--quiet` flags is essential for a robust CLI tool that respects user context and accessibility needs.
**Action:** Always include flags to disable visual enhancements and suppress verbose output in CLI tools.

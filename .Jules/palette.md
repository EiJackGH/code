## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Accessibility and Control
**Learning:** While color and emojis enhance UX, they can be inaccessible (color blindness) or intrusive (automation logs). Providing `--no-color` and `--quiet` flags is essential for a robust CLI tool that respects user context and accessibility needs.
**Action:** Always include flags to disable visual enhancements and suppress verbose output in CLI tools.

## 2024-05-24 - Readable Data Formatting in CLI
**Learning:** Large numbers without separators (e.g., 1000000) are hard to parse at a glance. Fixed-width alignment and thousands separators ($1,000,000) create a tabular layout that drastically improves data readability and scanability.
**Action:** Always format monetary/large values with separators and use f-string alignment for tabular data in CLI output.

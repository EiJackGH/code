## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Configurability and Noise Reduction
**Learning:** Hardcoded values in CLI tools limit usability. Providing arguments for key parameters (like `--days`, `--initial-cash`) empowers users. Additionally, offering a `--quiet` flag to suppress verbose logging (while keeping critical events) and a `--no-color` flag for accessibility/logging is essential for a polished CLI experience.
**Action:** Always implement `argparse` (or similar) with quiet and no-color options for CLI tools that produce significant output.

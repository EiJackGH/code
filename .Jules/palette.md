## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Accessibility & Usability
**Learning:** CLI tools often lack accessibility features like disabling color output, and usability features like customizable parameters without code edits.
**Action:** Always add `argparse` with `--no-color` and `--quiet` flags to Python CLI tools.

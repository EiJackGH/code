## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2026-02-06 - CLI Accessibility Standards
**Learning:** CLI tools are surprisingly inaccessible without standard flags like `--no-color` and `--quiet`. Users expect these controls to integrate with scripts and accessibility tools.
**Action:** Always implement `argparse` with quiet/color-disable options for any CLI outputting more than 5 lines.

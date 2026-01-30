## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-22 - CLI User Experience
**Learning:** CLI tools often lack basic customization and accessibility features like color toggles or quiet modes, making them harder to use in scripts or for users with visual impairments.
**Action:** Always check for and implement `argparse` with standard flags (`--quiet`, `--no-color`) in Python CLI tools to improve flexibility and accessibility.

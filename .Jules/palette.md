## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2026-01-26 - CLI Accessibility & Customization
**Learning:** Even in CLI tools, accessibility matters. Providing `--no-color` supports users with terminal restrictions or color vision deficiencies. Customization via arguments (vs. hardcoding) transforms a script into a tool.
**Action:** When working on CLI scripts, always implement `argparse` or similar to expose key parameters and display options to the user.

## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - Accessibility in CLI Tools
**Learning:** Command-line tools with hardcoded colors can be inaccessible or noisy in certain terminals/logs. Offering a `--no-color` and `--quiet` flag respects user preference and environment constraints.
**Action:** Always include standard `argparse` flags for verbosity and color control in CLI utilities.

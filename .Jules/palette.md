## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - Accessibility & Control in CLI Tools
**Learning:** Even in CLI environments, users need control over verbosity (`--quiet`) and accessibility settings (`--no-color`). Hardcoded values and unstoppable output streams are bad UX patterns that are easily fixed with standard arguments.
**Action:** Always include standard flags for controlling output verbosity and ANSI color usage in CLI tools.

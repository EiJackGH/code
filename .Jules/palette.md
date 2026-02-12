## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Accessibility and Configuration
**Learning:** Hardcoded simulation parameters create friction and limit accessibility. Adding CLI arguments (`argparse`) empowers users to explore scenarios without code edits. Additionally, providing a `--no-color` flag is crucial for users with visual impairments or those piping output to logs.
**Action:** Always implement standard CLI flags for configuration and accessibility (quiet mode, no-color) in command-line tools.

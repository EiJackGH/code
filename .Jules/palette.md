## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-10-24 - CLI Accessibility and Configuration
**Learning:** Hardcoded values and mandatory color codes limit CLI usability and accessibility. `--no-color` supports monochrome terminals/parsing, and `argparse` empowers users.
**Action:** Always wrap CLI entry points with argument parsing and provide flags to disable purely visual features like color.

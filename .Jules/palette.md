## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-10-24 - CLI Accessibility and Control
**Learning:** While colors improve scannability, they can be inaccessible or noisy in certain contexts. Users also need control over simulation parameters without modifying code.
**Action:** Implement `--no-color` for accessibility and `--quiet` for reduced verbosity. Use `argparse` to expose key parameters like simulation duration and initial capital.

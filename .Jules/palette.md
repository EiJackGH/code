## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2024-05-23 - CLI Accessibility and Configuration
**Learning:** While color-coding is great, it must be optional. Adding a `--no-color` flag is crucial for accessibility (e.g., color blindness, strict terminal environments). Similarly, a `--quiet` flag respects the user's need for concise output in automated pipelines.
**Action:** Always include `--no-color` and `--quiet` flags in CLI tools to support diverse user needs and environments.

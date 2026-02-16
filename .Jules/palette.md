## 2024-05-22 - Visual Hierarchy in CLI Output
**Learning:** Adding color-coded indicators (Green/Red) and emojis (💰, 📉) in CLI tools significantly reduces cognitive load when parsing financial data streams. It transforms a wall of text into a scannable narrative.
**Action:** For data-heavy CLI applications, always implement a semantic color system and visual anchors (icons/emojis) for key events.

## 2026-02-02 - CLI Accessibility & Verbosity
**Learning:** For CLI tools, allowing users to control verbosity (`--quiet`) and disable colors (`--no-color`) is a critical accessibility feature. It helps users who rely on screen readers or have specific terminal constraints, and prevents "wall of text" fatigue.
**Action:** Always wrap CLI entry points with `argparse` (or similar) and include standard flags for controlling output style and volume.

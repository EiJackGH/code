## 2025-02-23 - CLI Visual Hierarchy
**Learning:** CLI tools are often neglected in terms of UX. Adding semantic colors (Green/Red) and emojis (🟢/🔴) significantly improves the scannability of logs, acting as visual anchors for important events.
**Action:** When working on CLI tools, always check if the output stream supports ANSI colors and use them to highlight key state changes or results, ensuring a fallback or textual indicator (like +/- signs or icons) exists for accessibility.

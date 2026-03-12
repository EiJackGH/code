## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-03-03 - C++ Game Flow and Persistence
**Learning:** Implementing a "play-again" loop in C++ using a `do-while` loop improves game flow by avoiding the need for repeated program execution. ANSI color constants and `<iomanip>` can be used in C++ to achieve the "Palette" aesthetic with structured results boxes and colorful feedback.
**Action:** Use file-based persistence (e.g., `fstream`) to store high scores across sessions, providing users with a sense of progression and competition.

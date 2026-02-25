## 2024-05-23 - CLI UX Enhancement
**Learning:** Even in CLI apps, visual distinction (colors, emojis) significantly reduces cognitive load when scanning logs.
**Action:** Use ANSI colors and consistent emojis for key events (success/failure) in future CLI tools.

## 2025-02-28 - Structured CLI Reports
**Learning:** Dense numerical data in CLI output is hard to parse. Using ASCII box-drawing characters and alignment to create a "dashboard" or "invoice" style summary significantly improves readability and perceived quality.
**Action:** When summarizing simulation or batch job results, always format the final report as a structured table or box rather than a list of print statements.

## 2025-06-15 - CLI Input Hygiene
**Learning:** Default validation errors (stack traces, unhandled exceptions) break the "tool" illusion and feel amateur. Friendly, upfront validation with color-coded errors (e.g. "Error: Days must be positive") establishes trust and guides the user.
**Action:** Always validate CLI arguments explicitly before execution and use `sys.exit(1)` with a clear message.

# Palette's UX Learnings - Bitcoin Trading Simulation

## CLI Delight
- **Visual Structure:** Using box-drawing characters (`┏`, `┃`, `┗`, `━`) helps separate the final report from the scrolling logs, making it easier for users to find the most important information.
- **Emoji Semantics:**
  - `🟢` and `🔴` are excellent for quick status indication (Buy/Sell, Profit/Loss).
  - `🛒` (Buy) and `🏷️` (Sell) add a touch of personality to trade statistics.
  - `🚀` and `📉` provide immediate feedback on strategy performance relative to benchmarks.
- **Color Contrast:** Using `CYAN` for values and `BOLD` for headers improves readability in dense CLI output.

## Accessibility
- **No-Color Mode:** Always respect the `--no-color` flag by providing a fallback that removes ANSI escape codes while maintaining structure through spacing and symbols.
- **Quiet Mode:** `quiet` flags should suppress high-volume output (like daily ledgers) but can still show the final result, as long as it's clearly documented.

## Code Quality for UX
- **Consolidated Styling:** A single `Colors` class with a `disable()` method ensures consistent styling across the application and easier maintenance for future theme changes.
- **Data Clarity:** Providing "Strategy Return %" alongside absolute values helps users quickly grasp the magnitude of their performance without doing mental math.

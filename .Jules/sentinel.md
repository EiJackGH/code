## 2025-05-15 - [Unbounded CLI Arguments Cause DoS]
**Vulnerability:** The simulation script accepted unbounded `days` input, allowing a user to trigger a massive loop consuming CPU/Memory (Denial of Service).
**Learning:** `argparse` type checking (`type=int`) is insufficient for resource-intensive parameters. It does not validate ranges or logical constraints.
**Prevention:** Always implement explicit range checks (e.g., `0 < days <= MAX_LIMIT`) for CLI arguments that control loop iterations or resource allocation.

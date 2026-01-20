## 2024-05-22 - [CLI Color Coding]
**Learning:** Even in CLI tools, color coding and emojis drastically improve the "glanceability" of data streams (logs). Users can instantly distinguish good (Buy/Profit) from bad (Sell/Loss) events without reading the text.
**Action:** When working on CLI tools in the future, check if output is a "wall of text" and introduce semantic coloring for key events. Use a simple `Colors` class to keep it dependency-free for small scripts.

# Journal Project -- Iteration Log

## Milestone 3: Journal Capture Workflow

---

## v3.1 -- Initial journal capture

**Goal:** Remove Excel from the daily journaling workflow while keeping the project lightweight.

**What changed**
- Created `Scripts/add_thought.py`.
- Added support for manually selecting a journal date.
- Automatically appends new thoughts to `Thoughts.csv`.
- Added UTF-8 support for emojis and special characters.
- Fixed the CSV append edge case to ensure every thought is written as a new row.

**Key learning**

The biggest source of friction was not finding old thoughts—it was getting new thoughts into the system quickly.

---

## v3.2 -- Complete journal capture workflow

**Goal:** Reduce journal capture to a single command while preserving the simplicity of the project.

**What changed**
- Replaced single-line terminal input with platform-aware clipboard import for macOS and Windows.
- Preserved multi-paragraph journal entries exactly as written.
- Added a simple "Journal Capture" terminal interface.
- Displayed today's date as the default while still allowing backdating.
- Automatically rebuilds the dashboard after each new entry.
- Automatically opens the updated dashboard in the default browser.

**Key learning**

The most valuable improvement was not adding new functionality—it was removing friction. Making journal capture effortless makes the project far more likely to be used consistently.

---

## Workflow improvement

### Previous workflow

```text
Write thought
→ Open Excel
→ Paste
→ Save
→ Run build_dashboard.py
```

### Current workflow

```text
Write thought in Notes
→ Copy
→ python Scripts/add_thought.py
→ Enter date (or press Enter for today)
→ Press Enter
→ Dashboard rebuilds automatically
→ Dashboard opens automatically
```

---

## Current state (Milestone 3 complete)

- CSV-based journal storage
- Static HTML dashboard
- Beautiful reading interface
- Year filtering
- Live search
- Search result summary
- Highlighted search matches
- Clipboard-based journal capture
- Multi-paragraph support
- Emoji support
- Automatic dashboard rebuild
- Automatic dashboard launch

---

## Explicit non-goals

- No AI summaries
- No semantic search
- No embeddings or vector databases
- No sentiment analysis
- No automatic tagging
- No web application

Milestone 3 focused on removing friction from the journaling process rather than adding intelligence. The project now provides a complete end-to-end workflow—from capturing a thought to viewing it in the dashboard—while remaining lightweight, maintainable, and entirely file-based.
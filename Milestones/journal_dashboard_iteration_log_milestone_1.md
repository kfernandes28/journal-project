# Journal Project -- Iteration Log

## Milestone 1: Journal Dashboard MVP

------------------------------------------------------------------------

## v1.1 -- Project foundation

**Goal:** Create a lightweight, maintainable structure for the journal
system.

**What changed** - Created the project structure: - `Data/` -
`Scripts/` - `Dashboard/` - Chose a simple architecture over a staged
pipeline for the MVP.

**Key learning** - The journal currently has a single clean data source,
so extra pipeline layers would add complexity without providing value.

------------------------------------------------------------------------

## v1.2 -- Journal data source

**Goal:** Establish a single source of truth for journal entries.

**What changed** - Stored all thoughts in `Thoughts.csv` - Standardised
each entry with: - `timestamp` - `text`

**Key learning** - A simple CSV is sufficient for validating the concept
before introducing databases or AI.

------------------------------------------------------------------------

## v1.3 -- HTML dashboard generator

**Goal:** Generate a static dashboard directly from Python.

**What changed** - Created `build_dashboard.py` - Reads `Thoughts.csv` -
Produces `Dashboard/index.html` - Adopted the same build pattern used in
other Life OS projects.

**Key learning** - A generated HTML dashboard is simple to maintain and
requires no web server or framework.

------------------------------------------------------------------------

## v1.4 -- Year filtering

**Goal:** Browse journal entries by year.

**What changed** - Added automatic year extraction from timestamps. -
Built a year selector. - Displayed only entries from the selected year.

**Key learning** - Organising reflections by year immediately makes the
journal feel like chapters of a book rather than a list of notes.

------------------------------------------------------------------------

## v1.5 -- Reading experience

**Goal:** Make the journal enjoyable to revisit.

**What changed** - Designed large journal cards. - Added generous
whitespace. - Used serif typography for the journal text. - Added entry
and word counts for the selected year.

**Key learning** - This project succeeds or fails on the reading
experience rather than data density.

------------------------------------------------------------------------

## Current state (Milestone 1 complete)

-   Project structure established
-   CSV-based journal storage
-   Python dashboard generator
-   Static HTML dashboard
-   Year selector
-   Year-specific journal view
-   Entry and word counts
-   Readable journal card layout

------------------------------------------------------------------------

## Explicit non-goals

-   No AI summaries
-   No sentiment analysis
-   No tagging
-   No embeddings or vector databases
-   No search
-   No automatic categorisation

Milestone 1 focused on validating that years of thoughts can be stored
and revisited in a way that is genuinely enjoyable to read before adding
intelligence or automation.

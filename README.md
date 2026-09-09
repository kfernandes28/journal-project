# Journal Dashboard

A lightweight personal reflection system for capturing, revisiting, and
exploring thoughts over time.

## Why I built this

I've never been a big fan of journaling in the traditional sense.
Sitting down at a fixed time to write often feels like capturing what I
think I should be thinking about in that moment, rather than the
thoughts that naturally appear when my mind wanders.

Instead, I've always preferred thought dumping --- writing something
down when an idea, question, or reflection appears during quieter
moments.

For about a year I kept those thoughts in the Notes app, but realised
they mostly just sat there. I rarely went back to them, which meant a
growing archive of thoughts without much opportunity to actually learn
from them.

That led to two questions:

-   Could I store those thoughts in a better way without adding friction
    to capturing them?
-   Could I make them genuinely useful later --- whether that means
    finding old ideas, seeing how my thinking has changed, or eventually
    identifying patterns across time?

This project started as a simple dashboard for revisiting those thoughts
and has gradually evolved into the beginning of a personal reflection
system.

------------------------------------------------------------------------

## Features

-   Store journal entries using a simple `timestamp` + `text` CSV
    structure
-   Browse reflections by year
-   View entry and word counts
-   Search thoughts instantly within the selected year
-   See search result summaries
-   Highlight matching search terms
-   Capture new thoughts directly from the clipboard
-   Use today's date or manually backdate an entry
-   Preserve multi-paragraph entries, emojis, and special characters
-   Automatically rebuild and open the dashboard after adding a thought
-   Fall back to safe sample data when no private journal file exists

------------------------------------------------------------------------

## Architecture

``` text
Notes / Clipboard
        ↓
Scripts/add_thought.py
        ↓
Data/Thoughts.csv
        ↓
Scripts/build_dashboard.py
        ↓
Dashboard/index.html
```

The project intentionally stays lightweight.

There is no database, web server, API, or application framework. A CSV
remains sufficient for the current use case, while Python generates a
static HTML dashboard for exploration.

------------------------------------------------------------------------

## Screenshots

### Journal Dashboard

```{=html}
<!-- Add main dashboard screenshot here -->
```
### Search & Discovery

```{=html}
<!-- Add search/highlighting screenshot here -->
```
### Journal Capture

```{=html}
<!-- Add terminal capture screenshot here -->
```

------------------------------------------------------------------------

## How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/kfernandes28/journal-project.git
cd journal-project
```

### 2. Create a virtual environment

``` bash
python3 -m venv venv
```

### 3. Activate it

macOS / Linux:

``` bash
source venv/bin/activate
```

Windows:

``` bash
venv\Scripts\activate
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

### 5. Build the dashboard

``` bash
python Scripts/build_dashboard.py
```

If `Data/Thoughts.csv` does not exist, the dashboard automatically uses
the included `Data/sample_thoughts.csv`.

The generated dashboard is written to `Dashboard/index.html` and opens
automatically in the default browser.

------------------------------------------------------------------------

## Adding Your Own Thoughts

Run:

``` bash
python Scripts/add_thought.py
```

The capture workflow will:

1.  Ask for a date, with today as the default
2.  Import the current clipboard contents
3.  Create `Data/Thoughts.csv` automatically if it does not already
    exist
4.  Append the new reflection
5.  Rebuild the dashboard
6.  Open the updated dashboard

Clipboard capture currently supports macOS and Windows using built-in
operating-system tools.

------------------------------------------------------------------------

## Privacy & Sample Data

Personal journal entries are intentionally kept outside version control.

`Data/Thoughts.csv` is excluded through `.gitignore`.

The repository instead includes `Data/sample_thoughts.csv`, which
provides synthetic demonstration data so the project can be cloned and
run without exposing private journal content.

Generated dashboard output and the local virtual environment are also
ignored.

------------------------------------------------------------------------

## Project Evolution

### Milestone 1 --- Journal Dashboard MVP

Built the initial CSV-backed dashboard with a lightweight project
structure, static HTML generation, year filtering, entry and word
counts, and a reading-focused journal layout.

The priority was proving that old thoughts could be revisited in a way
that felt enjoyable rather than building a complex analytics pipeline.

### Milestone 2 --- Search & Discovery

Added live journal search, dynamic result summaries, dynamic entry and
word counts, and highlighted search matches.

The goal was to make old reflections easy to find without needing to
remember when they were written.

### Milestone 3 --- Journal Capture Workflow

Removed Excel from the regular workflow by adding clipboard-based
journal capture, manual dates or today's date, multi-paragraph and emoji
support, automatic private CSV creation, automatic dashboard rebuilding,
and automatic dashboard opening.

The main lesson was that reducing friction could be more valuable than
adding another analytical feature.

Detailed iteration logs are available in the `Milestones/` directory.

------------------------------------------------------------------------

## Technologies

-   Python
-   pandas
-   CSV
-   HTML
-   CSS
-   JavaScript
-   Git / GitHub

------------------------------------------------------------------------

## What I Learned

-   A simple data model can be enough when the problem itself is still
    being explored.
-   The reading experience matters more than information density for a
    journal.
-   Search creates immediate value before more advanced analysis is
    necessary.
-   Reducing capture friction makes a system far more likely to be used
    consistently.
-   New features should solve problems revealed through real use rather
    than being added because they are technically interesting.
-   Personal projects benefit from separating private source data from
    safe public demo data from the start.

------------------------------------------------------------------------

## Future Direction

The longer-term idea is something closer to:

> **"Spotify Wrapped for thoughts."**

Rather than simply storing and searching reflections, the project could
eventually help surface changes that happen too slowly to notice day to
day --- recurring questions, emerging themes, forgotten ideas,
unresolved loops, and shifts in how someone thinks over time.

The goal is not to add AI for its own sake. Any future reflection engine
should first prove that it can surface genuinely useful insight from
accumulated journal history while preserving the lightweight philosophy
of the project.

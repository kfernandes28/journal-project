# Journal Dashboard

A personal thought analytics system that transforms raw journaling data into structured insights and visualisation.

## Overview

This project explores the idea of:

> “What if there was a Spotify Wrapped for your thoughts?”

It takes raw journal entries stored in CSV format and turns them into a structured dashboard showing patterns, trends, and reflections over time.

This is part of a larger “Life OS” system being built across finance, health, and personal reflection.

---

## Features

* Loads and processes raw `Thoughts.csv`
* Cleans and structures unformatted journal data
* Generates a yearly dashboard view of thoughts
* Simple HTML output for visual exploration
* Designed to be extended into a full analytics pipeline

---

## Project Structure

```
Dashboard/   → Core dashboard logic
Data/        → Input CSV files
Scripts/     → Processing and utilities
docs/        → Screenshots and documentation
```

---

## How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the dashboard script:

```
python Scripts/<main_script>.py
```

3. Open the generated HTML file in your browser.

---

## Vision

This project is not just a dashboard.

It is the first step toward a personal operating system that connects:

* Finance data
* Health data
* Thoughts and journaling
* Life patterns over time

The goal is to move from data collection → understanding → insight → action.

---

## Next Steps

* Improve structure into modular pipeline
* Add database layer (replace CSV)
* Build API layer for access
* Dockerise for reproducibility
* Integrate into full “Life OS”

---

## Author

Kellan Fernandes
Systems Engineering Graduate
Building a personal Life OS across finance, health, and cognition

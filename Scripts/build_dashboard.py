from pathlib import Path
import pandas as pd
import html
import json

BASE_DIR = Path(__file__).resolve().parents[1]

PRIVATE_DATA_PATH = BASE_DIR / "Data" / "Thoughts.csv"
SAMPLE_DATA_PATH = BASE_DIR / "Data" / "sample_thoughts.csv"

DATA_PATH = PRIVATE_DATA_PATH if PRIVATE_DATA_PATH.exists() else SAMPLE_DATA_PATH

OUT_DIR = BASE_DIR / "Dashboard"
OUT_PATH = OUT_DIR / "index.html"


def main():
    df = pd.read_csv(DATA_PATH)

    df["timestamp"] = pd.to_datetime(df["timestamp"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["timestamp", "text"])

    df["year"] = df["timestamp"].dt.year
    df["date_label"] = df["timestamp"].dt.strftime("%d %B %Y")
    df["sort_date"] = df["timestamp"]

    df = df.sort_values("sort_date", ascending=False)

    years = sorted(df["year"].unique(), reverse=True)

    year_options = "\n".join(
        f'<option value="{year}">{year}</option>'
        for year in years
    )

    thoughts_html = ""

    for _, row in df.iterrows():
        safe_text = html.escape(str(row["text"])).replace("\n", "<br>")
        safe_date = html.escape(str(row["date_label"]))

        thoughts_html += f"""
        <article class="thought-card" data-year="{row['year']}">
            <div class="thought-date">{safe_date}</div>
            <div class="thought-text">{safe_text}</div>
        </article>
        """

    stats = {
        int(year): {
            "entries": int(len(df[df["year"] == year])),
            "words": int(
                df[df["year"] == year]["text"]
                .astype(str)
                .str.split()
                .str.len()
                .sum()
            ),
        }
        for year in years
    }

    page_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Journal Dashboard</title>
        <meta charset="utf-8">

        <style>
            body {{
                margin: 0;
                background: #f7f4ef;
                color: #1f1f1f;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }}

            .page {{
                max-width: 880px;
                margin: 0 auto;
                padding: 56px 28px 80px;
            }}

            .header {{
                margin-bottom: 36px;
            }}

            .eyebrow {{
                color: #8a7f73;
                font-size: 14px;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 10px;
            }}

            h1 {{
                font-size: 52px;
                line-height: 1.05;
                margin: 0;
                letter-spacing: -0.04em;
            }}

            .subtitle {{
                color: #6f665e;
                font-size: 18px;
                margin-top: 14px;
                line-height: 1.5;
            }}

            .controls {{
                display: flex;
                align-items: center;
                gap: 18px;
                background: rgba(255, 255, 255, 0.75);
                border: 1px solid #e5ded4;
                border-radius: 18px;
                padding: 18px;
                margin-bottom: 34px;
            }}

            select {{
                font-size: 18px;
                padding: 10px 14px;
                border-radius: 12px;
                border: 1px solid #d8cec2;
                background: white;
            }}

            .stat {{
                color: #6f665e;
                font-size: 15px;
            }}

            .stat strong {{
                color: #1f1f1f;
            }}

            .thought-card {{
                background: #fffaf3;
                border: 1px solid #eadfce;
                border-radius: 22px;
                padding: 30px 34px;
                margin-bottom: 22px;
                box-shadow: 0 10px 30px rgba(60, 45, 30, 0.05);
            }}

            .thought-date {{
                color: #9a6b3f;
                font-size: 14px;
                font-weight: 700;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                margin-bottom: 16px;
            }}

            .thought-text {{
                font-family: Georgia, "Times New Roman", serif;
                font-size: 22px;
                line-height: 1.75;
                color: #2d2925;
            }}

            .hidden {{
                display: none;
            }}

            @media (max-width: 700px) {{
                h1 {{
                    font-size: 40px;
                }}

                .thought-text {{
                    font-size: 19px;
                }}

                .controls {{
                    flex-direction: column;
                    align-items: flex-start;
                }}
            }}
        </style>
    </head>

    <body>
        <main class="page">
            <section class="header">
                <div class="eyebrow">Life OS</div>
                <h1>Journal Dashboard</h1>
                <div class="subtitle">
                    A readable archive of thoughts, reflections, and patterns over time.
                </div>
            </section>

            <section class="controls">
                <select id="yearSelect">
                    {year_options}
                </select>

                <div class="stat">
                    <strong id="entryCount"></strong> reflections
                </div>

                <div class="stat">
                    <strong id="wordCount"></strong> words
                </div>
            </section>

            <section id="thoughts">
                {thoughts_html}
            </section>
        </main>

        <script>
            const stats = {json.dumps(stats)};

            function updateYear() {{
                const selectedYear = document.getElementById("yearSelect").value;
                const cards = document.querySelectorAll(".thought-card");

                cards.forEach(card => {{
                    card.classList.toggle(
                        "hidden",
                        card.dataset.year !== selectedYear
                    );
                }});

                document.getElementById("entryCount").textContent =
                    stats[selectedYear]["entries"];

                document.getElementById("wordCount").textContent =
                    stats[selectedYear]["words"];
            }}

            document.getElementById("yearSelect").addEventListener("change", updateYear);
            updateYear();
        </script>
    </body>
    </html>
    """

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(page_html, encoding="utf-8")

    print(f"Read: {DATA_PATH}")
    print(f"Wrote: {OUT_PATH}")


if __name__ == "__main__":
    main()
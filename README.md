# Weather Data ETL Pipeline (Scheduled)

## Overview
This project builds a modular, automated ETL pipeline that fetches current weather data from a free API on a daily schedule, cleans it, and appends it to a local SQLite database — building a growing historical weather record over time. It's the fourth project in a broader Data Engineering portfolio, introducing scheduling and incremental (append-based) data loading.

## Data Source
- **API:** [Open-Meteo](https://open-meteo.com/) — free, no API key required
- **Location tracked:** Ranchi, India (configurable via function parameters)
- **Data fetched:** current temperature, relative humidity, and wind speed

## Pipeline Structure
Same modular ETL pattern as Project 3, extended with automation:

- **`step1_extract.py`** — fetches current weather data from the Open-Meteo API
- **`step2_transform.py`** — converts the timestamp to proper datetime and drops an unneeded metadata column
- **`step3_load.py`** — appends the cleaned reading into a SQLite database (rather than replacing existing data, so history builds up over time)
- **`main.py`** — orchestrates the full pipeline in sequence

## Automation
The pipeline is scheduled to run automatically once daily using **Windows Task Scheduler**, calling `main.py` directly with the correct working directory so relative file paths resolve correctly. The task is configured to run as soon as possible if a scheduled run is missed (e.g., if the computer was off).

## What Was Done
- Extracted live weather data via API
- Investigated the raw response structure to identify the relevant nested fields
- Cleaned the data: fixed the datetime type, dropped a non-weather metadata field
- Implemented an **append-based load** (`if_exists='append'`) instead of a replace-based load, to preserve historical readings
- Verified append behavior by running the pipeline multiple times and confirming row count grew rather than staying static
- Automated the pipeline using Windows Task Scheduler
- Encountered and resolved a real scheduling issue: an incorrect working directory caused the scheduled task to fail, since the script relies on a relative database path

## Project Structure
```
de-04-weather-etl/
├── data/
│ └── weather.db # SQLite database (not tracked in Git - grows over time)
├── notebooks/
│ └── exploration.ipynb # Scratch space for initial API exploration
├── src/
│ ├── step1_extract.py # Extract: fetch current weather from API
│ ├── step2_transform.py # Transform: fix data types, drop unneeded columns
│ ├── step3_load.py # Load: append cleaned data into SQLite
│ └── main.py # Orchestrates the full pipeline
├── requirements.txt
└── README.md
```

**Note:** `data/weather.db` is intentionally excluded from version control (see `.gitignore`), since it changes with every scheduled run. In a real production system, code is versioned while accumulating data typically is not — this project follows that same practice.

## Tech Stack
- Python
- Pandas
- Requests (for API calls)
- SQLite
- Windows Task Scheduler

## Key Takeaways
This project introduced two new concepts beyond Project 3: **incremental/append-based loading** (preserving history instead of overwriting it) and **pipeline automation** via task scheduling. It also involved genuine troubleshooting — diagnosing a failed scheduled run caused by an incorrect working directory, and recognizing that frequently-changing data files don't belong in version control the same way code does.

## How to Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline manually: `python src/main.py`
4. To automate: set up a scheduled task (e.g., Windows Task Scheduler) pointing to `main.py`, with the working directory set to the `src/` folder
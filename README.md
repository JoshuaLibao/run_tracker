# Run Tracker Project

## Overview
A Python and SQL-based run tracking project that validates, enriches, and analyzes running data.
This project demonstrates data cleaning, feature engineering, and SQL-based aggregation, providing insights such as pace, run types, and monthly summaries.

## Project Motivation
Being a marathoner, I wanted to create a project that reflects that interest, that being a run tracker. This allowed me to not only practice data processing with python(pandas) and sql but also relate the project to my personal interest.

## Technologies Used
    - Python 3.13.1
    - Pandas
    - SQLite/SQL
    - DB Browser for SQLite

## Data
- **Source:** `run_data_large.csv`  
- **Raw table:** `run_data` (imported into SQLite)  
- **Validated/enriched table:** `runs_clean` (features: pace, run type)  
- **Aggregated summary table:** `monthly_summary` (SQL-based monthly metrics)

## Features
### Data Cleaning & Feature Engineering (Pandas)
- Validate run data (remove zero distance/time)  
- Calculate pace for each run  
- Classify run type: easy, tempo, hard  
- Compute overall metrics: average pace, fastest/slowest pace, total distance, longest run, count of each run type  

### Aggregation & Analysis (SQL)
- Generate **monthly summary**: average pace, fastest/slowest pace, total distance, longest run  
- Group runs by month to provide easy-to-read analytics  
- Persist final tables in SQLite database (`run_tracker.db`)  

## Workflow
1. Import CSV into SQLite → `run_data`  
2. Load SQL table into Pandas DataFrame  
3. Validate and enrich data (Pandas) → `runs_clean`  
4. Export cleaned DataFrame back to SQL  
5. Apply SQL aggregation to generate `monthly_summary`  
6. Export results to database for review in DB Browser 

## How to Run
1. Clone the repository  
2. Open `run_pipeline.py`  
3. Ensure `run_tracker.db` is in `/data/`  
4. Run the Python script to generate cleaned and aggregated tables  
5. View tables in DB Browser or query via SQL  

## Next Steps / Future Work
- Add user input to filter runs by specific months  
- Implement more advanced metrics, e.g., pace trends over time  
- Include visualization (matplotlib / seaborn) for monthly summaries  

## Notes
- **Pandas:** row-level validation, feature calculations (pace, run type, overall metrics)  
- **SQL:** grouping by month, aggregations for monthly summaries, persisted tables  

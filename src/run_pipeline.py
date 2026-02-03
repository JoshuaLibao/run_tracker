import pandas as pd
import sqlite3

path = r'C:\Users\12063\Downloads\sqlite\run_tracker.db'
table_name = 'run_data'

conn = sqlite3.connect(path)
df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
       
# Validation
valid_run = df[(df["distance"] != 0) & (df["time"] != 0)]

# Calculate pace
pace = valid_run["time"] / valid_run["distance"]

# New column for pace
df['pace'] = pace

# New column for run type
cutoff = [0,4,6,10]
labels = ["easy", "tempo", "hard"]
df['run_type'] = pd.cut(df["rpe"], bins=cutoff, labels=labels)

# average, fastest, slowest, total miles, count of each run type, longest run
average = pace.mean()
fastest = pace.min()
slowest = pace.max()
total_miles = df["distance"].sum()
longest_run = df["distance"].max()
number_run_types = df["run_type"].value_counts()

#summary table to display features^^
easy_runs = number_run_types["easy"]
tempo_runs = number_run_types["tempo"]
hard_runs = number_run_types["hard"]
summary_table = pd.DataFrame({"easy":[easy_runs], 
                              "tempo": [tempo_runs], 
                              "hard":[hard_runs],
                              "average pace": [average], 
                              "fastest run":[fastest], 
                              "slowest run": [slowest], 
                              "total miles": [total_miles], 
                              "longest run": [longest_run]}, 
                              index=["results"])
# summary_table dataframe -> sql table
summary_table.to_sql(
    "summary_table",
    conn,
    if_exists="replace",
    index=False
)

# runs_clean dataframe -> sql table
df.to_sql(
    "runs_clean",
    conn,
    if_exists="replace",
    index=False
)
# monthly summary
monthly_summary = pd.read_sql(""" SELECT
    AVG(pace), MAX(pace), MIN(pace), MAX(distance), SUM(distance)
    FROM runs_clean
    WHERE strftime('%m',"date") 
    GROUP BY strftime('%m',"date")
            """,conn)
monthly_summary.rename(index={
    0:'January',
    1:'Feburary',
    2:'March',
    3:'April',
    4:'May',
    5:'June',
    6:'July',
    7:'August',
    8:'September',
    9:'October',
    10:'November',
    11:'December'
    }, columns={
    'AVG(pace)':'Average Pace',
    'MAX(pace)':'Slowest Pace',
    'MIN(pace)':'Fastest Pace',
    'MAX(distance)':'Longest run',
    'SUM(distance)':'Total miles ran'
}, inplace=True)
monthly_summary.index.name = 'Month'
monthly_summary.reset_index(inplace=True)
monthly_summary.to_sql('monthly_summary', conn, if_exists='replace', index=False)

conn.close()


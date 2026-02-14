-- Run Tracker
--========================
-- Monthly summary table
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "monthly_summary" (
"Month" TEXT,
  "Average Pace" REAL,
  "Slowest Pace" REAL,
  "Fastest Pace" REAL,
  "Longest run" REAL,
  "Total miles ran" REAL
);
-- Cleaned data
CREATE TABLE IF NOT EXISTS "runs_clean" (
"date" TEXT,
  "distance" REAL,
  "time" REAL,
  "rpe" INTEGER,
  "pace" REAL,
  "run_type" TEXT
);
COMMIT;

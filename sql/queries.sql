-- ====Monthly Summary Table====
-- This query provides a summary of all the runs for each month
SELECT
    AVG(pace), MAX(pace), MIN(pace), MAX(distance), SUM(distance)
    FROM runs_clean
    WHERE strftime('%m',"date") 
    GROUP BY strftime('%m',"date")

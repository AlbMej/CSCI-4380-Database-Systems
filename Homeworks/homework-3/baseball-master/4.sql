SELECT DISTINCT 
    salaries.yearid AS year, teamsalary.sumSalary AS salary 
FROM 
    salaries 
INNER JOIN (
    SELECT DISTINCT 
        yearid, SUM(salary) AS sumSalary 
    FROM 
        salaries 
    WHERE 
        (yearid, teamid) IN 
        (
        SELECT yearid, teamid FROM teams WHERE teams.wswin = 'Y'
        ) 
    GROUP BY 
        yearid, teamid
    ) teamsalary 
ON salaries.yearid = teamsalary.yearid 
ORDER BY 
    salary DESC;

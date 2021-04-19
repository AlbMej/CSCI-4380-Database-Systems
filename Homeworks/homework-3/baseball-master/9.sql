SELECT 
	yearid AS year, AVG(sumsalary) AS salary
FROM (
	SELECT 
		yearid, teamid, sum(salary) AS sumsalary 
	FROM 
		salaries 
	GROUP BY 
		yearid, teamid) AS FOO
GROUP BY
	yearid 
ORDER BY
	yearid ASC
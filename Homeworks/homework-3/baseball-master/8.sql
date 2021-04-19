SELECT 
	year, sums/average AS ratio 
FROM (
	SELECT DISTINCT 
		salaries.yearid AS year, AVG(salaries.salary) AS sums 
	FROM 
		allstarfull 
	INNER JOIN salaries 
	ON salaries.playerid = allstarfull.playerid 
	AND salaries.yearid = allstarfull.yearid 
	GROUP BY 
		salaries.yearid) AS years
INNER JOIN (
    SELECT 
    	yearid, AVG(salary) AS average 
    FROM 
    	salaries 
    GROUP BY 
    	yearid) AS avgs
ON year = avgs.yearid
GROUP BY year, sums, average;
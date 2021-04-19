
SELECT 
	franchise, AVG(CAST (attendance AS int)) AS attendance 
FROM 
   	teams
INNER JOIN (
    SELECT 
    	franchid, franchname AS franchise
    FROM 
    	teamsfranchises
    ) AS franchises
ON franchises.franchid = teams.franchid 
WHERE 
	yearid >= 1997
GROUP BY 
	franchise
ORDER BY 
	franchise;
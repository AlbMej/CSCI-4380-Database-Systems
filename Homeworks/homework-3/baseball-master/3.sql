SELECT 
	yearid AS years
FROM (
    SELECT 
    	teamid, yearid
    FROM (
        SELECT 
        	teamid, MAX(w) OVER 
        	(PARTITION BY yearid) AS w, yearid
        FROM 
        	managers
        WHERE 
        	yearid >= 1975

        INTERSECT

        SELECT 
        	teamid, w, yearid
        FROM 
        	managers
        ) mostwins 
    INTERSECT
    SELECT 
    	teamid, yearid
    FROM 
    	teams
    WHERE 
    	wswin = 'Y') AS worldseries
ORDER BY 
	yearid;
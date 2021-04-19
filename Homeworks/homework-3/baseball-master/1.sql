SELECT 
	COUNT(DISTINCT playerid) 
FROM 
	pitching 
WHERE 
	playerid 
IN (
    SELECT DISTINCT 
    	playerid 
    FROM 
    	pitching 
    WHERE 
    	yearid >= 1975 
    GROUP BY 
    	playerid, yearid 
    HAVING SUM(pitching.sv) > 40
    );

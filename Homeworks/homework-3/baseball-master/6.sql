SELECT namefirst AS first, namelast AS last, appearances
FROM (
    SELECT 
    	allstarfull.playerid, COUNT(allstarfull.playerid) AS appearances
    FROM 
    	halloffame
    INNER JOIN allstarfull ON 
    	halloffame.playerid = allstarfull.playerid
    WHERE 
    	halloffame.yearid = 2000
    GROUP BY 
    	allstarfull.playerid
    	) allstars
INNER JOIN master ON 
	allstars.playerid = master.playerid
ORDER BY 
	appearances DESC, master.namelast ASC
LIMIT 10;
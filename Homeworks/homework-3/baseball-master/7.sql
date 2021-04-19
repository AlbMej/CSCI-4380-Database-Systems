SELECT DISTINCT 
	batting.playerid, SUM(batting.h)::decimal/SUM(batting.ab) AS career_avg 
FROM 
	batting 
JOIN master
ON 
	batting.playerid = master.playerid 
WHERE
	batting.ab > 0 AND master.birthyear >= 1970 
GROUP BY 
	batting.playerid 
ORDER BY 
	career_avg DESC;
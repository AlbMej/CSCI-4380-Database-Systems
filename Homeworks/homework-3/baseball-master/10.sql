SELECT 
	name_full AS school_name, count 
FROM (
	SELECT 
		schoolid, count(playerid) as count
	FROM (
		SELECT DISTINCT schoolid, allstarfull.playerid
		FROM allstarfull, collegeplaying
		WHERE allstarfull.playerid = collegeplaying.playerid
		) AS allstars
	GROUP BY	
		schoolid) AS schoolids

	NATURAL JOIN (SELECT name_full, schoolid
				FROM schools) AS schoolsnames

	ORDER BY count DESC, school_name ASC
	LIMIT 10;




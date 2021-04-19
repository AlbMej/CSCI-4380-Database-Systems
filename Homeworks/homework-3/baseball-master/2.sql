SELECT 
	COUNT (DISTINCT batting.PlayerID)
FROM
	batting inner join master on (batting.PlayerID = master.PlayerID)
WHERE
	height < 72
    AND yearid = 2016
	AND ab > 0
	AND (1.*h/ab) > 0.3;
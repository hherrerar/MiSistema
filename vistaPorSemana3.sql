CREATE VIEW semana3 AS
SELECT es.name as Estudiante,
d7.rfid, 
d7.event_time as D7, 
d9.event_time as D9, 
d10.event_time as D10
FROM 
	oct07 as d7
FULL JOIN 
	oct9 as d9 ON d7.name = d9.name	
FULL JOIN 
	oct10 as d10 ON d7.name = d10.name	
FULL JOIN
	students as es ON d7.name = es.name
ORDER BY Estudiante

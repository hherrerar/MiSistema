CREATE VIEW semana AS
SELECT d7.name as Estudiante, d7.event_time as D7, d9.event_time as D9
FROM 
	oct07 as d7
FULL OUTER JOIN 
	oct9 as d9 ON d7.rfid = d9.rfid
ORDER BY Estudiante
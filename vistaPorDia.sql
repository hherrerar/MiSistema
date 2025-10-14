CREATE VIEW oct9 AS
SELECT *
FROM 
	students as s
JOIN 
	events as e ON e.rfid = s.mobile
WHERE
	strftime('%Y-%m-%d', e.event_time) ='2025-10-09'
GROUP BY event_time

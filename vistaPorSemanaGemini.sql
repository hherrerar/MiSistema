CREATE VIEW dias_asistencia5 AS
SELECT
    s.name,
    s.mobile, -- Incluye otras columnas de students si son necesarias
    -- Columna para el 7 de octubre
    COUNT(CASE WHEN strftime('%Y-%m-%d', e.event_time) = '2025-10-07' THEN 1 ELSE NULL END) AS eventos_2025_10_07,
    -- Columna para el 8 de octubre
    COUNT(CASE WHEN strftime('%Y-%m-%d', e.event_time) = '2025-10-08' THEN 1 ELSE NULL END) AS eventos_2025_10_08,
    -- Columna para el 9 de octubre
    COUNT(CASE WHEN strftime('%Y-%m-%d', e.event_time) = '2025-10-09' THEN 1 ELSE NULL END) AS eventos_2025_10_09,
	-- Columna para el 9 de octubre
    COUNT(CASE WHEN strftime('%Y-%m-%d', e.event_time) = '2025-10-10' THEN 1 ELSE NULL END) AS eventos_2025_10_10,
	-- Columna para el 9 de octubre
    COUNT(CASE WHEN strftime('%Y-%m-%d', e.event_time) = '2025-10-14' THEN 1 ELSE NULL END) AS eventos_2025_10_14
FROM
    students AS s
JOIN
    events AS e ON e.rfid = s.mobile
-- La cláusula WHERE ahora se usa para filtrar el rango total de datos, no la condición de la columna
WHERE
    strftime('%Y-%m-%d', e.event_time) BETWEEN '2025-10-07' AND '2025-10-14'
GROUP BY
    s.name, s.mobile;
	
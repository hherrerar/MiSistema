SELECT * FROM students AS s
INNER JOIN events AS e
ON S.mobile = e.rfid
ORDER BY name


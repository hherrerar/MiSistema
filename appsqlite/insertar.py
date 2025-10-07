import sqlite3 as sql
from datetime import datetime

def createDB():
    conn = sql.connect("mydatabase.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE events (
            id INTEGER PRIMARY KEY,
            rfid TEXT,
            event_name TEXT,
            event_time TEXT     
        )"""
    )
    conn.commit()
    conn.close()

# --- 1. Definir la función de adaptador ---
def adapt_datetime_iso(val: datetime) -> str:
    """Adapta un objeto datetime.datetime a una cadena de formato ISO 8601."""
    # datetime.isoformat() es la forma estándar de obtener el formato de cadena deseado.
    return val.isoformat()

# --- 2. Registrar el adaptador ---
# Asocia la clase datetime.datetime con la función adapt_datetime_iso.
def registrar():
    sql.register_adapter(datetime, adapt_datetime_iso)


def insertTimeStamp():
    conn = sql.connect("mydatabase.db")
    cursor = conn.cursor()
    now = datetime.now()
    cursor.execute("INSERT INTO events (rfid, event_name, event_time) VALUES (?, ?, ?)", ("1234567890","Aula 204", now))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createDB()
    #createTable()
    registrar()
    insertTimeStamp()
 


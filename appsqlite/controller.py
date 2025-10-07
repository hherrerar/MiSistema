import sqlite3 as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer       
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instuccion = f"INSERT INTO streamers VALUES ('{nombre}',{followers},{subs})"
    cursor.execute(instuccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def insertRows(streamerList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion1 = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion1, streamerList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name='AlexElCapo'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)



if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("ibai", 7000000, 25000)
    #insertRow("AlexElCapo", 8000000, 10000)
    #readRows()
    streamers = [
        ("ElXokas", 1000000, 9500),
        ("Cristinini", 3000000, 5500),
        ("Auronplay", 8000000, 2000)
    ]
    #insertRows(streamers)
    search()

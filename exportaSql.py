import sys
import sqlite3 as sql
import pandas as pd
from datetime import datetime

def conectarDB():
    conn = sql.connect(r"C:\sistemas\database.db")
    conn.commit()
    conn.close()

def consulta():
    conn = sql.connect(r"C:\sistemas\database.db")
    df = pd.read_sql_query('SELECT * FROM dias_asistencia5', conn)
    df.to_excel('asistencia_tabla.xlsx', index=False)
    conn.close()

if __name__ == "__main__":
    #conectarDB()
    #createTable()
    consulta()
    print('compila')

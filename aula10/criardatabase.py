import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ cria uma conexão ao banco de dados SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    
    #Se o banco de dados não existir será criado
    create_connection(r"C:\tools\sqllite\BD\pythonsqlite.db")
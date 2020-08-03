import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ cria uma conexão a uma banco de dados SQLite
        definido por db_file
    :param db_file: path do arquivo do banco de dados
    :return: Objeto Connection ou None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query todas as linhas na tabela tasks
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks por priority
    :param conn: O Objeto Connection 
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    
    #path do banco de dados
    database = r"C:\tools\sqllite\BD\pythonsqlite.db"

    # cria uma conexão a um banco de dados
    conn = create_connection(database)
    with conn:
        print("\n1. Consulta task por priority:")
        select_task_by_priority(conn, 1)

        print("\n2. Consulta todas as tasks")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()
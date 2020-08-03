import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ cria conexão a um banco de dados SQLite 
        definido em db_file
    :param db_file: path do arquivo database 
    :return: Objeto Conexão ou None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def delete_task(conn, id):
    """
    Delete uma task pela task id
    :param conn:  Conexão ao banco de dados SQLite
    :param id: id da task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    """
    Delete todas as linhas da tabela tasks
    :param conn: Conexão ao banco de dados SQLite
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    
    #path do banco de dados
    database = r"C:\tools\sqllite\BD\pythonsqlite.db"

    # cria uma conexão ao banco de dados
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2);
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()
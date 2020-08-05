import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ cria uma conexão a banco de dados SQLite 
        definido em db_file
    :param db_file: caminho para o arquivo database 
    :return: Objeto Connection ou None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_task(conn, task):
    """
    update priority, begin_date, e end date of de uma task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def main():
    
    #path do caminho do arquivo de banco de dados
    database = r"C:\tools\sqllite\BD\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn, (3, '2020-02-04', '2020-02-16', 2))


if __name__ == '__main__':
    main()
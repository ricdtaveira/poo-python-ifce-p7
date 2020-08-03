import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ cria uma conexão para o banco de dados SQLite 
        especificado por db_file
    :param db_file: arquivo banco de dados
    :return: Objeto Conexão ou Conexão Vazia
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ cria uma tabela a partir da sentença create_table_sql statement
    :param conn: Obejeto Conexão 
    :param create_table_sql: uma sentença CREATE TABLE 
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    #path do banco de dados
    database = r"C:\tools\sqllite\BD\pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # cria uma conexão ao um banco de dados
    conn = create_connection(database)

    # crias as tabelas 
    if conn is not None:
        # cria a tabela projetos
        create_table(conn, sql_create_projects_table)

        # cria a tabela tarefas 
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! não pode criar a conexão ao banco de dados.")


if __name__ == '__main__':
    main()
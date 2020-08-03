import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ criar uma conexão a um banco de dados SQLite
        definido em db_file
    :param db_file: nome do banco de dados
    :return: Objeto Conexão ou Vazio
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Inserir um novo projeto na tabela projetos
    :param conn: Conexão
    :param project: 
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    """
    Criar uma nova tarefa
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    
    #path do banco de dados
    database = r"C:\tools\sqllite\BD\pythonsqlite.db"
     
    # criar uma conexão com o banco de dados
    conn = create_connection(database)
    with conn:
        # inserir um novo projeto
        project = ('App com SQLite & Python', '2020-01-01', '2020-01-30');
        project_id = create_project(conn, project)

        # tarefas 
        task_1 = ('Analisar os requisitos da app', 1, 1, project_id, '2020-01-01', '2020-01-02')
        task_2 = ('Confirmar com o usuario os requitos mais importantes', 1, 1, project_id, '2020-01-03', '2015-01-05')

        # inserir as tarefas 
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()
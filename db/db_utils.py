import sqlite3

def connect_to_db(database_name="my_database.db"):
    return sqlite3.connect(database_name)

def create_table(con, create_table_sql):
    cursor = con.cursor()
    cursor.execute(create_table_sql)
    con.commit()

def insert_student(conn, estudantes):
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
    VALUES (?, ?, ?);
    """, estudantes)
    conn.commit()

def show_all_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Estudantes")
    return cursor.fetchall()


def select_students_by_year(con, start_year, end_year):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Estudantes WHERE Ano_de_Ingresso BETWEEN ? AND ?", (start_year, end_year))
    return cursor.fetchall()

def update_student(con, ano, id):
    cursor = con.cursor()
    cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE ID = ?", (ano, id))
    con.commit()

def delete_student(con, id):
    cursor = con.cursor()
    cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (id,))
    con.commit() 

def select_students_by_year_and_course(cursor, year, course):
    cursor.execute("SELECT * FROM Estudantes WHERE Curso = ? AND Ano_de_Ingresso > ?", (course, year))
    return cursor.fetchall()

def close_connection(con):
    con.close()

def drop_table(con, table_name):
    cursor = con.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    con.commit()


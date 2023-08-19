import sqlite3
from db import db_utils

con = db_utils.connect_to_db('db/database_alunos2.db')
db_utils.drop_table(con, 'Estudantes')

create_table_query = '''
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY,
    Nome TEXT,
    Curso TEXT,
    Ano_de_Ingresso INTEGER
)'''

db_utils.create_table(con, create_table_query)

estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]

db_utils.insert_student(con, estudantes)

print('------------------------------')
print('All students')
print(db_utils.show_all_students(con))

print('------------------------------')
print('Students by between years')
print(db_utils.select_students_by_year(con, 2019, 2020))

# UPDATE Estudantes SET Ano_de_Ingresso = 2020 WHERE ID = 2
db_utils.update_student(con, 2020, 2)

#DELETE FROM Estudantes WHERE ID = 4
db_utils.delete_student(con, 4)

print('------------------------------')
print('All students')
print(db_utils.show_all_students(con))

db_utils.close_connection(con)

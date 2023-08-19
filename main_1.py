import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

# Excluindo a tabela se ela já existir
cursor.execute("DROP TABLE IF EXISTS Estudantes")
conn.commit()

# Criando a tabela Estudantes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
);
""")

estudantes = [
    ("Ana Silva", 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

# Inserindo registros
cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
VALUES (?, ?, ?);
""", estudantes)

conn.commit()

# Selecionando todos os estudantes
print(" ")
cursor.execute("SELECT * FROM Estudantes")
print("Todos os Estudantes:")
print(cursor.fetchall())

# Filtrando estudantes que ingressaram entre 2019 e 2020
cursor.execute("SELECT * FROM Estudantes WHERE Ano_de_Ingresso BETWEEN 2019 AND 2020")
print("\nEstudantes que ingressaram entre 2019 e 2020:")
print(cursor.fetchall())

# Atualizando o "Ano de Ingresso" de um estudante específico
cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = 2020 WHERE ID = 4")
conn.commit()

# Deletando um registro
cursor.execute("DELETE FROM Estudantes WHERE ID = 2")
conn.commit()

# Mostrando todos os estudantes após deletar
cursor.execute("SELECT * FROM Estudantes")
print("\nEstudantes após deletar o registro com ID 2:")
print(cursor.fetchall())

# Filtrando os estudantes do Curso de Computação que ingressaram após 2019
cursor.execute("SELECT * FROM Estudantes WHERE Curso = 'Computação' AND Ano_de_Ingresso > 2019")
print("\nEstudantes do Curso de Computação que ingressaram após 2019:")
print(cursor.fetchall())

# Atualizando todos os registros dos alunos de Computação, campo ingresso para 2018
cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = 2018 WHERE Curso = 'Computação'")
conn.commit()

# Mostrando todos os estudantes após atualização
cursor.execute("SELECT * FROM Estudantes")
print("\nEstudantes após atualização do ano de ingresso dos estudantes de Computação:")
print(cursor.fetchall())

conn.close()

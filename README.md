[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/GsJsnvSu)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11573545&assignment_repo_type=AssignmentRepo)
# ProjÁgil - 2023

Material de apoio sobre SQL: https://www.devmedia.com.br/guia/guia-completo-de-sql/38314

### Exercício 1: SQL

Iremos utilizar a plataforma https://sqliteonline.com/ para treinar comandos SQL básicos. O arquivo que usaremos é "vgsales_pbi.csv" que pode ser baixado no link https://drive.google.com/file/d/1fhcUzrJau2w5zcQ1B3wpKhOv9mWet0xR/view?usp=sharing.

1. **Jogos da plataforma Xbox One**:
   - **Enunciado**: Liste todos os jogos disponíveis para a plataforma Xbox One. (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi WHERE platform ="XOne" LIMIT 5;
     ```
   - **Resultado**
    <p>ReCore	XOne	2016,0	Action	Microsoft Game Studios	0,06	0,03	0,0	0,1 <p>
    Tom Clancy's The Division	XOne	2016,0	Shooter	Ubisoft	1,2	0,62	0,0	2,01  <p>
    Valentino Rossi: The Game	XOne	2016,0	Racing	Namco Bandai Games	0,0	0,02	0,0	0,02 <p>
    The Technomancer	XOne	2016,0	Role-Playing	Focus Home Interactive	0,01	0,01	0,0	0,02<p>
    Dead Island Definitive Collection	XOne	2016,0	Action	Deep Silver	0,02	0,02	0,0	0,04<p>
  


2. **Jogos de Ação após 2010**:
   - **Enunciado**: Liste todos os jogos do gênero "Ação" que foram lançados após 2010.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi WHERE genre ="Action" and year > 2010 LIMIT 5;
     ```
   - **Resultado**
   <p>Brothers Conflict: Precious Baby	PSV	2017,0	Action	Idea Factory	0,0	0,0	0,01	0,01<p>
   Lego Star Wars: The Force Awakens	PS4	2016,0	Action	Warner Bros. Interactive Entertainment	0,14	0,32	0,0	0,54<p>
   Gundam Breaker 3	PS4	2016,0	Action	Namco Bandai Games	0,0	0,0	0,09	0,09<p>
   Taiko no Tatsujin: Don Don! Mystery Adventure	3DS	2016,0	Action	Namco Bandai Games	0,0	0,0	0,09	0,09<p>
   ReCore	XOne	2016,0	Action	Microsoft Game Studios	0,06	0,03	0,0	0,1<p>
    


3. **Jogos mais recentes**:
   - **Enunciado**: Liste os 5 jogos mais recentes lançados.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi ORDER BY Year DESC LIMIT 5;
     ```
   - **Resultado**
    <p>Imagine: Makeup Artist	DS	2020,0	Simulation	Ubisoft	0,27	0,0	0,0	0,29<p>
    Phantasy Star Online 2 Episode 4: Deluxe Package	PS4	2017,0	Role-Playing	Sega	0,0	0,0	0,03	0,03<p>
    Brothers Conflict: Precious Baby	PSV	2017,0	Action	Idea Factory	0,0	0,0	0,01	0,01<p>
    Phantasy Star Online 2 Episode 4: Deluxe Package	PSV	2017,0	Role-Playing	Sega	0,0	0,0	0,01	0,01<p>
    Hyakka Hyakurou: Sengoku Ninpoujou	PSV	2016,0	Adventure	D3Publisher	0,0	0,0	0,02	0,02<p>


4. **Jogos mais antigos**:
   - **Enunciado**: Liste os 5 jogos mais antigos.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi ORDER BY Year ASC LIMIT 5;
     ```
   - **Resultado**
    <p>Bridge	2600	1980,0	Misc	Activision	0,25	0,02	0,0	0,27<p>
    Freeway	2600	1980,0	Action	Activision	0,32	0,02	0,0	0,34<p>
    Defender	2600	1980,0	Misc	Atari	0,99	0,05	0,0	1,05<p>
    Kaboom!	2600	1980,0	Misc	Activision	1,07	0,07	0,0	1,15<p>
    Boxing	2600	1980,0	Fighting	Activision	0,72	0,04	0,0	0,77<p>


5. **Jogos de Aventura com mais vendas na América do Norte**:
   - **Enunciado**: Quais são os 3 jogos do gênero "Aventura" com as maiores vendas na América do Norte?  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
     SELECT * FROM vgsales_pbi WHERE genre= "Adventure" ORDER BY NA_Sales DESC LIMIT 3;
     ```
   - **Resultado**
    <p>Super Mario Land 2: 6 Golden Coins	GB	1992,0	Adventure	Nintendo	6,16	2,04	2,69	11,18<p>
    Assassin's Creed	X360	2007,0	Adventure	Ubisoft	3,28	1,65	0,07	5,55<p>
    Zelda II: The Adventure of Link	NES	1987,0	Adventure	Nintendo	2,19	0,5	1,61	4,38<p>
    


	 
6. **Jogos de RPG ou Estratégia lançados após 2005**:
   - **Enunciado**: Liste todos os jogos dos gêneros "RPG" ou "Strategy" lançados após 2005.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi WHERE genre= "Role-Playing" Or genre="Strategy"and year > 2005;
     ```
   - **Resultado**
    <p>Phantasy Star Online 2 Episode 4: Deluxe Package	PS4	2017,0	Role-Playing	Sega	0,0	0,0	0,03	0,03<p>
    Phantasy Star Online 2 Episode 4: Deluxe Package	PSV	2017,0	Role-Playing	Sega	0,0	0,0	0,01	0,015<p>
    Persona 5	PS3	2016,0	Role-Playing	Unknown	0,0	0,0	0,1	0,1<p>
    Caligula	PSV	2016,0	Role-Playing	FuRyu	0,0	0,0	0,05	0,05<p>
    The Technomancer	XOne	2016,0	Role-Playing	Focus Home Interactive	0,01	0,01	0,0	0,02<p>



### Exercício 2: Python - Sqlite

Objetivo: Familiarizar-se com os comandos básicos de SQL e aprender a filtrar registros usando o comando WHERE.

Crie uma tabela chamada "Estudantes" com os seguintes campos:

- **ID (chave primária)**
- **Nome**
- **Curso**
- **Ano de Ingresso**

Insira 5 registros de estudantes na tabela. Inclua os seguintes estudantes fictícios como parte desses registros:

- Ana Silva, Computação, Ano de Ingresso: 2019
- Pedro Mendes, Física, Ano de Ingresso: 2021
- Carla Souza, Computação, Ano de Ingresso: 2020
- João Alves, Matemática, Ano de Ingresso: 2018
- Maria Oliveira, Química, Ano de Ingresso: 2022
 
**Selecione e mostre todos os registros da tabela no console.**

- Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive) e exiba no console. Use o comando WHERE para realizar essa filtragem.

- Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.

- Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.

- Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.

- Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. Mostre por todos estudantes novamente.




### Exercicio 3: Python - SQLite

**Exercício de Reaproveitamento e Organização de Código**

A medida que os sistemas crescem e se tornam mais complexos, a necessidade de manter o código organizado e reutilizável torna-se cada vez mais evidente. Manter funções comuns em módulos separados não apenas torna seu código mais legível, mas também permite que você reutilize funções sem duplicar o código. Isso reduz o risco de erros, facilita a manutenção e economiza tempo no longo prazo.

Considere o arquivo `main_1.py` que vocês trabalharam anteriormente. Nele, várias operações relacionadas ao banco de dados foram realizadas. Estas operações são comuns em muitas aplicações e podem ser reutilizadas em diversos contextos.

**Tarefa:** 

1. Crie um arquivo chamado `db_utils.py` dentro da pasta `db`.
2. Crie funções mais comuns relacionadas ao banco de dados para este novo arquivo. Por exemplo, funções para criar tabelas, inserir registros, consultar registros, atualizar e deletar.
3. No `main_2.py`, importe e utilize as funções do arquivo `db_utils.py` para realizar as operações do Exercício 2.

**Dica:** Ao organizar seu código desta maneira, você estará aplicando o princípio DRY (Don't Repeat Yourself) do desenvolvimento de software, que visa reduzir a repetição de informações de todos os tipos.
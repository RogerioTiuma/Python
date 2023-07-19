import sqlite3

#Conectar ao banco de dados SQLite
conn = sqlite3.connect('almoxarifado.db')
cursor = conn.cursor()

# Executar o script SQL
sql_script = """
CREATE TABLE Funcionario (
id INTEGER PRIMARY KEY,
nome TEXT,
cargo TEXT,
departamento TEXT
);

CREATE TABLE Supervisor (
id INTEGER PRIMARY KEY,
nome TEXT,
cargo TEXT,
departamento TEXT
);

CREATE TABLE Almoxarifado (
id INTEGER PRIMARY KEY,
nome TEXT,
localizacao TEXT
);

CREATE TABLE RetiradaMaterial (
id INTEGER PRIMARY KEY,
id_funcionario INTEGER,
id_supervisor INTEGER,
id_almoxarifado INTEGER,
data_retirada TEXT,
quantidade INTEGER,
FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id),
FOREIGN KEY (id_supervisor) REFERENCES Supervisor(id),
FOREIGN KEY (id_almoxarifado) REFERENCES Almoxarifado(id)
);

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (1, 'João Silva', 'Assistente de Almoxarifado', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (2, 'Maria Souza', 'Auxiliar de Estoque', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (3, 'Pedro Santos', 'Técnico de Suprimentos', 'Suprimentos');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (4, 'Mariana Rodrigues', 'Assistente de Almoxarifado', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (5, 'Lucas Oliveira', 'Auxiliar de Estoque', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (6, 'Juliana Lima', 'Técnica de Suprimentos', 'Suprimentos');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (7, 'Ricardo Almeida', 'Assistente de Almoxarifado', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (8, 'Carla Santos', 'Auxiliar de Estoque', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (9, 'Gustavo Costa', 'Técnico de Suprimentos', 'Suprimentos');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (10, 'Ana Silva', 'Assistente de Almoxarifado', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (11, 'Carlos Mendes', 'Auxiliar de Estoque', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (12, 'Fernanda Sousa', 'Técnica de Suprimentos', 'Suprimentos');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (13, 'Bruno Castro', 'Assistente de Almoxarifado', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (14, 'Laura Lima', 'Auxiliar de Estoque', 'Logística');

INSERT INTO Funcionario (id, nome, cargo, departamento)
VALUES (15, 'Rafaela Ferreira', 'Técnica de Suprimentos', 'Suprimentos');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (1, 'Roberto Ferreira', 'Supervisor de Almoxarifado', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (2, 'Ana Oliveira', 'Supervisora de Estoque', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (3, 'Carlos Pereira', 'Supervisor de Suprimentos', 'Suprimentos');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (4, 'Mariana Silva', 'Supervisora de Almoxarifado', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (5, 'Lucas Rodrigues', 'Supervisor de Estoque', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (6, 'Juliana Oliveira', 'Supervisora de Suprimentos', 'Suprimentos');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (7, 'Ricardo Santos', 'Supervisor de Almoxarifado', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (8, 'Carla Mendes', 'Supervisora de Estoque', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (9, 'Gustavo Sousa', 'Supervisor de Suprimentos', 'Suprimentos');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (10, 'Ana Castro', 'Supervisora de Almoxarifado', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (11, 'Carlos Lima', 'Supervisor de Estoque', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (12, 'Fernanda Almeida', 'Supervisora de Suprimentos', 'Suprimentos');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (13, 'Bruno Santos', 'Supervisor de Almoxarifado', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (14, 'Laura Mendes', 'Supervisora de Estoque', 'Logística');

INSERT INTO Supervisor (id, nome, cargo, departamento)
VALUES (15, 'Rafaela Sousa', 'Supervisora de Suprimentos', 'Suprimentos');

INSERT INTO Almoxarifado (id, nome, localizacao)
VALUES (1, 'Almoxarifado Central', 'Prédio A, Sala 101');

INSERT INTO Almoxarifado (id, nome, localizacao)
VALUES (2, 'Almoxarifado Regional', 'Prédio B, Sala 202');

INSERT INTO Almoxarifado (id, nome, localizacao)
VALUES (3, 'Almoxarifado Matriz', 'Prédio C, Sala 303');

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (1, 1, 1, 1, '2023-06-18', 10);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (2, 2, 2, 2, '2023-05-17', 5);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (3, 3, 3, 3, '2023-03-16', 8);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (4, 4, 4, 1, '2023-07-15', 12);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (5, 5, 5, 2, '2023-05-14', 6);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (6, 6, 6, 3, '2023-05-13', 9);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (7, 7, 7, 1, '2023-05-12', 15);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (8, 8, 8, 2, '2023-05-11', 7);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (9, 9, 9, 3, '2023-06-10', 10);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (10, 10, 10, 1, '2023-05-09', 13);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (11, 11, 11, 2, '2023-04-08', 8);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (12, 12, 12, 3, '2023-05-07', 11);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (13, 13, 13, 1, '2023-05-06', 14);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (14, 14, 14, 2, '2023-05-05', 9);

INSERT INTO RetiradaMaterial (id, id_funcionario, id_supervisor, id_almoxarifado, data_retirada, quantidade)
VALUES (15, 15, 15, 3, '2023-05-04', 12);
"""

# Dividir o script em comandos separados
sql_commands = sql_script.split(";")

# Executar cada comando SQL
for command in sql_commands:
    if command.strip() != "":
        cursor.execute(command)

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()

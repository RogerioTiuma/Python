import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('almoxarifado.db')
cursor = conn.cursor()

# Consulta utilizando INNER JOIN
query2 = """
SELECT R.id, F.nome AS funcionario, S.nome AS supervisor, A.nome AS almoxarifado, R.data_retirada, R.quantidade
FROM RetiradaMaterial R
INNER JOIN Funcionario F ON R.id_funcionario = F.id
INNER JOIN Supervisor S ON R.id_supervisor = S.id
INNER JOIN Almoxarifado A ON R.id_almoxarifado = A.id
WHERE R.data_retirada >= '2023-05-01' AND R.data_retirada <= '2023-05-31'
"""

# Executar a consulta
cursor.execute(query2)

# Obter os resultados da consulta
results = cursor.fetchall()

# Criar um DataFrame a partir dos resultados
df = pd.DataFrame(results, columns=['id', 'funcionario', 'supervisor', 'almoxarifado', 'data_retirada', 'quantidade'])

# Gerar o arquivo CSV
df.to_csv('resultado2.csv', index=False)

# Fechar a conexão
conn.close()

# Ler o arquivo CSV usando o pandas
df_csv = pd.DataFrame(pd.read_csv('resultado2.csv'))

# Exibir o DataFrame lido
print(df_csv)

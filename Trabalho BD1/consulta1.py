import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('almoxarifado.db')
cursor = conn.cursor()

# Consulta utilizando LEFT JOIN 
query = """
SELECT R.id, F.nome AS funcionario, S.nome AS supervisor, A.nome AS almoxarifado, R.data_retirada, R.quantidade
FROM RetiradaMaterial R
INNER JOIN Funcionario F ON R.id_funcionario = F.id
LEFT JOIN Supervisor S ON R.id_supervisor = S.id
INNER JOIN Almoxarifado A ON R.id_almoxarifado = A.id
"""

# Executar a consulta
cursor.execute(query)

# Obter os resultados da consulta
results = cursor.fetchall()

# Criar um DataFrame a partir dos resultados
df = pd.DataFrame(results, columns=['id', 'funcionario', 'supervisor', 'almoxarifado', 'data_retirada', 'quantidade'])

# Gerar o arquivo CSV
df.to_csv('resultado1.csv', index=False)

# Fechar a conexão
conn.close()

# Ler o arquivo CSV usando o pandas
df_csv = pd.DataFrame(pd.read_csv('resultado1.csv'))

# Exibir o DataFrame lido
print(df_csv)

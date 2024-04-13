import psycopg2

# Estabelecimento de uma conexão com o banco de dados
conn = psycopg2.connect(
    dbname="atividade_db",
    user="postgres",
    password="postgres",
    host="172.18.0.2",
    port="5432"
)

# Criação um cursor para executar consultas
cur = conn.cursor()

# Execução de um comando SQL
cur.execute("SELECT * FROM atividade")

# Recuperação dos resultados, se houver
rows = cur.fetchall()
for row in rows:
    print(row)

# Fechamento do cursor e da conexão
cur.close()
conn.close()

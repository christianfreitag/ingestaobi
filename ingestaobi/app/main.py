import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError
import time
# Conexão com banco
POSTGRES_USER = 'postgres'
POSTGRES_PW = 'chrisRenLem987*'
POSTGRES_DB = 'lojinha'
POSTGRES_HOST = 'db'
POSTGRES_PORT = '5432'

# Cria a conexão
def create_conn():
    conn = None
    while not conn:
        try:
            conn = psycopg2.connect(
                dbname=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PW,
                host=POSTGRES_HOST,
                port=POSTGRES_PORT
            )
            print("Connection to DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred. Connection to DB failed. Retrying in 5 seconds")
            time.sleep(5)
    return conn

conn = create_conn()

# Ler dados da planilha
df = pd.read_excel('data/Dataset.xlsx')

# Renomear colunas
df = df.rename(columns={
    'ID-Produto': 'id_produto',
    'Produto': 'produto',
    'Categoria': 'categoria',
    'Segmento': 'segmento',
    'Fabricante': 'fabricante',
    'Loja': 'loja',
    'Cidade': 'cidade',
    'Estado': 'estado',
    'Vendedor': 'vendedor',
    'ID-Vendedor': 'id_vendedor',
    'Data Venda': 'data_venda',
    'ValorVenda': 'valor_venda'
})

# Alterar formatação das datas
df['data_venda'] = pd.to_datetime(df['data_venda'], format='%Y-%m-%d')

# Alterar valor venda para float e removendo decorações
df['valor_venda'] = df['valor_venda'].replace('R$', '').replace(',', '.').astype(float)

# Mostra dados
print(df.head())

# Salva no banco de dados
cursor = conn.cursor()
columns = [sql.Identifier(col) for col in df.columns]
values = sql.SQL(',').join(map(sql.Literal, [tuple(x) for x in df.values]))

insert = sql.SQL('INSERT INTO Vendas.CompraProduto ({}) VALUES {}').format(
    sql.SQL(', ').join(columns), values
)
cursor.execute(insert)
conn.commit()
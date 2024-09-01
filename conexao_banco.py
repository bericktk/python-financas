import mysql.connector
from mysql.connector import Error
from datetime import datetime
import pandas as pd
import yfinance as yf

conexao = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'cotacoes',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

def conectar():
    try:
        conn = mysql.connector.connect(**conexao)
        cursor = conn.cursor()
        print('Conexão bem sucedida!')
        return conn, cursor
    except mysql.connector.Error as e:
        print(f'Não foi possível conectar ao banco de dados: {e}')
        return None, None

def inserirDados(conn, cursor, data):
    conn, cursor = conectar()
    if conn is None or cursor is None:
        return
    try:
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        data_convertida = [tuple(x) for x in data[['Date', 'Ativo', 'Aberto', 'Alta', 'Baixa', 'Fechamento', 'Fechamento Ajustado', 'Volume']].values]

        inserir_dados = """INSERT INTO dados_acoes (Date, Ativo, Aberto, Alta, Baixa, Fechamento, Fechamento_Ajustado, Volume) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE
        Ativo = VALUES(Ativo),
        Aberto = VALUES(Aberto), 
        ALTA = VALUES(ALTA), 
        Baixa = VALUES(Baixa), 
        Fechamento = VALUES(Fechamento), 
        Fechamento_Ajustado = VALUES(Fechamento_Ajustado), 
        Volume = VALUES(Volume);
        """
        cursor.executemany(inserir_dados, data_convertida)
        conn.commit()
        print('Dados inseridos com sucesso!')

    except mysql.connector.Error as e:
        print(f'Erro ao inserir os dados: {e}')
        conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


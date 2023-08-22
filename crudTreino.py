import sqlite3 
from pathlib import Path
ROOT_DIR   = Path(__file__).parent
BD_NAME    = '.bd.alunos'
BD_FILE    = ROOT_DIR/BD_NAME 
TABLE_NAME = 'tb_alunos'
conexao = sqlite3.connect(BD_FILE)
cursor = conexao.cursor()

cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
               '('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT NOT NULL,'
               'idade INTEGER NOT NULL,'
               'peso REAL NOT NULL'
               ')'
               )


cursor.close()
conexao.close()
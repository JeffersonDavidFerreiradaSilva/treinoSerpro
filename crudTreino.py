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
conexao.commit()
def criarAluno(conexao,nome,idade,peso):
    novoAluno = conexao.execute("INSERT INTO tb_alunos (nome,idade,peso) VALUES (?,?,?)",(nome,idade,peso))
    conexao.commit()
    print("Aluno cadastrado com sucesso!")
def listarAluno(conexao):
    Alunos = conexao.execute("SELECT * FROM tb_alunos")
    print ("Listagem realizada com sucesso!") 
def atualizarAlunos(conexao,id,nome,idade,peso):
    atualizando = conexao.execute("UPDATE tb_alunos SET nome = ?, idade = ?, peso = ? WHERE id = ?", (nome,idade,peso,id))
    print("Aluno atualizado com Sucesso!")
    conexao.commit()
def deletarAluno(conexao,id):
    deletar = conexao.execute("DELETE FROM tb_alunos WHERE id = ?",(id,))
    conexao.commit()
    print("Aluno deletado com sucesso!")
# criarAluno("Nayana Roberta da Silva Pereira",24, 75.5)
# listarAluno()
#atualizarAlunos(4,"JOSE ROBERTO DA SILVA PEREIRA", 20, 52)
deletarAluno(3)
cursor.close()
conexao.close()
from database.db import Database
from views.livro_view import LivroView
class LivroContoller:
    def __init__(self, db_config):
        self.db = Database(
            db_config["dbname"],
            db_config["user"],
            db_config["password"],
            db_config["host"],
            db_config["port"]
        )
        self.criar_tabela_se_nao_existir()
        self.view = LivroView()
    
    def criar_tabela_se_nao_existir(self):
        conn = self.db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                        CRIETE TABLE IF NOT EXISTS livros(
                        id SERIAL PRIMARY KEY,
                        titulo VARCHAR(300) NOT NULL,
                        autor VARCHAR(90) NOT NULL,
                        ano INTEGER,
                        isbn VARCHAR(13)
                        );

                        """)
            
    def adicionar_livros(self, id, titulo, autor, ano, isbn):
        conn = self.db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute
import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

def criar_database_se_nao_existir(self):
    try:
        conn = psycopg2.connect(
            dbaname=self.dbname,
            user = self.user,
            passeword = self.password,
            host = self.host,
            port = self.port   
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_datdabase WHERE datname = %5", (self.dbname,))
        exists = cur.fetchone()
        if not exists:
            cur.execute(sql.SQL("CRIETE DATABASE {}"). format(sql.Identifier(self.dbname)))
            cur.close()
            conn.close
        
    except Exception as e:
        print(f"erro ao criar o banco de dados: {e}") 
        
def connect(self):
    self.criar_database_se_nao_existir()
    try:
        conn = psycopg2.connect(
            db = self.dbname,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
            
        )
        
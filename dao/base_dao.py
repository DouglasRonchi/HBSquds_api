import MySQLdb

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(
            host="mysql.topskills.study", 
            database="topskills14", 
            user="topskills14", 
            passwd="Dauana2019" )
        self.cursor = self.conexao.cursor()

    def inserir(self, comando_sql_insert):
        self.cursor.execute(comando_sql_insert)
        self.conexao.commit()
        id_gerado = self.cursor.lastrowid
        return id_gerado


    def deletar(self, comando_sql_delete):
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()
        return 'Deletado'
    
    def listar(self, comando_sql_listar):
        self.cursor.execute(comando_sql_listar)
        return self.cursor.fetchall()

    def buscar_por_id(self, comando_sql_buscar_id):
        self.cursor.execute(comando_sql_buscar_id)
        return self.cursor.fetchone()
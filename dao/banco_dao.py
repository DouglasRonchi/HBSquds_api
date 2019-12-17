from dao.base_dao import BaseDao
from model.bd import BD


class BancoDao(BaseDao):

    def inserir(self, bd:BD):
        comando_sql_insert = f"INSERT INTO banco VALUES(DEFAULT, '{bd.nome}')"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM banco WHERE id = {id}"
        return super().deletar(comando_sql_delete)

    def listar(self, id=None):
        lista_squad = []
        comando_sql_listar = """SELECT nome, id FROM banco"""

        l = super().listar(comando_sql_listar)
        squad = BD(l[0], l[1])
        lista_squad.append(squad.__dict__)
        return lista_squad

    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"""SELECT 
                                nome, 
                                id 
                                FROM banco
                                WHERE id = {id}"""

        l = super().buscar_por_id(comando_sql_buscar_id)
        squad = BD(l[0], l[1])   
        return squad

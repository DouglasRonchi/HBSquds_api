from dao.base_dao import BaseDao
from model.linguagem import Linguagem


class LingDao(BaseDao):

    def inserir(self, ling:Linguagem):
        comando_sql_insert = f"INSERT INTO linguagens VALUES(DEFAULT, '{ling.nome}')"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM linguagens WHERE id = {id}"
        return super().deletar(comando_sql_delete)

    def listar(self, id=None):
        lista_squad = []
        comando_sql_listar = """SELECT nome, id FROM linguagens"""

        lista_ling = super().listar(comando_sql_listar)
        for l in lista_ling:
            squad = Linguagem(l[0], l[1])
            lista_squad.append(squad.__dict__)
        return lista_squad

    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"""SELECT 
                                nome, 
                                id 
                                FROM linguagens
                                WHERE id = {id}"""

        l = super().buscar_por_id(comando_sql_buscar_id)
        squad = Linguagem(l[0], l[1])
        return squad

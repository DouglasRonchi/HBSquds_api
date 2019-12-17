from dao.base_dao import BaseDao
from model.framework import Framework


class FrameDao(BaseDao):

    def inserir(self, frame:Framework):
        comando_sql_insert = f"INSERT INTO framework VALUES(DEFAULT, '{frame.nome}')"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM framework WHERE id = {id}"
        return super().deletar(comando_sql_delete)

    def listar(self, id=None):
        lista_frames = []
        comando_sql_listar = "SELECT nome, id FROM framework"
        for l in super().listar(comando_sql_listar):
            squad = Framework(l[1], l[0]).__dict__
            lista_frames.append(squad)
        return lista_frames

    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"""SELECT 
                                nome, 
                                id 
                                FROM framework
                                WHERE id = {id}"""

        l = super().buscar_por_id(comando_sql_buscar_id)
        squad = Framework(l[0], l[1])  
        return squad

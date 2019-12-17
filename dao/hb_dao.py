from dao.base_dao import BaseDao
from model.hbsquads import HB
from model.bd import BD
from model.framework import Framework
from model.linguagem import Linguagem


class HBSquads(BaseDao):

    def inserir(self, hb:HB):
        comando_sql_insert = f"INSERT INTO squads VALUES(DEFAULT, '{hb.nome}', {hb.bd.id}, {hb.framework.id}, {hb.linguagem.id})"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM squads WHERE id = {id}"
        return super().deletar(comando_sql_delete)

    def listar(self, id=None):
        lista_squad = []
        comando_sql_listar = """SELECT 
                                s.nome, 
                                bd.nome,
                                bd.id, 
                                f.nome,
                                f.id, 
                                l.nome,
                                l.id, 
                                s.id 
                                FROM squads as s 
                                JOIN banco as bd
                                ON s.fk_bd = bd.id 
                                JOIN framework as f 
                                ON s.fk_framework = f.id 
                                JOIN linguagens as l 
                                ON s.fk_linguagem = l.id"""

        tupla_cads = super().listar(comando_sql_listar)
        for l in tupla_cads:
            bd = BD(l[1],l[2])
            frame = Framework(l[3],l[4])
            ling = Linguagem(l[5],l[6])
            squad = HB(l[0], bd.__dict__, frame.__dict__, ling.__dict__, l[4])
            lista_squad.append(squad.__dict__)
        return lista_squad

    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"""SELECT 
                                s.nome, 
                                bd.nome,
                                bd.id, 
                                f.nome,
                                f.id, 
                                l.nome,
                                l.id, 
                                s.id 
                                FROM squads as s 
                                JOIN banco as bd
                                ON s.fk_bd = bd.id 
                                JOIN framework as f 
                                ON s.fk_framework = f.id 
                                JOIN linguagens as l 
                                ON s.fk_linguagem = l.id
                                WHERE s.id = {id}"""

        l = super().buscar_por_id(comando_sql_buscar_id)
        bd = BD(l[1],l[2])
        frame = Framework(l[3],l[4])
        ling = Linguagem(l[5],l[6])
        squad = HB(l[0], bd.__dict__, frame.__dict__, ling.__dict__, l[7])   
        return squad.__dict__


        
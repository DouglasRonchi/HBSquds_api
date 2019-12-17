from dao.hb_dao import HBSquads
from dao.framework_dao import FrameDao
from dao.linguagem_dao import LingDao
from dao.banco_dao import BancoDao
from model.hbsquads import HB
from flask_restful import Resource
from flask import request

class HbControllers(Resource):
    def __init__(self):
        self.dao_hb = HBSquads()
        self.dao_frame = FrameDao()
        self.dao_bd = BancoDao()
        self.dao_ling = LingDao()

    def get(self, id=None):
        if (id):
            return self.dao_hb.buscar_por_id(id)
        else:
            return self.dao_hb.listar()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        bd = _json['fk_bd']
        framework = _json['fk_framework']
        linguagem = _json['fk_linguagem']
        nome_frame = self.dao_frame.buscar_por_id(framework)
        nome_ling = self.dao_ling.buscar_por_id(linguagem)
        nome_bd = self.dao_bd.buscar_por_id(bd)
        squad = HB(nome, nome_bd, nome_frame, nome_ling)

        if nome == 'Nicole' and (nome_frame.nome == 'react') and (nome_ling.nome == 'php') and (nome_bd.nome == 'mysqlserver'):
            id_post = self.dao_hb.inserir(squad)
            return self.dao_hb.buscar_por_id(id_post)
        elif nome == 'Nicole':
            return f'{nome} não possui estes conhecimentos!'

        if nome == 'Mateus' and (nome_frame.nome == 'angular') and (nome_ling.nome == 'python') and (nome_bd.nome == 'mongo'):
            id_post = self.dao_hb.inserir(squad)
            return self.dao_hb.buscar_por_id(id_post)
        elif nome == 'Mateus':
            return f'{nome} não possui estes conhecimentos!'

        if nome == 'Tiago' and (nome_frame.nome == 'vue') and (nome_ling.nome == 'java') and (nome_bd.nome == 'postgresql'):
            id_post = self.dao_hb.inserir(squad)
            return self.dao_hb.buscar_por_id(id_post)
        elif nome == 'Tiago':
            return f'{nome} não possui estes conhecimentos!'

        # id_post = self.dao_hb.inserir(squad)
        # return self.dao_hb.buscar_por_id(id_post)


    def delete(self, id):
        self.dao_hb.deletar(id)
        return 'Deletado!!!'
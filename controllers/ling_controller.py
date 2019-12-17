from dao.linguagem_dao import LingDao
from model.linguagem import Linguagem
from flask_restful import Resource
from flask import request

class LingControllers(Resource):
    def __init__(self):
        self.dao_ling = LingDao()

    def get(self):
        if id:
            return self.dao_ling.listar(id)
        else:
            return self.dao_ling.listar()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        ling = Linguagem(nome)
        id_post = self.dao_ling.inserir(ling)
        return self.dao_ling.buscar_por_id(id_post)

    def delete(self, id):
        self.dao_ling.deletar(id)
        return 'Deletado!!!'
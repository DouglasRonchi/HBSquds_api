from dao.hb_dao import HBSquads
from model.bd import BD
from flask_restful import Resource
from flask import request

class BancoControllers(Resource):
    def __init__(self):
        self.dao_bd = BancoDao()

    def get(self):
        if id:
            return self.dao_bd.listar(id)
        else:
            return self.dao_bd.listar()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        banco = BD(nome)
        id_post = self.dao_bd.inserir(banco)
        return self.dao_bd.buscar_por_id(id_post)

    def delete(self, id):
        self.dao_bd.deletar(id)
        return 'Deletado!!!'
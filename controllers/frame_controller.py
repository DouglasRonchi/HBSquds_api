from dao.framework_dao import FrameDao
from model.framework import Framework
from flask_restful import Resource
from flask import request

class FrameControllers(Resource):
    def __init__(self):
        self.dao_frame = FrameDao()

    def get(self, id=None):
        if (id):
            return self.dao_frame.buscar_por_id(id)
        else:
            return self.dao_frame.listar()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        frame = Framework(nome)
        id_post = self.dao_frame.inserir(frame)
        return f'Framework (id:{id_post}) adicionado com sucesso'

    def delete(self, id):
        self.dao_frame.deletar(id)
        return 'Deletado!!!'
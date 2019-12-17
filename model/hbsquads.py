from model.bd import BD
from model.framework import Framework
from model.linguagem import Linguagem

class HB:
    def __init__(self, nome, tipo_db:BD, tipo_framework:Framework, tipo_linguagem:Linguagem, id=None):
        self.nome = nome
        self.bd = tipo_db
        self.framework = tipo_framework
        self.linguagem = tipo_linguagem
        self.id = id

    

class Verificacao:
    def __init__(self, pessoa, lista):
        self.pessoa = pessoa
        self.lista = lista

    def regras(self):
        
        if self.pessoa == '1':
            nicole_lista = ['mysqlserver', 'react' , 'php']
            if nicole_lista == self.lista:
                print('Resultado: \033[32m\nVALIDO\033[m')
            else:
                print('\nResultado: \033[31mValor Inválido!\033[m')
        
        if self.pessoa == '2':
            mateus_lista = ['mongo', 'angular', 'python']
            if mateus_lista == self.lista:
                print('Resultado: \033[32m\nVALIDO\033[m')
            else:
                print('\nResultado: \033[31mValor Inválido!\033[m')
        
        if self.pessoa == '3':
            tiago_lista = ['postgresql', 'vue', 'java']
            if tiago_lista == self.lista:
                print('Resultado: \033[32m\nVALIDO\033[m')
            else:
                print('\nResultado: \033[31mValor Inválido!\033[m')






from dao.verificacao_dao import Verificacao

# nicole_lista = ['mysqlserver', 'react', 'php']
# mateus_lista = ['mongo', 'angular', 'python']
# tiago_lista = ['postgresql', 'vue', 'java']

registrados = [] 
i = 1
while i <=3:
    lista = []
    print('''
        \033[34m------------
        Nicole = [1]
        Mateus = [2]
        Tiago  = [3]
        ------------\033[m\n''')


    resposta = input('Escolha uma opção: ')

    if resposta not in registrados:
        registrados.append(resposta)
    
        print('\033[32m------------------------\033[m\n')
        if resposta == '1' or resposta == '2' or resposta == '3':
            
            print('\033[33mOpções de banco: mysqlserver, mongo, postgresql\033[m')
            banco = input('Digite um banco de dados: ').lower().strip()
            lista.append(banco)
            print('\033[32m------------------------\033[m\n')

            print('\033[33mOpções de framework: vue, angular, react\033[m')
            framework = input('Digite um framework: ').lower().strip()
            lista.append(framework)
            print('\033[32m------------------------\033[m\n')

            print('\033[33mOpções de linguagens: java, python, php\033[m')
            linguagem = input('Digite uma linguagem: ').lower().strip()
            lista.append(linguagem)

                    
            funcionario = Verificacao(resposta, lista)
            funcionario.regras()
            i+=1
                
            print(lista)
        else:
            print('\033[31mResposta Incorreta!\033[m')
            i+=0
    else:
        print('\033[31mEste usuário já está registrado\033[m')


print('Programa encerrado!')     

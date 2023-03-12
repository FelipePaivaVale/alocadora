# cadastrar, consultar disponibilidade (alugado ou disponivel), listar veiculos,
# listar veiculos por modelo, listar veiculos por ano
from locadora import *


app.cadastro_auto("fiat", "uno", 2019, "abc123", 0, 30)
app.cadastro_auto("fiat", "pulse", 2018, "anc343", 0, 30)
app.cadastro_auto("bmw", "x6", 2010, "akr250", 0, 30)
app.cadastro_auto("bmw", "x5", 2014, "kbm345", 0, 30)
app.cadastro_auto("renault", "duster", 2018, "kbm345", 0, 30)
app.cadastro_auto("renault", "logan", 2011, "kbm77", 0, 30)
app.cadastro_usuario_auto('pedro')
app.cadastro_usuario_auto('juse')

def mostrar():
    for carros in lista_carros:
        print(carros)

print('Bem-Vindo ao app de carros Lucas Samuel e Felipe\n')

def mensagem(msg):
    print('-' * 70)
    print(msg)

while (True):
    mensagem('1- Cadastrar Veículo')
    mensagem('2- Consultar disponibilidade dos Veículos')
    mensagem('3- Alugar carro')
    mensagem('4- Devolver carro')
    mensagem('5- Listar veículos por marca')
    mensagem('6- Listar veículos por modelo')
    mensagem('7- Listar veículos por ano')
    mensagem('8- Cadastrar cliente')
    mensagem('9- Exibir clientes')
    print('-' * 70)
    operação = int(input('Informe a operação que deseja realizar: '))

    if (operação == 1):
        app.cadastrar()
        input()

    elif (operação == 2):
        app.mostrar_carros()
        input() 
    
    elif(operação == 3):
        app.alugar_carro()
        input()

    elif(operação == 4):
        app.devolver_carro()
        input()
    
    elif (operação == 5):
        print('1-Fiat\n2-Bmw\n3-Renault')
        escolha = int(input("qual marca deseja procurar? \n"))

        if (escolha == 1):
            marca = 'fiat'
        elif (escolha == 2):
            marca = 'bmw'
        elif (escolha == 3):
            marca = 'renault'
        app.listar_marca(marca)

        input()

    elif (operação == 6):
        print('1- Ver modelos da fiat: \n2- Ver modelos da Bmw: \n 3- Ver modelos da renault')
        escolha = int(input('Deseja ver os modelos de qual marca?'))

        if (escolha == 1):
            print('')
            modelo = 'fiat'
        elif (escolha == 2):
            print('')
            modelo = 'xesque'
        elif (escolha == 3):
            print('')
            modelo = ''
            
        app.listar_modelo(modelo)
        input()

    elif(operação == 7):
        ano = int(input("de qual ano deseja ver os carros"))
        app.listar_ano(ano)
        input()

    elif(operação == 8):
        app.cadastrar_cliente()
        input()
    
    elif(operação == 9):
        app.mostrar_usuarios()
        input()

    else:
        print('Operação invalida')

# qual a marca
# qual modelod a marca

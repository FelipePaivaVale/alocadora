from locadora import *
from os import system, name

print('Bem-Vindo ao app de carros Lucas Samuel e Felipe\n')

def mensagem(msg):
    print('-' * 70)
    print(msg)

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

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
    mensagem('10- Verificar hitorico de cliente')
    mensagem('0 - encerrar programa')
    print('-' * 70)

    try:
        operação = int(input('Informe a operação que deseja realizar: '))
    except:
        operação = -1

    if (operação == 1):
        app.cadastrar()
        input()
        limpar_tela()

    elif (operação == 2):
        app.mostrar_carros()
        input()
        limpar_tela()
    
    elif(operação == 3):
        app.alugar_carro()
        input()
        limpar_tela()

    elif(operação == 4):
        app.devolver_carro()
        input()
        limpar_tela()
    
    elif (operação == 5):
        app.lista_de_marcas()
        marca = str(input("por qual marca deseja procurar? "))
        app.listar_marca(marca)
        input()
        limpar_tela()

    elif (operação == 6):
        app.lista_de_modelos()
        modelo = str(input("por qual modelo deseja procurar? "))
        app.listar_modelo(modelo)
        input()
        limpar_tela()

    elif(operação == 7):
        app.lista_de_anos()
        ano = int(input("de qual ano deseja ver os carros: "))
        app.listar_ano(ano)
        input()
        limpar_tela()

    elif(operação == 8):
        app.cadastrar_cliente()
        input()
        limpar_tela()
    
    elif(operação == 9):
        app.mostrar_usuarios()
        input()
        limpar_tela()

    elif(operação == 10):
        app.mostrar_historico()
        input()
        limpar_tela()

    elif(operação == 0):
        break

    else:
        print('Operação invalida\n')
        input()
        limpar_tela()

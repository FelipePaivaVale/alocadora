import random
from datetime import timedelta, date
from os import system, name

lista_carros = []
lista_clientes = []

class veiculo():
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._alugado = False
        
class carro(veiculo):
    def __init__(self,marca, modelo, ano, placa, km, val):
        super().__init__(marca, modelo, ano)
        self._placa = placa
        self._km = km
        self._val = val
        self._aluguel = self._val

    def alugar(self, tempo):
        self.tempo = int(tempo)
        self._alugado = True
        self._aluguel_a_pagar = self._val * self.tempo
        
        self._dia_alugado = date.today()
        self._entrega = timedelta(days= self.tempo) + timedelta(-1)
        self._dia_entrega = self._dia_alugado + (self._entrega)

    @property
    def km(self):
        return self._km
    
    @km.setter
    def km(self, kms):
        self._km = self._km + kms

    def devolver(self,dias):
        self.dias = int(dias)
        atrasado = False
        self._alugado = False

        self._tempo_para_entregar = timedelta(days= self.dias) + timedelta(-1)
        self._dia_devolvido = self._dia_alugado + self._tempo_para_entregar

        if(self._dia_entrega < self._dia_devolvido):
            atraso = self.dias - self.tempo
            atrasado = True
        
        if(atrasado == True):
            valor_total = (self._val*self.tempo) + ((self._val+(self._val*0.20))*atraso)

            tempo_atrasado = abs((self._dia_devolvido-self._dia_entrega).days)

            print(f"Entrega atrasada deveria ser entregue há: {tempo_atrasado} dias no dia {self._dia_entrega}")
        
        else:
            if(self.tempo > self.dias):
                valor_total = self._val*self.dias
                
            else:
                valor_total = self._val*self.tempo

        self._aluguel_a_pagar = valor_total

        return self._dia_devolvido

    def __str__(self):
        if(self._alugado == True):
            esta_alugado = "ALUGADO"
        else:
            esta_alugado = "DISPONIVEL PARA ALUGAR"
        return f"marca: {self._marca}\nmodelo: {self._modelo}\nano: {self._ano}\nplaca: {self._placa}\nquilometros radados: {self._km}\ndiaria: {self._val}\n{esta_alugado}"

class recibo(carro):
    def __init__(self, carro_alugado, km, data, entrega):
        self.carro_alugado = carro_alugado
        self.quilometragem_rodada  = km
        self.dia_do_aluguel = data
        self.dia_da_entrega = entrega
    
    def __str__(self) -> str:
        return f"marca: {self.carro_alugado._marca}\nmodelo: {self.carro_alugado._modelo}\nano: {self.carro_alugado._ano}\nplaca: {self.carro_alugado._placa}\nquilometros rodados no aluguel: {self.quilometragem_rodada}\nalugado dia: {self.dia_do_aluguel}\nentregue dia: {self.dia_da_entrega}"
    
class cliente(carro):
    def __init__(self, nome):
        self._nome = nome
        self._id = random.randint(100,999)
        self.historico = []

    @property   
    def nome(self):
        return self._nome
    
    @property   
    def id(self):
        return self._id

    def consultar_historico(self):
        if(len(self.historico) == 0):
            print("o usuario não alugou nenhum carro")
        
        else:
            for carros in self.historico:
                print("-"*10)
                print(carros)
                print("-"*10)

    def adicionar_historico(self,carro_novo, km, data, entrega):
        self.carro_alugado = recibo(carro_novo, km, data, entrega)
        self.historico.append(self.carro_alugado)
    
    def __str__(self):
        return f'cliente: {self._nome} - {self._id}'

class app(cliente, carro, veiculo):
    def cadastrar_cliente(self):
        novo_cliente = str(input("qual o nome do cliente: ").lower())
        lista_clientes.append(cliente(novo_cliente))

    def cadastrar(self):
        marca = str(input("marca: ").lower())
        modelo = str(input("modelo: ").lower())
        ano = int(input("ano: "))

        print("especificações do carro\n")
        placa = app.gerador_de_placa()
        km = int(input("quantos km rodados: "))
        diaria = int(input("qual o valor da diaria: "))

        lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))
        print("cadastrado com sucesso!!")

    def cadastro_auto(marca,modelo,ano,placa,km,diaria):
        lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

    def cadastro_usuario_auto(nome):
        lista_clientes.append(cliente(nome))

    def alugar_carro(self):
        carros_alugaveis = []
        for veiculos in lista_carros:
            if(veiculos._alugado == False):
                carros_alugaveis.append(veiculos)
           
        if(len(carros_alugaveis) == 0):
            print("não há carros disponiveis")

        else:
            i= 1
            for veiculos in lista_carros:
                if(veiculos._alugado == False):
                    print(i,"=========================")
                    print(veiculos)
                    print('==========================\n')
                i += 1
            carro_selecionado = int(input("selecione um carro para alugar: "))
            carro_selecionado = carro_selecionado-1
            
            try:
                self.carro_alugado = lista_carros[carro_selecionado]
            except:
                print("id de carro inexistente tente escolher outro")
                input()
                app.alugar_carro()

            tempo_aluguel = int(input("quantos dias deseja alugar: "))
            
            self.carro_alugado.alugar(tempo_aluguel)

            self.hoje = date.today()
            entrega = timedelta(days= tempo_aluguel) + timedelta(-1)
            data_entrega = self.hoje + entrega

            valor_total = self.carro_alugado._val * tempo_aluguel
            
            self.comprador = app.selecionar_comprador()

            print(f"o valor do seu aluguel é de R${valor_total}")
            print(f"alugado dia: {self.hoje}\ndata de entrega: {data_entrega}")
            print("ALUGADO COM SUCECSSO")

    def devolver_carro(self):
        carros_alugados = []
        for veiculos in lista_carros:
            if(veiculos._alugado == True):
                carros_alugados.append(veiculos)
        
        if(len(carros_alugados) == 0):
            print("não há carros alugados")

        else:
            i= 1
            for veiculos in lista_carros:
                if(veiculos._alugado == True):
                    print(i,"=========================")
                    print(veiculos)
                    print('==========================\n')
                i += 1

            carro_escolhido = int(input("qual carro deseja devolver: "))
            dias = int(input("em quantos dias foi feita a devolução: "))
            km_rodados = int(input("quantos kms foram rodados no carro: "))
            
            carro_escolhido = carro_escolhido-1

            try:
                carro_devolvido = lista_carros[carro_escolhido]
            except:
                print("id de carro inexistente tente escolher outro")
                input()
                app.devolver_carro()

            carro_devolvido.km = km_rodados

            dia_entrega = carro_devolvido.devolver(dias)

            valor_total = carro_devolvido._aluguel_a_pagar

            self.comprador.adicionar_historico(self.carro_alugado, carro_devolvido.km,self.hoje, dia_entrega)
            
            print(f"o valor a ser pago é de R${valor_total}\n \n")
            print("CARRO DEVOLVIDO")

    def mostrar_carros():
        for veiculos in lista_carros:
            print("-"*30)
            print(veiculos)
            
    def listar_marca(marca):
        lista_por_marca = []
        for veiculos in lista_carros:
            if (veiculos._marca == marca):
                lista_por_marca.append(veiculos)

        if(len(lista_por_marca) == 0):
            print("não há carros disponiveis desta marca")

        else:    
            for veiculos in lista_carros:
                if (veiculos._marca == marca):
                    print(veiculos)
                    print('==========================\n')

    def listar_modelo(modelo):
        lista_por_modelo = []
        for veiculos in lista_carros:
            if (veiculos._modelo == modelo):
                lista_por_modelo.append(veiculos)

        if(len(lista_por_modelo) == 0):
            print("não há carros disponiveis deste modelo")

        else:   
            for veiculos in lista_carros:
                if (veiculos._modelo == modelo):
                    print(veiculos)
                    print('==========================\n')

    def listar_ano(ano):
        lista_por_ano = []
        for veiculos in lista_carros:
            if(veiculos._ano == ano):
                lista_por_ano.append(veiculos)

        if(len(lista_por_ano) == 0):
            print("não possuimos carros deste ano")

        else:        
            for veiculos in lista_carros:
                if (veiculos._ano == ano):
                    print(veiculos)
                    print('==========================\n')

    def mostrar_usuarios():
        i = 1
        for user in lista_clientes:  
            print('-'*20)
            print(i,"-", user)
            i += 1
            
    def mostrar_alugados():
        i= 1
        for veiculos in lista_carros:
            if(veiculos._alugado == True):
                print(i,"=========================")
                print(veiculos)
                print('==========================\n')
            i += 1

    def mostrar_historico(self):
        app.mostrar_usuarios()

        escolhido = int(input("deseja verificar historico de qual usuario: "))

        escolhido = escolhido-1
        usuario_escolhido = lista_clientes[escolhido]

        usuario_escolhido.consultar_historico()
    
    def lista_de_marcas():
        lista_das_marcas = []

        for i in range(len(lista_carros)):
            lista_das_marcas.append(lista_carros[i]._marca)
        
        marcas_unicas = list(set(lista_das_marcas))
        
        for marcas in marcas_unicas: 
            print("-",marcas)
    
    def lista_de_modelos():
        lista_dos_modelos = []

        for i in range(len(lista_carros)):
            lista_dos_modelos.append(lista_carros[i]._modelo)

        modelos_unicos = list(set(lista_dos_modelos))

        for modelos in modelos_unicos:
            print("-",modelos)

    def lista_de_anos():
        lista_de_anos = []
        for i in range(len(lista_carros)):
            lista_de_anos.append(lista_carros[i]._ano)
        
        anos_unicos = list(set(lista_de_anos))
        anos_unicos.sort()

        for anos in anos_unicos:
            print(f"-{anos}", end=" ")
        print("")

    def gerador_de_placa():
        import string
        letras = string.ascii_uppercase
        numeros = string.digits
        placa = ''.join(random.choice(letras)for i in range(3))
        placa = placa + "".join(random.choice(numeros))
        placa = placa + "".join(random.choice(letras))
        placa = placa + "".join(random.choice(numeros)for i in range(2))
        return placa
    
    def selecionar_comprador():
        app.mostrar_usuarios()
        print('-'*20)
        print("0 - novo cliente\n")
        comprador = int(input("quem ira comprar o carro: "))
        if(comprador == 0):
            app.cadastrar_cliente()
            comprador = lista_clientes[-1]
        else:
            comprador = comprador-1
            comprador = lista_clientes[comprador]

        return comprador

app.cadastro_auto("fiat", "uno", 2019, app.gerador_de_placa(), 0, 50)
app.cadastro_auto("fiat", "pulse", 2018, app.gerador_de_placa(), 0, 90)
app.cadastro_auto("bmw", "x6", 2010, app.gerador_de_placa(), 0, 190)
app.cadastro_auto("bmw", "x5", 2014, app.gerador_de_placa(), 0, 200)
app.cadastro_auto("renault", "duster", 2018, app.gerador_de_placa(), 0, 90)
app.cadastro_auto("renault", "logan", 2011, app.gerador_de_placa(), 0, 80)
app.cadastro_usuario_auto('pedro')
app.cadastro_usuario_auto('josivaldo')

print('Bem-Vindo ao app de carros Lucas Samuel e Felipe\n')

def mensagem(msg):
    print('-' * 70)
    print(msg)

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class menu():
    def __init__(self):
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
                operação = int(input('Informe a operação que deseja realizar: ').strip())
            except:
                operação = -1

            if (operação == 1):
                app.cadastrar(self)
                input()
                limpar_tela()

            elif (operação == 2):
                app.mostrar_carros()
                input()
                limpar_tela()
            
            elif(operação == 3):
                app.alugar_carro(self)
                input()
                limpar_tela()

            elif(operação == 4):
                app.devolver_carro(self)
                input()
                limpar_tela()
            
            elif (operação == 5):
                app.lista_de_marcas()
                marca = str(input("por qual marca deseja procurar? ").lower())
                app.listar_marca(marca)
                input()
                limpar_tela()

            elif (operação == 6):
                app.lista_de_modelos()
                modelo = str(input("por qual modelo deseja procurar? ").lower())
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
                app.cadastrar_cliente(self)
                input()
                limpar_tela()
            
            elif(operação == 9):
                app.mostrar_usuarios()
                input()
                limpar_tela()

            elif(operação == 10):
                app.mostrar_historico(self)
                input()
                limpar_tela()

            elif(operação == 0):
                break

            else:
                print('Operação invalida\n')
                input()
                limpar_tela()

menu()

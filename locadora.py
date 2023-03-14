import random
from datetime import timedelta, date

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
        self._aluguel_a_pagar = self._val * tempo

        self._dia_alugado = date.today()
        self._entrega = timedelta(days= tempo)
        self._dia_entrega = self._dia_alugado + self._entrega

    @property
    def km(self):
        return self._km

    def devolver(self,dias):
        self.dias = int(dias)
        atrasado = False
        self._alugado = False

        self._tempo_para_entregar = timedelta(days= dias)
        self._dia_devolvido = self._dia_alugado + self._tempo_para_entregar

        if(self._dia_entrega < self._dia_devolvido):
            atraso = self.dias - self.tempo
            atrasado = True

        if(atrasado == True):
            valor_total = (self._val*self.tempo) + ((self._val+(self._val*0.20))*atraso)
            tempo_atrasado = abs((self._dia_devolvido-self._dia_entrega).days)

            print(f"Entrega atrasada deveria ser entregue há: {tempo_atrasado} dias no dia {self._dia_entrega}")

        else:
            valor_total = self._val*self.tempo

        self._aluguel_a_pagar = valor_total

    def __str__(self):
        if(self._alugado == True):
            esta_alugado = "ALUGADO"
        else:
            esta_alugado = "DISPONIVEL PARA ALUGAR"
        return f"marca: {self._marca}\nmodelo: {self._modelo}\nano: {self._ano}\nplaca: {self._placa}\nquilometros radados: {self._km}\ndiaria: {self._aluguel}\n{esta_alugado}"
    
class cliente():
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
                print("="*10)
                print(carros)
                print("="*10)

    def alugar_carro_usuario(self,carro_novo):
        self.historico.append(carro_novo)
    
    def __str__(self):
        return f'cliente: {self._nome} - {self._id}'

class app(cliente, carro, veiculo):
    def cadastrar_cliente():
        novo_cliente = str(input("qual o nome do cliente: "))
        lista_clientes.append(cliente(novo_cliente))

    def cadastrar():
        marca = str(input("marca: "))
        modelo = str(input("modelo: "))
        ano = int(input("ano: "))

        print("especificações do carro\n")
        placa = app.gerador_de_placa()
        km = int(input("quantos km rodados: "))
        diaria = int(input("qual o valor da diaria: "))

        lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

    def cadastro_auto(marca,modelo,ano,placa,km,diaria):
        lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

    def cadastro_usuario_auto(nome):
        lista_clientes.append(cliente(nome))

    def alugar_carro():
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
                carro_alugado = lista_carros[carro_selecionado]
            except:
                print("id de carro inexistente tente escolher outro")
                input()
                app.alugar_carro()

            tempo_aluguel = int(input("quantos dias deseja alugar: "))
            
            carro_alugado.alugar(tempo_aluguel)

            hoje = date.today()
            entrega = timedelta(days= tempo_aluguel)
            data_entrega = hoje + entrega

            valor_total = carro_alugado._val * tempo_aluguel

            comprador = app.selecionar_comprador()

            comprador.alugar_carro_usuario(carro_alugado)

            print(f"o valor do seu aluguel é de R${valor_total}")
            print(f"alugado dia: {hoje}\ndata de entrega: {data_entrega}")

    def devolver_carro():
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
            
            carro_escolhido = carro_escolhido-1
            try:
                carro_devolvido = lista_carros[carro_escolhido]
            except:
                print("id de carro inexistente tente escolher outro")
                input()
                app.devolver_carro()

            carro_devolvido.devolver(dias)
            valor_total = carro_devolvido._aluguel_a_pagar

            print(f"o valor a ser pago é de R${valor_total}\n \n")

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
            print(i, '='*20)
            print(user)
            i += 1
            
    def mostrar_alugados():
        i= 1
        for veiculos in lista_carros:
            if(veiculos._alugado == True):
                print(i,"=========================")
                print(veiculos)
                print('==========================\n')
            i += 1

    def mostrar_historico():
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

    def gerador_de_placa():
        import string
        letras = string.ascii_uppercase
        numeros = string.digits
        placa = ''.join(random.choice(letras)for i in range(3))
        placa = placa + "".join(random.choice(numeros))
        placa = placa + "".join(random.choice(letras))
        placa = placa + "".join(random.choice(numeros)for i in range(2))
    
    def selecionar_comprador():
        app.mostrar_usuarios()
        print(0,'='*20)
        print("novo cliente")
        comprador = int(input("quem ira comprar o carro: "))
        if(comprador == 0):
            app.cadastrar_cliente()
            comprador = lista_clientes[-1]
        else:
            comprador = comprador-1
            comprador = lista_clientes[comprador]

        return comprador
        

app.cadastro_auto("fiat", "uno", 2019, app.gerador_de_placa(), 0, 30)
app.cadastro_auto("fiat", "pulse", 2018, app.gerador_de_placa(), 0, 30)
app.cadastro_auto("bmw", "x6", 2010, app.gerador_de_placa(), 0, 30)
app.cadastro_auto("bmw", "x5", 2014, app.gerador_de_placa(), 0, 30)
app.cadastro_auto("renault", "duster", 2018, app.gerador_de_placa(), 0, 30)
app.cadastro_auto("renault", "logan", 2011, app.gerador_de_placa(), 0, 30)
app.cadastro_usuario_auto('pedro')
app.cadastro_usuario_auto('josivaldo')

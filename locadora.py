lista_carros = []
lista_clientes = []

class veiculo:
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

    def alugar(self, tempo):
        self.tempo = int(tempo) 
        self._alugado = True
        self._aluguel = self._val * tempo

    @property
    def aluguel(self):
        return self._aluguel
    
    def devolver(self,dias):
        self.dias = int(dias)
        atrasado = False
        self._alugado = False
        
        if(self.tempo < self.dias):
            atraso = self.dias - self.tempo
            atrasado = True

        if(atrasado == True):
            valor_total = (self._val*self.tempo) + ((self._val+(self._val*0.20))*atraso)

        else:
            valor_total = self._val*self.tempo

        self._aluguel = valor_total

    def __str__(self):
        return f"modelo: {self._modelo}\nmarca: {self._marca}\nano: {self._ano}\nplaca: {self._placa}\nquilometros radados: {self._km}"
    
class cliente():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        
def cadastrar():
    marca = str(input("marca: "))
    modelo = str(input("modelo: "))
    ano = int(input("ano: "))

    print("especificações do carro")
    placa = str(input("qual a placa do carro: "))
    km = int(input("quantos km rodados: "))
    diaria = int(input("qual o valor da diaria: "))

    lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

def cadastro_auto(marca,modelo,ano,placa,km,diaria):
    lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

def alugar_carro():
    i= 1
    for veiculos in lista_carros:
        if(veiculos._alugado == False):
            print(i,"=========================")
            print(veiculos)
            print('==========================\n')
        i += 1

    carro_selecionado = int(input("selecione um carro para alugar: "))
    carro_selecionado = carro_selecionado-1
    carro_alugado = lista_carros[carro_selecionado]

    tempo_aluguel = int(input("quantos dias deseja alugar: "))
    
    carro_alugado.alugar(tempo_aluguel)

    valor_total = carro_alugado._val * tempo_aluguel
    print(f"o valor do seu aluguel é de R${valor_total}")

def devolver_carro():
    i= 1
    for veiculos in lista_carros:
        if(veiculos._alugado == True):
            print(i,"=========================")
            print(veiculos)
            print('==========================\n')
        i += 1

    carro_escolhido = int(input("qual carro deseja devolver"))
    dias = int(input("em quantos dias foi feita a devolução"))
    
    carro_escolhido = carro_escolhido-1
    carro_devolvido = lista_carros[carro_escolhido]

    carro_devolvido.devolver(dias)
    valor_total = carro_devolvido.aluguel

    print(f"o valor a ser pago é de R${valor_total}")

def mostrar_carros():
    for veiculos in lista_carros:
        print("-"*30)
        print(veiculos)
        
def listar_marca(marca):
    for veiculos in lista_carros:
        if (veiculos._marca == marca):
            print(veiculos)
            print('==========================\n')

def listar_modelo(modelo):
    for veiculos in lista_carros:
        if (veiculos._modelo == modelo):
            print(veiculos)
            print('==========================\n')

def listar_ano(ano):
    for veiculos in lista_carros:
        if (veiculos._ano == ano):
            print(veiculos)
            print('==========================\n')


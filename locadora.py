lista_carros = []

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
        self.tempo = tempo 
        self._alugado = True
        
    def devolver(self,dias):
        atrasado = False

        if(self.tempo < dias):
            atraso = self.tempo - dias
            atrasado = True

        if(atrasado == True):
            aluguel = self._val + ((self._val/100)*20)*atraso
        else:
            aluguel = self._val*self.tempo

        return aluguel
    
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

    return lista_carros

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
    dias_da_devolução = int(input("em quantos dias foi feita a devolução"))
    
    carro_escolhido = carro_devolvido-1
    carro_devolvido = lista_carros[carro_escolhido]
    carro_devolvido.devolver(dias_da_devolução)

def mostrar_carros():
    for veiculos in lista_carros:
        print(veiculos)
                  

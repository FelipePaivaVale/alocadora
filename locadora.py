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
        self.alugado = True
        
    def devolver(self,dias):
        atrasado = False

        if(self.tempo < dias):
            atraso = self.tempo - dias
            atrasado = True

        if(atrasado == True):
            aluguel = self._val + ((self._val/100)*20)*atraso

        return aluguel
    
    def alugado(self):
        if(self._alugado == True):
            print("o carro esta alugado")
        else:
            print("o carro nao esta alugado")

    def __str__(self):
        return f"modelo: {self._modelo}\nmarca: {self._marca}\nano: {self._ano}\nplaca: {self._placa}\nquilometros radados: {self._km}\n"
    
class cliente():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        
def cadastrar():
    marca = str(input("marca: "))
    ano = int(input("ano: "))
    modelo = str(input("modelo: "))
    print("especificações do carro")
    placa = str(input("qual a placa do carro: "))
    km = int(input("quantos km rodados: "))
    diaria = int(input("qual o valor da diaria: "))
    lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

def cadastro_auto(marca,modelo,ano,placa,km,diaria):
    lista_carros.append(carro(marca, modelo, ano, placa, km, diaria))

cadastro_auto("fiat","uno",2020,"abc123",0,20)
cadastro_auto("fiat","riske",2020,"anc343",0,20)
cadastro_auto("bmw","breske",2020,"akr250",0,20)
cadastro_auto("bmw","xesque",2020,"kbm345",0,20)

i= 1
for veiculos in lista_carros:
    print(i,"=========================")
    print(veiculos)
    print('==========================\n')
    i += 1


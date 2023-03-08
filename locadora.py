lista_carros = []

class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._alugado = False

    def alugar(self, tempo):
        self.tempo = tempo 
        self._alugado = True
        
    def devolver(self,dias):
        atrasado = False

        if(self.tempo < dias):
            atraso = self.tempo - dias
            atrasado = True

        if(atrasado == True):
            aluguel = self.val_diaria + ((self.val_diaria/100)*20)*atraso

        return aluguel
    
    def alugado(self):
        if(self._alugado == True):
            print("o carro esta alugado")
        else:
            print("o carro nao esta alugado")
        
class carro(veiculo):
    def __init__(self, placa, km, val):
        self.placa = placa
        self.km = km
        self.val = val

    def __str__(self):
        return print(f'''modelo -> {self.modelo}
        marca -> {self.marca}
        ano -> {self.ano}
        placa -> {self.placa}
        km rodados -> {self.km}''')
    
class cliente(carro):
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

def cadastrar():
    marca = str(input("escreva o modelo "))
    ano = int(input("escreva o ano "))
    c = carro(marca, ano)
    lista_carros.append(c)

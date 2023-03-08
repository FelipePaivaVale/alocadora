lista_carros = []

class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._alugado = False
        
class carro(veiculo):
    def __init__(self,marca, modelo, ano, placa, km, val):
        self.placa = placa
        self.km = km
        self.val = val
        super().__init__(marca,modelo, ano)

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

    def __str__(self):
        return f'''modelo -> {self.modelo}
        marca -> {self.marca}
        ano -> {self.ano}
        placa -> {self.placa}
        km rodados -> {self.km}'''
    
class cliente():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

def cadastrar():
    marca = str(input("escreva o marca "))
    ano = int(input("escreva o ano "))
    modelo = str(input("escreva o modelo "))
    print("especificações do carro")
    placa = str(input("qual a placa do carro"))
    km = int(input("quantos km rodados"))
    diaria = int(input("qual o valor da diaria"))
    c = carro(marca, modelo, ano, placa, km, diaria)
    lista_carros.append(c)

c1 = cadastrar()
print(c1)

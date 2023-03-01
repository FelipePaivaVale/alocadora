class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def alugar(self, tempo,val_diaria):
        self.tempo = tempo
        self.val_diaria = val_diaria
        
    def devolver(self,dias):
        atraso = False

        if(self.tempo < dias):
            atraso = self.tempo - dias
            atraso = True

        if(atraso = True):
            aluguel = self.val_diaria+ ((self.val_diaria/100)*20)*atraso

        return aluguel

class carro(veiculo):
    def __init__(self, placa, km, val):
        self.placa = placa
        self.km = km
        self.val = val
    

class cliente(carro):
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

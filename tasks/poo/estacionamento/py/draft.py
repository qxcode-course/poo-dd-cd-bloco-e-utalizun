from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, hora_entrada: int):
        self.id = id
        self.tipo = tipo
        self.hora_entrada = 0

    def setEntrada(self, hora):
        self.hora_entrada = hora

    def getEntrada(self):
        return self.hora_entrada
    
    def getId(self):
        return self.id
    
    def getTipo(self):
        return self.tipo
    
    @abstractmethod
    def calcular_valor(self, hora_saida):
        pass

    def __str__(self):
        return f"__{self.tipo} : ___{self.id} : {self.horaEntrada}"
    
class Bike(Veiculo):
    def __init__(self, id):
        super().__init__(id,"Bike")

    def calcular_valor(self, hora_saida):
        return 3.0
    

class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaAtual = 0

    def procurar_veiculo(self, id):
        for i, v in enumerate(self.veiculos):
            if v.getId() == id:
                return i
        return -1
    
    def passarTempo(self, tempo):
        self.horaAtual += tempo 

    def estacionar(self, veiculo):
        veiculo.setEntrada(self.horaAtual)
        self.veiculos.append(veiculo)

    def pagar(self, id):
        idx = self.procurar_veiculo(id)
        if idx == -1:
            return
        
        v = self.veiculos [idx]
        valor = v.calcular_valor(self.horaAtual)

        print (
            f"{v.getTipo()} chegou {v.getEntrada()} saiu{self.horaAtual}."
            f"Pagar R$ {valor:.2}"
        )

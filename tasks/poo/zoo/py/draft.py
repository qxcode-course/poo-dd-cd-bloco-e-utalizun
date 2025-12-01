from abc import ABC, abstractmethod

class Brinquedo(ABC):
    @abstractmethod
    def apertar(self):
        pass
    @abstractmethod
    def jogar_no_chao(self):
        pass

def brincar(brinquedo: Brinquedo):
    brinquedo.apertar()
    brinquedo.jogar_no_chao()
    print(brinquedo)
    
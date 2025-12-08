from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou o(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass

class papa_leguas(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    def fazer_som(self):
        print("BEEP - BEEP")

    def mover(self):
        print("Correu!!")

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    def fazer_som(self):
        print("RWAAAAAW Hakuna Matata")

    def mover(self):
        print("Desfilando")
        
class Cachorro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    def fazer_som(self):
        print("Scooby-doobee-doooo")

    def mover(self):
        print("Correu do fantasma!")

class Passarinho(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    def fazer_som(self):
        print("Eu acho que vi um gatinho!")

    def mover(self):
        print("Se escondeu do Frajola!")

class Lagarta(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    def fazer_som(self):
        print("Tu! Quem És Tu?!")

    def mover(self):
        print("tornou-se Borboleta")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Tipo: {type(animal).__name__} \n")

#

animais: list[Animal] = [
    papa_leguas("papa doido"),
    Leao("Simba"),
    Cachorro("Scooby"),
    Passarinho("Piu-Piu"),
    Lagarta("Absolen")
]

for animal in animais:
    apresentar(animal)
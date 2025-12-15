from abc import ABC, abstractmethod
class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")
        
    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: str, nome_titular:str, limite: float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite = limite

    def resumo(self):
        return "Cartão de credito: " + super().resumo()
    
    def get_limite(self):
        return self.limite
    
    def processar(self):
        if self.valor > self.limite:
            print(f"pagamento recusado por por limite insuficiente no cartão {self.numero}")
            return
        self.limite -= self.valor
        print(f"pagamento aprovado no cartão {self.numero}, com titular de nome {self.nome_titular}.")

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"pagamento aprovado via pix, com chave {self.chave} no banco {self.banco}.")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, cod_barras: int, vencimento: str):
        super().__init__(valor, descricao)
        self.cod_barras = cod_barras
        self.vencimento = vencimento

    def processar(self):
        print("O boleto foi gerado, aguardando pagamento... \n")
        print(f"Vencimento: {self.vencimento}")

def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    print(pagamento.resumo())
    pagamento.processar()








# os teste são aqui:

compra1 = CartaoCredito(150.0, "Compra de eletrônicos", "1234-5678-9012-3456", "João Silva", 500.0)
compra2 = Pix(75.0, "Pagamento de serviços", "talisson@email.com", "Banco X")
compra3 = Boleto(222.0, "Pagamento", 12345678900987654321, "13/12/2025")
compra4 = CartaoCredito(600.0, "Compra de móveis", "9876-5432-1098-7654", "Maria Oliveira", 500.0)


Pagamento = [compra1, compra2, compra3, compra4]
for pagamento in Pagamento:
    print("\nprocessando pagamento...")
    try:
        processar_pagamento(pagamento)
    except ValueError as e:
        print(e)
    print("-" * 40)

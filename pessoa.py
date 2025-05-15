class Pessoa:
    def __init__(self, nome, cpf, status):
        self.nome = nome
        self.cpf = cpf
        self.status = status

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Status: {self.status}"

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome}: R${self.preco:.2f}, Quantidade: {self.quantidade}"
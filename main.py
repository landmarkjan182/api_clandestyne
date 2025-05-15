#Mateus Yuri Koike
#joao victor brandao
#Gabriel Eiji Nakandakari shinkae
import os
from pessoa import Pessoa, Produto


class SistemaEstoque:
    ARQUIVO_ESTOQUE = 'estoque.txt'
    ARQUIVO_PESSOAS = 'pessoas.txt'
    ARQUIVO_VENDAS = 'vendas.txt'

    def __init__(self):
        self.estoque = {}
        self.pessoas = {}
        self.carregar_dados()

    def carregar_dados(self):
        self.carregar_estoque()
        self.carregar_pessoas()

    def carregar_pessoas(self):
        if os.path.exists(self.ARQUIVO_PESSOAS):
            with open(self.ARQUIVO_PESSOAS, 'r') as f:
                self.pessoas = {}
                for line in f:
                    nome, cpf, status = line.strip().split(',')
                    self.pessoas[cpf] = Pessoa(nome, cpf, status)

    def salvar_pessoas(self):
        with open(self.ARQUIVO_PESSOAS, 'w') as f:
            for cpf, pessoa in self.pessoas.items():
                f.write(f"{pessoa.nome},{pessoa.cpf},{pessoa.status}\n")

    def carregar_estoque(self):
        if os.path.exists(self.ARQUIVO_ESTOQUE):
            with open(self.ARQUIVO_ESTOQUE, 'r') as f:
                self.estoque = {}
                for line in f:
                    nome, preco, quantidade = line.strip().split(',')
                    self.estoque[nome] = Produto(nome, float(preco), int(quantidade))
        else:
            self.criar_estoque_inicial()
    
    def cadastrar_produto(self, nome, preco, quantidade):
        
        try:
            preco_float = float(preco)
            quantidade_int = int(quantidade)
            
            if nome in self.estoque:             
                self.estoque[nome].quantidade += quantidade_int
                print(f"Quantidade do produto '{nome}' atualizada.")
            else:              
                if preco_float <= 0 or quantidade_int < 0:
                    print("Erro: Valores devem ser positivos.")
                    return False
                self.estoque[nome] = Produto(nome, preco_float, quantidade_int)
                print(f"Produto '{nome}' cadastrado com sucesso!")
            
            self.salvar_estoque()
            return True
            
        except ValueError:
            print("Erro: Valores inválidos para preço ou quantidade.")
            return False

    def adicionar_estoque(self, nome, quantidade):
        if nome not in self.estoque:
            print("Erro: Produto não encontrado.")
            return False
        
        try:
            quantidade_int = int(quantidade)
            if quantidade_int <= 0:
                print("Erro: Quantidade deve ser positiva.")
                return False
                
            self.estoque[nome].quantidade += quantidade_int
            self.salvar_estoque()
            print(f"Estoque de '{nome}' atualizado com sucesso!")
            return True
            
        except ValueError:
            print("Erro: Quantidade inválida.")
            return False
        
    def criar_estoque_inicial(self):
        estoque_inicial = [
            ("Camiseta com estampa padrão", 55, 50),
            ("Camiseta com estampa pequena", 50, 50),
            ("Camiseta sem estampa", 40, 50),
            ("Cordão de moto", 10, 50),
            ("Pulseira", 5, 50),
            ("Capinha de telefone com estampa", 25, 50),
            ("Adesivo", 5, 50),
            ("Chaveiro", 10, 50),
            ("Capacete", 500, 50),
            ("Capacete personalizado", 600, 50),
            ("Blusa de frio", 150, 50),
            ("Luva", 100, 50),
            ("Calça", 40, 50)
        ]
        with open(self.ARQUIVO_ESTOQUE, 'w') as f:
            for nome, preco, quantidade in estoque_inicial:
                f.write(f"{nome},{preco},{quantidade}\n")
                self.estoque[nome] = Produto(nome, preco, quantidade)

    def salvar_estoque(self):
        with open(self.ARQUIVO_ESTOQUE, 'w') as f:
            for produto in self.estoque.values():
                f.write(f"{produto.nome},{produto.preco},{produto.quantidade}\n")

    def registrar_venda(self, nome_produto, quantidade, valor_total):
        with open(self.ARQUIVO_VENDAS, 'a') as f:
            f.write(f"{nome_produto},{quantidade},{valor_total}\n")

    def realizar_venda(self, nome, quantidade):
        if nome not in self.estoque:
            print("Produto não encontrado.")
            return False
        
        produto = self.estoque[nome]
        
        if produto.quantidade < quantidade:
            print("Quantidade insuficiente em estoque.")
            return False
        
        total = quantidade * produto.preco
        produto.quantidade -= quantidade
        
        self.salvar_estoque()
        self.registrar_venda(nome, quantidade, total)
        
        print(f"Venda realizada. Total: R${total:.2f}")
        return True

    def listar_estoque(self):
        print("\n--- ESTOQUE ---")
        if not self.estoque:
            print("Estoque vazio.")
        else:
            for produto in self.estoque.values():
                print(produto)

    def listar_pessoas(self):
        print("\n--- PESSOAS CADASTRADAS ---")
        if not self.pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in self.pessoas.values():
                print(pessoa)

    def listar_vendas(self):
        print("\n--- VENDAS REALIZADAS ---")
        if not os.path.exists(self.ARQUIVO_VENDAS):
            print("Nenhuma venda registrada.")
        else:
            with open(self.ARQUIVO_VENDAS, 'r') as f:
                for line in f:
                    nome, quantidade, total = line.strip().split(',')
                    print(f"Produto: {nome}, Quantidade: {quantidade}, Total: R${float(total):.2f}")                

if __name__ == "__main__":
    from menu import Menu
    sistema = SistemaEstoque()
    menu = Menu(sistema)
    menu.exibir_menu()

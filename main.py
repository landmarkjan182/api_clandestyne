#mateus yuri koike
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




import os
from pessoa import Pessoa

class Menu:
    def __init__(self, sistema):
        self.sistema = sistema

    def limpar_tela(self):
        os.system('clear')

    def exibir_cabecalho(self):
        self.limpar_tela()
        print("\n" + "=" * 50)
        print("  🏍️ Sistema de Gestão do Motoclube 🏍️")
        print("=" * 50)
        print("\nMENU PRINCIPAL:")
        print("1. Listar estoque completo")
        print("2. Cadastrar novo produto")
        print("3. Adicionar quantidade a produto existente")
        print("4. Realizar venda")
        print("5. Cadastrar novo membro")
        print("6. Listar todos os membros")
        print("7. Ver histórico de vendas")
        print("8. Sair do sistema")
        print("=" * 50)

    def cadastrar_produto(self):
        self.limpar_tela()
        print("\n" + "=" * 50)
        print("   📦 CADASTRO DE NOVO PRODUTO   ")
        print("=" * 50)
        
        nome = input("\nNome do produto: ").strip()
        if not nome:
            print("\nErro: Nome do produto não pode estar vazio!")
            input("\nPressione Enter para voltar...")
            return

        preco = input("Preço unitário (R$): ").strip()
        quantidade = input("Quantidade inicial: ").strip()

        if self.sistema.cadastrar_produto(nome, preco, quantidade):
            print(f"\n✅ Produto '{nome}' cadastrado/atualizado com sucesso!")
        else:
            print("\n❌ Falha ao cadastrar produto. Verifique os dados.")
        
        input("\nPressione Enter para voltar...")

    def adicionar_estoque(self):
        self.limpar_tela()
        print("\n" + "=" * 50)
        print("   📈 ADICIONAR QUANTIDADE   ")
        print("=" * 50)
        
        if not self.sistema.estoque:
            print("\nEstoque vazio. Cadastre produtos primeiro.")
            input("\nPressione Enter para voltar...")
            return

        print("\nProdutos disponíveis:")
        self.sistema.listar_estoque()
        
        nome = input("\nNome do produto: ").strip()
        if nome not in self.sistema.estoque:
            print("\n❌ Produto não encontrado!")
            input("\nPressione Enter para voltar...")
            return

        quantidade = input("Quantidade a adicionar: ").strip()
        
        if self.sistema.adicionar_estoque(nome, quantidade):
            print(f"\n✅ Estoque de '{nome}' atualizado com sucesso!")
        else:
            print("\n❌ Operação falhou. Verifique a quantidade.")
        
        input("\nPressione Enter para voltar...")

    def realizar_venda(self):
        self.limpar_tela()
        print("\n" + "=" * 50)
        print("   💰 REALIZAR VENDA   ")
        print("=" * 50)
        
        if not self.sistema.estoque:
            print("\nEstoque vazio. Cadastre produtos primeiro.")
            input("\nPressione Enter para voltar...")
            return

        print("\nProdutos disponíveis:")
        self.sistema.listar_estoque()
        
        nome = input("\nProduto vendido: ").strip()
        if nome not in self.sistema.estoque:
            print("\n❌ Produto não encontrado!")
            input("\nPressione Enter para voltar...")
            return

        try:
            quantidade = int(input("Quantidade vendida: ").strip())
            if quantidade <= 0:
                print("\n❌ Quantidade deve ser maior que zero!")
                input("\nPressione Enter para voltar...")
                return
                
            if self.sistema.realizar_venda(nome, quantidade):
                print("\n✅ Venda registrada com sucesso!")
            else:
                print("\n❌ Falha ao registrar venda.")
        except ValueError:
            print("\n❌ Quantidade inválida! Use números inteiros.")
        
        input("\nPressione Enter para voltar...")

    def cadastrar_pessoa(self):
        self.limpar_tela()
        print("\n" + "=" * 50)
        print("   👤 CADASTRO DE MEMBRO   ")
        print("=" * 50)
        
        nome = input("\nNome completo: ").strip()
        if not nome:
            print("\n❌ Nome não pode estar vazio!")
            input("\nPressione Enter para voltar...")
            return

        cpf = input("CPF (apenas números): ").strip()
        if not cpf.isdigit():
            print("\n❌ CPF deve conter apenas números!")
            input("\nPressione Enter para voltar...")
            return

        print("\nTipo de membro:")
        print("1. Membro Fundador")
        print("2. Membro Regular")
        print("3. Novato")
        print("4. Associado")
        print("5. Visitante")
        
        status_opcao = input("\nOpção (1-5): ").strip()
        status_dict = {
            '1': 'Membro Fundador',
            '2': 'Membro Regular',
            '3': 'Novato',
            '4': 'Associado',
            '5': 'Visitante'
        }
        
        status = status_dict.get(status_opcao, 'Visitante')
        self.sistema.pessoas[cpf] = Pessoa(nome, cpf, status)
        self.sistema.salvar_pessoas()
        
        print(f"\n✅ {nome} cadastrado como {status} com sucesso!")
        input("\nPressione Enter para voltar...")

    def exibir_menu(self):
        while True:
            self.exibir_cabecalho()
            opcao = input("\nEscolha uma opção (1-8): ").strip()

            if opcao == '1':
                self.limpar_tela()
                self.sistema.listar_estoque()
                input("\nPressione Enter para voltar...")
            elif opcao == '2':
                self.cadastrar_produto()
            elif opcao == '3':
                self.adicionar_estoque()
            elif opcao == '4':
                self.realizar_venda()
            elif opcao == '5':
                self.cadastrar_pessoa()
            elif opcao == '6':
                self.limpar_tela()
                self.sistema.listar_pessoas()
                input("\nPressione Enter para voltar...")
            elif opcao == '7':
                self.limpar_tela()
                self.sistema.listar_vendas()
                input("\nPressione Enter para voltar...")
            elif opcao == '8':
                print("\n🚀 Saindo do sistema... Até logo! 🚀")
                break
            else:
                print("\n❌ Opção inválida! Escolha de 1 a 8.")
                input("\nPressione Enter para tentar novamente...")

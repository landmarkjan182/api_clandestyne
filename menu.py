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
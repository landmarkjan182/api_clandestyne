# 🏍️ Sistema de Estoque do Motoclube

Este sistema foi desenvolvido para gerenciar o estoque de produtos, realizar vendas e cadastrar pessoas ligadas ao motoclube (como membros, civis, novatos, etc). Tudo é feito diretamente no terminal, com armazenamento dos dados em arquivos `.txt`.

## ✅ Funcionalidades

- Visualizar o estoque de produtos
- Registrar vendas
- Cadastrar pessoas com status personalizado
- Listar pessoas cadastradas
- Listar vendas realizadas

## 📁 Arquivos do Projeto

- `main.py`: Arquivo principal, inicializa o sistema.
- `menu.py`: Controla a exibição do menu e a interação com o usuário.
- `pessoa.py`: Contém as classes `Pessoa` e `Produto`, responsáveis por armazenar dados de pessoas e itens do estoque.
- `estoque.txt`: Arquivo gerado automaticamente com os produtos disponíveis.
- `pessoas.txt`: Armazena os dados das pessoas cadastradas.
- `vendas.txt`: Registra o histórico de vendas realizadas.

## ▶️ Como usar

1. Coloque os arquivos `main.py`, `menu.py` e `pessoa.py` na mesma pasta.
2. Execute o `main.py`.
3. O menu exibirá as seguintes opções:
   - **1**: Listar o estoque
   - **2**: Realizar uma venda
   - **3**: Cadastrar uma pessoa (com CPF e status)
   - **4**: Listar todas as pessoas cadastradas
   - **5**: Ver o histórico de vendas
   - **6**: Sair do sistema

As informações são salvas automaticamente nos arquivos `.txt`, permitindo que os dados sejam mantidos mesmo após encerrar o programa.

## 👨‍💻 Desenvolvedores

- Mateus Yuri Koike  
- João Victor Brandão  
- Gabriel Eiji Nakandakari Shinkae


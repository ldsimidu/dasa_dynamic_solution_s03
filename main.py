import os

def limpa_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

# Garante que o usuário escolha uma opção válida da lista
def forca_opcao(lista, mensagem):
    while True:
        escolha = input(mensagem)
        if escolha not in lista:
            print("⚠️  Escolha inválida")
        else:
            return escolha

# Solicita input até que um texto não vazio seja fornecido
def input_nao_vazio(mensagem):
    while True:
        variavel = input(mensagem)
        if variavel == "":
            print(f"⚠️ Texto não pode ser vazio")
        else:
            return variavel

# Aguarda o usuário pressionar Enter e retorna ao menu principal
def retorna_menu():
    input("\n\n◀️ Insira qualquer valor para voltar ao menu!")
    main_estoque()


def main_estoque():
    limpa_tela()
    opc_menu = ['1','2','3','4','5','0']

    print("-=" * 17)
    print('''
        1) Cadastrar item
        2) Listar item
        3) Descontar item
        4) Comprar itens
        5) Relatório de Estoque
        0) Sair
    ''')
    print("-=" * 17 + "\n")

    escolha = forca_opcao(opc_menu, 'Qual opção o usuário deseja acessar?:\n-> ')
    if escolha == "1":
        cadastro_item()
    elif escolha == "2":
        listar_item_cadastrados()
    elif escolha == "3":
        desconto()
    elif escolha == "4":
        compra()
    elif escolha == "5":
        relatorio_estoque()
    elif escolha == "0":
        print("👋 Volte sempre! =)")

def cadastro_item():
    limpa_tela()

def listar_item_cadastrados():
    limpa_tela()

def desconto():
    limpa_tela()

def compra():
    limpa_tela()

def relatorio_estoque():
    limpa_tela()

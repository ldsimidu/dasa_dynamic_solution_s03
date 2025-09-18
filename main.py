import os
from collections import deque


# Estrutura de dados
estoque = []
fila_consumo = deque()
pilha_consumo = []



#Funções

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

#Algoritimos de ordenação
def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    while esquerda and direita:
        if esquerda[0][chave] <= direita[0][chave]:
            resultado.append(esquerda.pop(0))
        else:
            resultado.append(direita.pop(0))
    resultado.extend(esquerda if esquerda else direita)
    return resultado

def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave]> pivo[chave]]
    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

#Algoritimos de busca 
def busca_sequencial(lista, nome):
    for item in lista:
        if item["nome"].lower() == nome.lower():
            return item
    return None

def busca_binaria(lista, nome):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]["nome"].lower() == nome.lower():
            return lista[meio]
        elif lista[meio]["nome"].lower() < nome.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return None


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
        6) Relatório de Estoque
        0) Sair
    ''')
    print("-=" * 17 + "\n")

    escolha = forca_opcao(opc_menu, 'Qual opção o usuário deseja acessar?:\n-> ')
    if escolha == "1":
        cadastro_item()
    elif escolha == "2":
        listar_item_cadastrados()
    elif escolha == "3":
        registrar_consumo()
    elif escolha == "4":
        menu_busca()
    elif escolha == "5":
        menu_ordenacao()
    elif escoha == "6":
        relatorio_estoque()
    elif escolha == "0":
        print("👋 Volte sempre! =)")

def cadastro_item():
    limpa_tela()
    nome = input_nao_vazio("Nome do insumo: ")
    quantidade = int(input("Quantidade inicial: "))
    validade = input_nao_vazio("Validade (AAAA-MM-DD): ")
    estoque.append({"nome": nome, "quantidade": quantidade, "validade": validade})
    print(f"✅ {nome} cadastrado com sucesso!")
    retorna_menu()

def listar_item_cadastrados():
    limpa_tela()

def desconto():
    limpa_tela()

def compra():
    limpa_tela()

def relatorio_estoque():
    limpa_tela()

# Executar
if __name__ == "__main__":
    main_estoque()
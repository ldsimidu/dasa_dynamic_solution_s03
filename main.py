import os
import random
from collections import deque

# Estruturas de dados

estoque = []
fila_consumo = deque()   
pilha_consumo = []       


# Utilidades de I/O
def limpa_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

def pausa():
    input("\n\n◀️  Pressione Enter para voltar ao menu...")

def forca_opcao(lista, mensagem):
    while True:
        escolha = input(mensagem).strip()
        if escolha not in lista:
            print("⚠️  Escolha inválida.")
        else:
            return escolha

def input_nao_vazio(mensagem):
    while True:
        variavel = input(mensagem).strip()
        if variavel == "":
            print("⚠️  Texto não pode ser vazio.")
        else:
            return variavel

def input_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        txt = input(mensagem).strip()
        try:
            val = int(txt)
            if minimo is not None and val < minimo:
                print(f"⚠️  Valor deve ser ≥ {minimo}.")
                continue
            if maximo is not None and val > maximo:
                print(f"⚠️  Valor deve ser ≤ {maximo}.")
                continue
            return val
        except ValueError:
            print("⚠️  Digite um número inteiro válido.")

# Algoritmos de Ordenação
def merge_sort(lista, chave):
    """Merge Sort estável: O(n log n)."""
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita  = merge_sort(lista[meio:], chave)
    return merge(esquerda, direita, chave)

def merge(esq, dir, chave):
    """Intercalação sem pop(0), usando ponteiros (eficiente)."""
    i = j = 0
    res = []
    while i < len(esq) and j < len(dir):
        if esq[i][chave] <= dir[j][chave]:
            res.append(esq[i]); i += 1
        else:
            res.append(dir[j]); j += 1
    res.extend(esq[i:])
    res.extend(dir[j:])
    return res

def quick_sort(lista, chave):
    """Quick Sort com pivô aleatório: médio O(n log n)."""
    if len(lista) <= 1:
        return lista
    pivo = random.choice(lista)
    menores = [x for x in lista if x is not pivo and x[chave] <= pivo[chave]]
    maiores = [x for x in lista if x is not pivo and x[chave] >  pivo[chave]]
    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

# Algoritmos de Busca
def busca_sequencial(lista, nome):
    alvo = nome.lower()
    for item in lista:
        if item["nome"].lower() == alvo:
            return item
    return None

def busca_binaria(lista_ordenada_por_nome, nome):
    """Pré-condição: lista ordenada por item['nome'].lower()."""
    alvo = nome.lower()
    inicio, fim = 0, len(lista_ordenada_por_nome) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = lista_ordenada_por_nome[meio]["nome"].lower()
        if nome_meio == alvo:
            return lista_ordenada_por_nome[meio]
        elif nome_meio < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

# Ações de Estoque
def cadastro_item():
    limpa_tela()
    print("📦 Cadastro de Insumo\n")
    nome = input_nao_vazio("Nome do insumo: ")
    quantidade = input_inteiro("Quantidade inicial: ", minimo=0)
    validade = input_nao_vazio("Validade (AAAA-MM-DD): ")
    estoque.append({"nome": nome, "quantidade": quantidade, "validade": validade})
    print(f"✅ {nome} cadastrado com sucesso!")
    pausa()

def listar_item_cadastrados():
    limpa_tela()
    print("🗂️  Itens Cadastrados\n")
    if not estoque:
        print("⚠️  Nenhum insumo cadastrado.")
    else:
        for item in estoque:
            print(f"- {item['nome']} | Qtd: {item['quantidade']} | Validade: {item['validade']}")
    pausa()

def registrar_consumo():
    limpa_tela()
    print("🧪 Registrar Consumo de Insumo\n")
    nome = input_nao_vazio("Nome do insumo consumido: ")
    item = busca_sequencial(estoque, nome)
    if item:
        if item["quantidade"] > 0:
            item["quantidade"] -= 1
            fila_consumo.append(nome)   
            pilha_consumo.append(nome)  
            print(f"✅ Consumo de {nome} registrado! Quantidade atual: {item['quantidade']}")
        else:
            print("⚠️  Estoque insuficiente!")
    else:
        print("⚠️  Insumo não encontrado!")
    pausa()

def menu_busca():
    limpa_tela()
    print("🔎 Buscar Insumo por Nome\n")
    nome = input_nao_vazio("Digite o nome do insumo: ")
    print("\n1) Busca Sequencial\n2) Busca Binária (lista ordenada por nome)")
    escolha = forca_opcao(['1','2'], "-> ")
    if escolha == "1":
        resultado = busca_sequencial(estoque, nome)
    else:
        lista_ordenada = sorted(estoque, key=lambda x: x["nome"].lower())
        resultado = busca_binaria(lista_ordenada, nome)

    if resultado:
        print(f"\n✅ Encontrado: {resultado}")
    else:
        print("\n⚠️  Insumo não encontrado.")
    pausa()

def menu_ordenacao():
    limpa_tela()
    print("↕️  Ordenar Estoque\n")
    print("1) Merge Sort por QUANTIDADE\n2) Quick Sort por VALIDADE")
    escolha = forca_opcao(['1','2'], "-> ")
    if escolha == "1":
        ordenado = merge_sort(estoque, "quantidade")
    else:
        ordenado = quick_sort(estoque, "validade")

    print("\n📋 Resultado da Ordenação:\n")
    for item in ordenado:
        print(f"- {item['nome']} | Qtd: {item['quantidade']} | Validade: {item['validade']}")
    pausa()

def relatorio_estoque():
    limpa_tela()
    print("📊 Relatório de Consumo\n")
    print("📌 Fila (ordem cronológica de consumo):")
    print(list(fila_consumo))
    print("\n📌 Pilha (últimos consumos primeiro):")
    print(list(reversed(pilha_consumo)))
    pausa()


# Loop principal 
def main_estoque():
    while True:
        limpa_tela()
        print("-=" * 20)
        print('''
        1) Cadastrar item
        2) Listar itens
        3) Registrar consumo
        4) Buscar item
        5) Ordenar estoque
        6) Relatório de consumo
        0) Sair
        ''')
        print("-=" * 20 + "\n")

        escolha = forca_opcao(['1','2','3','4','5','6','0'], 'Qual opção você deseja acessar?\n-> ')
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
        elif escolha == "6":
            relatorio_estoque()
        elif escolha == "0":
            print("👋 Volte sempre! =)")
            break



# Execução
if __name__ == "__main__":
    main_estoque()

# 🏥 Solução DASA - Dynamic Programming

## 👩‍🎓 Alunos

| Nome                                   | RM       |
|----------------------------------------|----------|
| Bruna Costa Candeias                   | 558938   |
| Carlos Eduardo dos Santos Ribeiro Filho| 556785   |
| Lucas Derenze Simidu                   | 555931   |
| Marcos Vinícius da Silva Costa         | 555490   |
| Sofia Fernandes                        | 554873   |


## 🎯 Desafio Escolhido

**1ª Forma: Controle de Estoque com Estruturas de Dados e Programação Dinâmica**

---

## 🧠 Objetivo da Solução

Desenvolver um sistema de gerenciamento de estoque que simula a operação de uma unidade hospitalar, permitindo o cadastro, controle, reposição e análise de itens armazenados, com foco em performance e eficiência.  
A aplicação implementa técnicas de **programação dinâmica com memorização (_memoization_)** para otimizar cálculos recorrentes sobre os dados.

---

## 🧰 Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3  
- **Estruturas:** Dicionários, Listas, Deque (fila), Listas como pilha  
- **Técnicas de Dynamic Programming:**  
  - ✅ Função recursiva com memorização para cálculo do estoque total (`estoque_total`)  

### 📦 Estruturas de Dados no Estoque
- **Fila (FIFO)**: usada para registrar o consumo dos insumos em ordem cronológica, permitindo **auditoria** e relatórios de histórico.  
- **Pilha (LIFO)**: registra os últimos consumos no topo, permitindo análise rápida e até “desfazer” o último consumo.  

### 🔎 Estruturas de Busca
- **Busca Sequencial**: percorre a lista inteira, útil para estoques pequenos ou quando não há ordenação.  
- **Busca Binária**: aplicada em listas ordenadas por nome, garantindo **rapidez e eficiência** em estoques grandes (O(log n)).  

### ↕️ Algoritmos de Ordenação
- **Merge Sort (por quantidade)**: estável, garante O(n log n) e é usado para identificar insumos com menor quantidade → **apoio na reposição**.  
- **Quick Sort (por validade)**: rápido na prática, organiza os insumos pela data de validade → aplicação da regra **FEFO (First Expire, First Out)**, evitando desperdícios.  

---

## 🚀 Impacto na Solução
- **Controle inteligente**: combina pilha e fila para rastrear consumos sob diferentes perspectivas.  
- **Agilidade**: buscas rápidas tornam o sistema eficiente em estoques grandes.  
- **Decisão estratégica**: ordenações ajudam a prever faltas de insumos e evitar vencimentos.  
- **Confiabilidade**: os algoritmos asseguram que o sistema funcione de forma organizada e auditável, fundamental em ambientes hospitalares.

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em seu sistema.  
2. No terminal ou prompt de comando, execute:

```bash
python main.py



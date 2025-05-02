# 💰 Simulador de Investimento com IOF e IR

Este projeto contém uma implementação em Python para calcular o rendimento de um investimento considerando os impostos aplicáveis: **IOF (Imposto sobre Operações Financeiras)** e **IR (Imposto de Renda)**. A simulação é baseada em uma taxa anual fixa e leva em conta os períodos de aplicação para determinar a rentabilidade líquida.

## 📜 Descrição

O código simula um sistema de cálculo de rendimento a partir de um valor inicial investido, aplicando tributações conforme a tabela de impostos vigente. O sistema considera:
- A **Taxa Anual de 14,15%** (equivalente a aproximadamente **1,18% ao mês**).
- **Imposto sobre Operações Financeiras (IOF)**: Aplicado conforme o número de dias de investimento (se menor que 30 dias).
- **Imposto de Renda (IR)**: Aplicado conforme o período de investimento.

O objetivo principal é fornecer ao usuário um valor estimado de rendimento líquido após aplicação das tributações.

---

## 📌 Estrutura do Código

### 🔹 Constantes do Sistema
O código define a taxa anual e calcula a taxa mensal automaticamente:
```python
TAXA_ANUAL = 14.15
TAXA_MESES = TAXA_ANUAL / 12
```

### 🔹 Classe bcolors
Define cores para saída no terminal, facilitando a legibilidade das mensagens para o usuário.

### 🔹 Classe IOF
Responsável pelo cálculo do desconto de IOF, seguindo uma tabela predefinida com valores de alíquota de acordo com o número de dias.

### 🔹 Classe IR
Define a alíquota do Imposto de Renda conforme o tempo de aplicação:

- Até 180 dias ➝ 22,5%
- Entre 181 e 360 dias ➝ 20%
- Entre 361 e 720 dias ➝ 17,5%
- Acima de 720 dias ➝ 15%

### 🔹 Classe Investimento
Esta classe permite ao usuário inserir os dados do investimento (valor e tempo de aplicação) e calcula o rendimento líquido após descontos de IOF e IR.

#### 🔸 Validação dos Dados
Antes de prosseguir com os cálculos, o código verifica se os valores inseridos são numéricos e positivos:

```
python
if not isinstance(valor, float):
    raise TypeError("Valor inserido inválido!")
```

#### 🔸 Cálculo do Rendimento
A fórmula básica de cálculo do rendimento bruto é:

```
python
rendimento_bruto = valor * (TAXA_MESES * (tempo_aplicacao / 30))
```
Após isso, a função aplica as deduções de IOF e IR:

```
python
rendimento_liquido = IOF.desconto(tempo_aplicacao, rendimento_bruto)
rendimento_liquido = IR.desconto(tempo_aplicacao, rendimento_liquido)
```

## 🚀 Como Executar

1. Instale Python 3 no seu sistema.
2. Copie o código para um arquivo investimento.py.
3. Execute o script com:

```bash
python investimento.py
```

4. Insira o valor do investimento e o período de aplicação (em dias).
5. Veja o rendimento líquido calculado no terminal.

## 📊 Exemplo de Uso

```python
# Executando o programa:
Valor de investimento: R$1000
Tempo da aplicação (dias): 200
```
Saída esperada:

```
Seu rendimento é de: R$174.20
```

## 🛠 Melhorias Possíveis:

- Adicionar suporte para diferentes tipos de investimento e taxas variáveis.
- Criar uma interface gráfica para facilitar a interação.
- Integrar com APIs financeiras para taxas atualizadas em tempo real.

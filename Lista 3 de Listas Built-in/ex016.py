""" Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados."""

vendas = []
while True:
    venda = float(input("Indique a venda brutas da semana do vendedor (0=parar o programa): $ "))
    if venda == 0:
        break
    vendas.append(venda)


contadores = [0] * 9

for venda in vendas:
    salario = 200 + 0.09 * venda
    indice = int((salario - 200) // 100)
    indice = min(indice, 8)
    contadores[indice] += 1

print(f'\n{"Faixa salariais":<20}{"Número de vendedores"}')
for i, contagem in enumerate(contadores):
    if i == 8:
        print(f"$1000 em diante: {contagem:>6}")
    else:
        print(f"${200 + (i * 100)} - ${299 + (i * 100)}: {contagem:>10}")
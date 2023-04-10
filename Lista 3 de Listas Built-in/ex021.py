""" 21) Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
 Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
 litro de combustível. Calcule e mostre:
a - O modelo do carro mais econômico;
b - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer
uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa."""

def litros_distancia(km, distancia=1000):
    return distancia/km

modelos = []
consumo = []
litros = []

print("Comparativo de Consumo de Combustível")
for i in range(1,6):
    print(f"Veículo {i}")
    modelos.append(str(input("Nome: ")))
    consumo.append(float(input("Km por litro: ")))

for c in consumo:
    litros.append(litros_distancia(c))

print("\nRelatório final:")
cont = 1
for m, c, l in zip(modelos, consumo, litros):
    print(f"{cont} - {m:<10} - {c:>5} - {l:.2f} litros - R${2.25 * l:.2f}")
    cont += 1

for m, l in zip(modelos, litros):
    if l == min(litros):
        print(f"\nO menor consumo é do {m}")
        
    



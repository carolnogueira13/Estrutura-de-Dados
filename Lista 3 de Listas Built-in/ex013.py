# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

media_de_temperaturas = []
soma_das_temp = 0

for i in range(12):
    temp = float(input(f"Média de temperatura do mês {i+1}: "))
    soma_das_temp += temp
    media_de_temperaturas.append(temp)

media_de_temperaturas_anual = soma_das_temp/12
print(f"Média de temperatura anual: {media_de_temperaturas_anual:.2f}ºC")

print("Meses acima da média de temperatura anual:")
meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto',
        9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
for i, media in enumerate(media_de_temperaturas):
    if media > media_de_temperaturas_anual:
        print(f"{i + 1} - {meses[i+1]}: {media}ºC") 

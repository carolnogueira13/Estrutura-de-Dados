# 19) Você foi contratado para desenvolver um programa que leia o resultado da enquete de sistemas operacionais de
# computadores e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0,
# que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os
# valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente
# informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.


def porcentagem(votos, total_de_votos):
    return (100 * votos) / total_de_votos


votos = []

print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")

while True:
    voto = int(input("""
1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - Mac OS
6 - Outros
Sua opção (0=fim): """))
    if voto == 0:
        break
    if voto not in (1, 2, 3, 4, 5, 6):
        print("Informe um valor entre 1 e 6 ou 0 para sair!")
        continue
    votos.append(voto)

print("\nResultado da votação:")

porcentagens = []
for i in range(1, 7):
    porcentagens.append(porcentagem(votos.count(i), len(votos)))

print(f"\n{'Sistema operacional':<30}{'Votos':<10}{'Porcentagem':<10}")
print("-" * 60)
sistemas = {1: "Windows Server", 2: "Unix", 3: "Linux", 4: "Netware", 5: "Mac OS", 6: "Outro"}
for i, por in enumerate(porcentagens):
    if por != 0:
        print(f"{(sistemas[i + 1]):<30} {votos.count(i + 1):<10} {por:<10.2f}%")
print("-" * 60)
print(f"{'Total':<30}{len(votos):<10}")

for i, por in enumerate(porcentagens):
    if por == max(porcentagens):
        print(
            f"\nO sistema operacional mais votado foi o {sistemas[i + 1]}, com {votos.count(i + 1):.2f} votos, correspondendo a {por}% do total de votos ")

''' 18) Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa,
que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este
programa, utilizando a linguagem de programação python. Para computar cada voto, a telefonista digitará um número,
entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação
foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo,
mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação,
o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos
dados a ele.'''


def porcentagem(votos, total_de_votos):
    return (100 * votos) / total_de_votos


votos = []

print("Enquete: Quem foi o melhor jogador?")

while True:
    voto = int(input("Número do jogador (0=fim): "))
    if voto == 0:
        break
    if voto > 23 or voto < 0:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        continue
    votos.append(voto)


porcentagens = []
for i in range(1,24):
    porcentagens.append(porcentagem(votos.count(i), len(votos)))


# Cria o cabeçalho do relatório
cabecalho = "Resultado da votação:\n"
cabecalho += f"\nForam computados {len(votos)} votos\n"
print(cabecalho)

# Cria o corpo do relatório
corpo = f'\n{"Jogador":<10}{"Votos":<10}{"Porcentagem":<10}\n'
for i, por in enumerate(porcentagens):
    if por != 0:
        corpo += f"{(i + 1):<10} {votos.count(i+1):<10} {por:<10.2f}%\n"
print(corpo)

# Cria o rodapé do relatório
rodape = ''
for i, por in enumerate(porcentagens):
    if por == max(porcentagens):
        rodape += f"O melhor jogador foi o número {i+1}, com {votos.count(i+1)} votos, correspondendo a {por}% do total de votos "
print(rodape)


with open('relatorio_jogadores.txt', 'w') as arquivo:
    arquivo.write(cabecalho + corpo + rodape)




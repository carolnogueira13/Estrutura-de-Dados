# 22) Defeitos em mouses 

def porcentagem(defeit, total_de_defeitos):
    return (100 * defeit) / total_de_defeitos

defeitos = []
identificacao_defeitos = {1: 'Necessita de esfera', 2: 'Necessita de limpeza',
                          3: 'Necessita de troca de cabo ou conector', 4: 'Quebrado ou inutilizado'}
i = 1
while True:
    print(f"Mouse {i}")
    defeito = int(input(f"""1 - {identificacao_defeitos[1]}
2 - {identificacao_defeitos[2]}
3 - {identificacao_defeitos[3]}
4 - {identificacao_defeitos[4]}
Escolha sua opção (0 - para o programa): """))
    if defeito == 0:
        break
    if defeito not in (1, 2, 3, 4):
        print("Escolha uma opção válida de 1 a 4 ou 0 para parar o programa")
        continue
    defeitos.append(defeito)
    i += 1

porcentagens = []
for i in range(1,5):
    porcentagens.append(porcentagem(defeitos.count(i), len(defeitos)))

print(f"\nQuantidade de mouses: {len(defeitos)}")

print(f"\n{'Situação':<44}{'Quantidade':<15}{'Percentual':<10}")
for i, por in enumerate(porcentagens):
    print(f"{i+1} - {(identificacao_defeitos[i+1]):<40} {defeitos.count(i+1):<15} {por:<10.2f}%")


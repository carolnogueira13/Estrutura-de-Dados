# 7) Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva
# que inverta ordem dos elementos presentes no vetor.

def inverte_vetor(vetor: list, inicio: int, fim: int) -> list:
    if inicio >= fim:
        return
    temp = vetor[inicio]
    vetor[inicio] = vetor[fim]
    vetor[fim] = temp
    inverte_vetor(vetor, inicio + 1, fim - 1)


if __name__ == "__main__":
    vetor = [float(i) for i in range(100)]  # cria um vetor de 100 posições de 0.00 a 99.00
    print(f"Vetor original = {vetor}")
    inverte_vetor(vetor, 0, len(vetor) - 1)
    print(f"Vetor invertido: {vetor}")

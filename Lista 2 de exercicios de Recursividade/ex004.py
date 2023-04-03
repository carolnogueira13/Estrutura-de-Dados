# 4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

# 1ª forma:
def soma_vetor(vetor: list, n: int) -> int:
    if n == 0:
        return 0
    return vetor[n - 1] + soma_vetor(vetor, n - 1)


if __name__ == "__main__":
    vetor = [1, 2, 3, 4]
    print(f"A soma dos elementos do vetor {vetor} é {soma_vetor(vetor, len(vetor))}")


# 2ª forma:

def somaLista(lista: list) -> int:
    if not lista:
        return 0
    return lista[0] + somaLista(lista[1:])  # tira o primeiro termo da lista a cada recursão


if __name__ == "__main__":
    vetor = [1, 2, 3, 4]
    print(f"A soma dos elementos do vetor {vetor} é {somaLista(vetor)}")

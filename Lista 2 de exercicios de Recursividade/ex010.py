# 10) Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por
# exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def contagem(n: int, k: int) -> int:
    if n == 0:
        return 0
    elif n % 10 == k:
        return 1 + contagem(n // 10, k)
    else:
        return contagem(n // 10, k)


if __name__ == "__main__":
    n = 7620021192
    k = 2
    print(f"O dígito {k} aparece {contagem(n, k)} vezes no número {n}")

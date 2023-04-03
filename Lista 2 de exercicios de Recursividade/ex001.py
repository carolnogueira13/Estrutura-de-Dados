# 1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.

def fatorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    n = int(input("Digite um número: "))
    fat = fatorial(n)
    print(f"O fatorial de {n} é {fat}")


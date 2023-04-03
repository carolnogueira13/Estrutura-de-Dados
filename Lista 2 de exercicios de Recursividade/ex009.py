# 9) Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. (
# Igual a questão 05)

def somatorio(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + somatorio(n - 1)


if __name__ == "__main__":
    n = int(input("Digite um número inteiro positivo: "))
    print(f"O somatório de 1 a {n} é {somatorio(n)}")

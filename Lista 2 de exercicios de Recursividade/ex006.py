# 6) Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule
# k^n . Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir
# o resultado da chamada da função.

def potencia(n1: int,n2: int) -> int:
    if n2 == 0:
        return 1
    else:
        return n1 * potencia(n1,n2-1)


if __name__ == "__main__":
    k = int(input("Valor de k (base): "))
    n = int(input("Valor de n (expoente): "))
    pot = potencia(k,n)
    print(f"O resultado de {k} elevado a {n} = {pot}")
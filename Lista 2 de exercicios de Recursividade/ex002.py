# 2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta
# sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...


def fibonacci_sequence(n: int) -> int:
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


if __name__ == "__main__":
    n = int(input("Deseja retornar qual o terma da sequência de Fibonacci: "))
    print(f"O {n}º termo da sequência de Fibonacci é {fibonacci_sequence(n - 1)}")
    print("E a sequência completa até esse termo é: ", end="")
    for i in range(n):
        print(fibonacci_sequence(i), end=" ")
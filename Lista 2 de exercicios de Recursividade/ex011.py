# 11) A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo
# recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros.

def Multip_Rec(n1: int, n2: int) -> int:
    if n2 == 0:
        return 0
    else:
        return n1 + Multip_Rec(n1, n2 - 1)


if __name__ == "__main__":
    x = 2
    y = 23
    multip = Multip_Rec(x, y)
    print(f"O resultado da multiplicação de {x} * {y} = {multip}")

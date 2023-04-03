# 8) O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y. Escreva uma função
# recursiva mdc em python, que retorna o máximo divisor comum de x e y. O mdc de x e y é definido como segue: se y é
# igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto.

def mdc(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return mdc(y, x % y)


if __name__ == "__main__":
    x = int(input("Insira um número: "))
    y = int(input("Insira um número: "))
    print(f"O máximo divisor comum de {x} e {y} é {mdc(x, y)}")

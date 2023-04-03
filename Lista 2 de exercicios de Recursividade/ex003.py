# 3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321

# 1ª forma (transformado em lista de strings):
def inverte_numero_lista(lista: list, inicio: int, fim: int) -> list:
    if inicio >= fim:
        return
    temp = lista[inicio]
    lista[inicio] = lista[fim]
    lista[fim] = temp
    inverte_numero_lista(lista, inicio + 1, fim - 1)


if __name__ == "__main__":
    numero = 123
    lista = list(str(numero))
    inverte_numero_lista(lista, 0, len(lista) - 1)
    numero_invertido = int(''.join(lista))
    print(numero_invertido)


# 2ª forma (usando o slice):
def inverte(n: int) -> int:
    n = str(n)
    if n == '':
        return n
    return n[-1] + inverte(n[:-1])


if __name__ == "__main__":
    numero = 123
    numero_invertido = inverte(numero)
    print(numero_invertido)


# 3ª forma (usando módulo):
def inverte_numero(n: int, temp=0) -> int:
    if n == 0:
        return temp
    else:
        resto = n % 10
        temp = temp * 10 + resto
        return inverte_numero(n // 10, temp)


if __name__ == "__main__":
    numero = 123
    numero_invertido = inverte_numero(numero)
    print(numero_invertido)


# 20) Programa de abono de salários 

def abono(salario):
    if salario < 1000:
        return 100.00
    else:
        return salario * 0.2


salarios = []
valor_minimo = 0

print("Projeção de gastos com abono")

while True:
    sal = float(input("Salário: "))
    if sal == 0:
        break
    salarios.append(sal)


abonos = []
for salario in salarios:
    if salario < 1000:
        valor_minimo += 1
    abonos.append(abono(salario))

print(f"\n{'Salario':<12}{'- Abono':<10}")
for salario, abono in zip(salarios, abonos):
    print(f"{f'R${salario:<10.2f}'}{f'- ${abono:<10.2f}'}")

print(f"\nForam processados {len(salarios)} colaboradores")
print(f"Total gasto com abonos: R${sum(abonos):.2f}")
print(f"Valor mínimo pago a {valor_minimo} colaboradores")
print(f"Maior valor de abono pago: R${max(abonos):.2f}")

    
    




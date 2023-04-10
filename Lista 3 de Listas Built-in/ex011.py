# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

import random
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for i in range(10):
    vetor1.append(random.randrange(10))
    vetor2.append(random.randrange(10))
    vetor3.append(random.randrange(10))
    

for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print(f"O vetor 1 formado é: {vetor1}")
print(f"O vetor 2 formado é: {vetor2}")
print(f"O vetor 3 formado é: {vetor3}")
print(f"O vetor 4 intercalado formadao é: {vetor4}")
import matplotlib
import numpy as np
from random import choice,randrange,randint
from math import pow

# print(matplotlib.__version__)

# Atividade 3
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print(f'Escolhe um número aleatorio da lista: {choice(lista)}')
print('-----------------------')
#  Atividade 4
print(f'Número aleatorio menor que 100 : {randrange(1,100)}')
print('-----------------------')
# Atividade 5
base = int(input('Digite o primeiro número:'))
expoente = int(input('Digite o segundo número:'))
print(f"{base} elevado a {expoente} é igual a {pow(base, expoente)}")
print('-----------------------')
# Atividade 6
n = int(input("Digite o nº de participantes do sorteio: "))
print(f"O número sorteado foi {randint(1, n)}")

'''
9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, 
    identificando quais resultaram em um número inteiro. A lista é a seguinte:
    
    numeros = [2, 8, 15, 23, 91, 112, 256]

    No final, informe quais números possuem raízes inteiras e seus respectivos valores.

    Dica: use a comparação entre a divisão inteira (//) 
            da raiz por 1 com o valor da raiz para verificar se o número é inteiro. Por exemplo:
    
    num = 1.5
    num_2 = 2
    print(f'{num} é inteiro? :', num // 1 == num)
    print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)

    1.5 é inteiro? : False
    2 é inteiro? : True
'''
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]
# iniciando uma lista vazia para receber as raízes
raiz = []

# laço for para calcular cada raiz da lista de números e adicionar a lista raiz
for numero in numeros:
  raiz.append(sqrt(numero))

# laço for para ler a lista raiz e exibir um texto só quando a raiz for um valor inteiro 
for i in range(len(raiz)):
  # condição para testar se um número é inteiro (Ex: 2.5 // 1 = 2 ... 2 != 2.5)
  if raiz[i] // 1 == raiz[i]:
    print(f"O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}")
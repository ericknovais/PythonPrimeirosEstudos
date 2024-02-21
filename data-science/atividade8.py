'''
    8. Para diversificar e atrair novos(as) clientes, 
        uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". 
        Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor 
        a salada de frutas da pessoa cliente. 
        Crie o código que faça essa seleção aleatória de acordo com a lista abaixo
'''

from random import choices

# Lista das frutas disponíveis
frutas = ["maçã", "banana", "uva", "pêra","manga", "coco", 
          "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

# Gerando uma lista com a escolha aleatoria de 3 frutas 
salada = choices(frutas, k=3)

# Imprimindo os itens da lista de frutas gerada
print(f"A salada surpresa é: {salada[0]}, {salada[1]} e {salada[2]}")
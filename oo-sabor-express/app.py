from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça','gourmet')
restaurante_bk = Restaurante('bk','fostfood')
restaurante_mexicano = Restaurante('MexiCuzinho', 'Mexicano') 
restaurante_bk.alternar_estado()

bebida_melancia = Bebida('Melancia', 5.0, 'Grande')
prato_big_king = Prato('Big King', 19,90, 'Hamburg da casa')

# restaurante_bk.receber_avalicao('Erick', 7)
# restaurante_bk.receber_avalicao('Roberta', 5)
# restaurante_bk.receber_avalicao('Jamal', 8)

def main():
    pass

if __name__ == '__main__':
    main()
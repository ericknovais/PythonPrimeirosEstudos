from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça','gourmet')
restaurante_bk = Restaurante('bk','fostfood')
restaurante_mexicano = Restaurante('MexiCuzinho', 'Mexicano') 
restaurante_bk.alternar_estado()

bebida_melancia = Bebida('Melancia',5.0,'Grande')
bebida_melancia.aplicar_desconto()
prato_big_king = Prato('Big King',19.90,'Hamburg da casa')
prato_big_king.aplicar_desconto()

restaurante_bk.adicionar_no_cardapio(bebida_melancia)
restaurante_bk.adicionar_no_cardapio(prato_big_king)

restaurante_bk.receber_avalicao('Erick', 7)
restaurante_bk.receber_avalicao('Roberta', 5)
restaurante_bk.receber_avalicao('Jamal', 8)

def main():
    restaurante_bk.exibir_cardapio

if __name__ == '__main__':
    main()
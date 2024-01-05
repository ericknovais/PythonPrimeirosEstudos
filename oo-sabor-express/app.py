from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_bk = Restaurante('bk','fostfood')
restaurante_mexicano = Restaurante('MexiCuzinho', 'Mexicano') 
restaurante_bk.alternar_estado()

restaurante_bk.receber_avalicao('Erick', 7)
restaurante_bk.receber_avalicao('Roberta', 5)
restaurante_bk.receber_avalicao('Jamal', 8)

def main():
    Restaurante.listar_restaurantres()

if __name__ == '__main__':
    main()
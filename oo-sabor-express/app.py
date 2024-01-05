from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_bk = Restaurante('bk','fostfood')
restaurante_mexicano = Restaurante('MexiCuzinho', 'Mexicano') 
restaurante_bk.alternar_estado()

def main():
    Restaurante.listar_restaurantres()

if __name__ == '__main__':
    main()
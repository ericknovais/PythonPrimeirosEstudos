from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida:
    def __init__(self, nome, preco, tamanho):
        super().__init__(self, nome, preco)
        self._tamanho = tamanho
    
    def __str__(self):
       """Retorna uma representação em string da Bebida."""
       return f'{self._nome}'
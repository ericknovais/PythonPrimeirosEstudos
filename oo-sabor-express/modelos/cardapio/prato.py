from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(self, nome, preco)
        self._descricao = descricao

    def __str__(self):
       """Retorna uma representação em string do Prato."""
       return f'{self._nome}'
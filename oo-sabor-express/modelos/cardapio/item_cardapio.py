class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def __str__(self):
       """Retorna uma representação em string do Item Cardapio."""
       return f'{self._nome}'
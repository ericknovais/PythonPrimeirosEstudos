class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
       return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantres(cls):
        print(f'{'Nome restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for  restaurante in cls.restaurantes:
            print (f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
restaurante_bk = Restaurante('BK','FastFood')
restaurante_bk.alternar_estado()
restaurante_dog = Restaurante('MosterDog','FastFood')

Restaurante.listar_restaurantres()
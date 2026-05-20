from pedido import Pedido
from rich import print 
from rich.panel import Panel

def linha():
    print()
    print('-' * 24)
    print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        return f'{self.nome:<25}  - R${self.preco:>6.2f}'
    print()
    
    
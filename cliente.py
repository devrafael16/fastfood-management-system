from pedido import Pedido
from produto import Produto

def linha():
    print()
    print('-' * 24)
    print()

class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def resumo(self):
        print(f'Cliente: {self.nome}')

        for i, pedido in enumerate(self.pedidos, start=1):
            print(f'\nPedido {i}:')
            pedido.listar_produtos()
            print(f'Total: R${pedido.total():.2f}')
            print('-' * 30)
        print(f'Valor total dos pedidos: R${sum(pedido.total() for pedido in self.pedidos):.2f}')

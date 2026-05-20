from rich import print 
from rich.panel import Panel

def linha():
    print()
    print('-' * 24)
    print()

class Pedido:
    def __init__(self):
        self.produtos = []
        self.status = 'Aberto'

    def remover_ultimo_produto(self):
        if self.produtos:
            produto_removido = self.produtos.pop()
            return produto_removido
        return None
    print()

    def definir_status(self, status):
        self.status = status
        return self.status
    print()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
    print()
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(f'- {produto.mostrar()}')
            print()

    def pedido_vazio(self):
        return len(self.produtos) == 0
    print()
    
    def remover_produto_por_indice(self, indice):
        if 0 <= indice < len(self.produtos):
            return self.produtos.pop(indice)
        return None
    print()


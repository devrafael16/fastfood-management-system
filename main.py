from cliente import Cliente
from produto import Produto
from pedido import Pedido
from sistema_pedido import *
import json
import os

def linha():
    print()
    print('-' * 24)
    print()


def main():

    while True:
        print(f'{"FAST FOOD":=^30}')
        print('1 - Novo pedido')
        print('2 - Ver pedidos salvos')
        print('0 - Sair')
        print('=' * 30)
        menu = input('Digite a opção desejada: ')
        if menu == '0':
            print('Obrigado pela preferência. Volte sempre!')
            break
        elif menu == '1':
            novo_pedido()
        elif menu == '2':
            ver_pedido()
        else:
            print('Opção inválida!')
            




if __name__ == "__main__":
    main()


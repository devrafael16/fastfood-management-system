from cliente import Cliente
from produto import Produto
from pedido import Pedido
from sistema_pedido import *
import json
import os
from rich import print
from rich.panel import Panel
from rich.console import Console

def linha():
    print()
    print('=' * 24)
    print()

console = Console()

def main():
    """Exibe o menu principal do sistema"""

    while True:
        console.print(Panel.fit(f'[bold yellow]{" FAST FOOD ":=^30}[/]', border_style='yellow'))
        console.print('[1] - Novo pedido', style='cyan')
        console.print('[2] - Ver pedidos salvos', style='cyan')
        console.print('[3] - Atualizar status', style='cyan')
        console.print('[4] - Excluir pedido', style='cyan')
        console.print('[0] - Sair', style='cyan')
        console.rule(style='yellow')
        menu = input('Digite a opção desejada: ')
        print()
        if menu == '0':
            print('[green]Obrigado pela preferência. Volte sempre![/]')
            console.rule(style='yellow')
            break
        elif menu == '1':
            novo_pedido()
        elif menu == '2':
            ver_pedido()
        elif menu == '3':
            atualizar_status()
        elif menu == '4':
            excluir_pedido()
        else:
            print('Opção inválida!')
            




if __name__ == "__main__":
    main()


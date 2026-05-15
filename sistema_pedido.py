from produto import Produto
from cliente import Cliente
from pedido import Pedido
import os
import json

def linha():
    print()
    print('-' * 24)
    print()

def novo_pedido():
    nome = input('Digite seu nome: ')
    cliente1 = Cliente(nome)


    cardapio = [
        Produto('Hambúrguer', 15.00),
        Produto('Pizza', 45.00),
        Produto('Coxinha', 8.00),
        Produto('Pastel', 12.00),
        Produto('Sorvete', 15.00),
        Produto('Coca-cola', 12.00),
        Produto('Guaraná', 10.00)
    ]
    pedido_atual = Pedido()
    cliente1.adicionar_pedido(pedido_atual)
    
    print()
    print(f'Bem-vindo {cliente1.nome}!'.center(24))

    while True:
    
        linha()
        print('Seu pedido atual:'.center(24))
        if pedido_atual.pedido_vazio():
            print('Pedido vazio.'.center(24))

        else:
            pedido_atual.listar_produtos()
            print(f'Status do pedido: {pedido_atual.status}')
            print(f'Total parcial: R${pedido_atual.total():.2f}')
            print(f'Total de itens: {len(pedido_atual.produtos)}')
            linha()
        print('Cardápio:'.center(24))
        linha()
        for i, produto in enumerate(cardapio, start=1):
            print(f'{i} - {produto.mostrar()}')
        print('-1 - Remover último item do pedido.')
        print('-2 - Remover item específico.')
        print('00 - Finalizar pedido')
        linha()

        escolha = input('Digite o número do item que deseja adicionar ao pedido: ')

        if escolha == '00':
            if pedido_atual.pedido_vazio():
                print('Pedido vazio.')
                continue
            
            pedido_atual.definir_status('Finalizado')

            print()
            print('Resumo do pedido:')
            pedido_atual.listar_produtos()
            print(f'Status do pedido: {pedido_atual.status}')
            print(f'Total de itens: {len(pedido_atual.produtos)}')
            print(f'Total: R${pedido_atual.total():.2f}')
            produtos_json = []
            for produto in pedido_atual.produtos:
                lista = {"nome": produto.nome, "preco": produto.preco}
                produtos_json.append(lista)  
            pedido_json = {
                'cliente': cliente1.nome,
                'status': pedido_atual.status,
                'produtos': produtos_json,
                'total': pedido_atual.total()
            }
            nome_arquivo = 'Pedido' + cliente1.nome + '.json'
            caminho_pasta = os.path.dirname(__file__)
            pasta_pedidos = os.path.join(caminho_pasta, 'pedidos')
            if not os.path.exists(pasta_pedidos):
                os.mkdir(pasta_pedidos)
            caminho_arquivo = os.path.join(pasta_pedidos, nome_arquivo)
            
            with open(caminho_arquivo, 'w') as arquivo:
                json.dump(pedido_json, arquivo, indent=4)
        
            linha()
            break

        elif escolha == '-1':
            produto = pedido_atual.remover_ultimo_produto()

            if produto:
                print(f'{produto.nome} removido do pedido.')
            else:
                print('Pedido vazio.')

            linha()
        
        elif escolha == '-2':
            if pedido_atual.pedido_vazio():
                print('Pedido vazio')
            else:
                for i, produto in enumerate(pedido_atual.produtos, start=1):
                    print(f'{i} - {produto.mostrar()}')
                numero_do_item = int(input('Qual item deseja remover: '))
                produto_removido = pedido_atual.remover_produto_por_indice(numero_do_item -1)
                if produto_removido:
                    print(f'{produto_removido.nome} removido do pedido.')
                else:
                    print('Item inválido')
            


        elif escolha.isdigit():
            escolha = int(escolha)

            if 1 <= escolha <= len(cardapio):
                produto = cardapio[escolha - 1]
                pedido_atual.adicionar_produto(produto)
                print(f'{produto.nome} adicionado ao pedido.')
                if pedido_atual.status != 'Em andamento':
                    pedido_atual.definir_status('Em andamento')
                print(f'Status do pedido: {pedido_atual.status}')
                linha()
            else:
                print('Opção inválida.')
                
        else:
            print('Digite uma opção válida.')
        
def ver_pedido():
    caminho_pasta = os.path.dirname(__file__)
    pasta_pedidos = os.path.join(caminho_pasta, 'pedidos')
    if os.path.exists(pasta_pedidos):
        pasta = os.listdir(pasta_pedidos)
        if not pasta:
            print('Nenhum pedido salvo.')
            return
    
        for i, valor in enumerate(pasta):
            print(f'{i + 1} - {valor}') 
            print()
        escolha_arquivo = input('Escolha um pedido da lista: ')
        if escolha_arquivo.isdigit():
            escolha_arquivo = int(escolha_arquivo)
            if 1 <= escolha_arquivo <= len(pasta):
                escolha = pasta[escolha_arquivo - 1]
                arquivo_pasta = os.path.join(pasta_pedidos, escolha)
                with open(arquivo_pasta, 'r') as arquivo:
                    pedido = json.load(arquivo)

                print('=' * 30)
                print(f"Cliente: {pedido['cliente']}")
                print(f"Status: {pedido['status']}")
                for i,produto in enumerate(pedido['produtos'], start=1):
                    print(f"{i} - {produto['nome']} - R${produto['preco']:.2f}")
                print(f"Total: {pedido['total']:.2f}")
                print('=' * 30)
    else:
        print('Nenhum pedido encontrado')
        
            
        
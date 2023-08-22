from cardapio import Cardapio
from utils import Utils
class Carrinho:
    cardapio = Cardapio.obter_cardapio()
    cardapio_completo = Cardapio.obter_cardapio_inteiro()
    def __init__(self):
        self.lista_de_pedidos = []
        self.valor_total_compra = 0

    @staticmethod
    def escolher_item_cardapio():
        codigo_do_pedido = input('------------------------------------------------------ \n'
                                 'Digite o código do produto desejado: ').lower()
        return codigo_do_pedido

    def add_to_cart(self, codigo_do_pedido):
        if codigo_do_pedido in Carrinho.cardapio:
            existir_sanduiche_na_lista = Utils.encontrar_item_por_chave('sanduiche', self.lista_de_pedidos)
            existir_cafe_na_lista = Utils.encontrar_item_por_chave('cafe', self.lista_de_pedidos)
            if (codigo_do_pedido == 'queijo' and existir_sanduiche_na_lista) or (
                    codigo_do_pedido == 'chantily' and existir_cafe_na_lista) or (
                    codigo_do_pedido != 'queijo' and codigo_do_pedido != 'chantily'):
                for item in Carrinho.cardapio_completo:
                    if codigo_do_pedido == item:
                        try:
                            quantidade = int(input('Digite a quantidade que deseja comprar: '))
                            if quantidade > 0:
                                self.valor_total_compra += (Carrinho.cardapio_completo[item]['valor'] * quantidade)
                                print(
                                    f'O produto {item} foi adicionado. O custo total é de: R${self.valor_total_compra: .2f}.')
                                existe_produto_na_lista = Utils.encontrar_item_por_chave(item, self.lista_de_pedidos)
                                if existe_produto_na_lista:
                                    Utils.incrementar_quantidade(item, quantidade, self.lista_de_pedidos)
                                else:
                                    self.lista_de_pedidos.append({item: {'quantidade': quantidade}})
                            else:
                                print('Quantidade inválida.')
                        except ValueError:
                            print('Por favor, informe a quantidade a ser comprada.')
            else:
                print('Item extra não pode ser pedido sem o principal.')
        else:
            print('##### Item inválido! #####')

    def finalizar_ou_continuar_comprando(self):
        try:
            finalizar_ou_continuar = int(input('-------------------------------------------------------- \n'
                                               'Deseja prosseguir para pagamento ou continuar comprando? \n'
                                               '[0] Prosseguir para pagamento \n'
                                                '[1] Continuar comprando \n'
                                               '-------------------------------------------------------- '))
            if finalizar_ou_continuar == 0:
                finalizar = True
                return finalizar
        except ValueError:
            print('Por favor, informe a opção corretamente..')

    def obter_carrinho(self):
        print(f'Os itens selecionados são: \n {self.lista_de_pedidos} \n '
              f'O valor total a pagar é de R${self.valor_total_compra: .2f}.')


class Pagamento(Carrinho):
    def __init__(self, lista_de_pedidos, valor_total_compra):
        super().__init__()
        self.lista_de_pedidos = lista_de_pedidos
        self.valor_total_compra = valor_total_compra

    @staticmethod
    def escolher_forma_de_pagamento():
        while True:
            try:
                forma_de_pagamento = int(input('----------------------------------- \n'
                                               'Qual a forma de pagamento desejada? \n'
                                               '[0] Dinheiro \n'
                                               '[1] Debito \n'
                                               '[2] Credito \n'
                                               '---- DESCONTOS E TAXAS ---- \n'
                                               '- Pagamento em dinheiro tem 5% de desconto \n'
                                               '- Pagamento a crédito tem acréscimo de 3% no valor total \n'
                                               '---------------------------'))
                if 0 <= forma_de_pagamento <= 2:
                    return forma_de_pagamento
                else:
                    print('Forma de pagamento inválida!')
            except ValueError:
                print('Digite o valor corretamente')

    def obter_carrinho(self):
        print(f'Os itens selecionados são: \n {self.lista_de_pedidos} \n '
              f'O valor total a pagar é de R${self.valor_total_compra: .2f}.')

    def valor_total_a_pagar(self, forma_de_pagamento):
        if forma_de_pagamento == 0:
            self.valor_total_compra * 0.95
            print(f'{self.valor_total_compra: .2f}')
        elif forma_de_pagamento == 1:
            print(f'{self.valor_total_compra: .2f}')
        else:
            self.valor_total_compra * 1.03
            print(f'{self.valor_total_compra: .2f}')
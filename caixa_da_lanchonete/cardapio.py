class Cardapio:
    _itens = {
        'cafe': {'descrição': 'Café', 'valor': 3},
        'chantily': {'descrição': 'Chantily (extra do Café)', 'valor': 1.6},
        'suco': {'descrição': 'Suco Natural', 'valor': 6.2},
        'sanduiche': {'descrição': 'Sanduíche', 'valor': 6.5},
        'queijo': {'descrição': 'Queijo (extra do Sanduíche)', 'valor': 2},
        'salgado': {'descrição': 'Salgado', 'valor': 7.25},
        'combo1': {'descrição': '1 Suco e 1 Sanduíche', 'valor': 9.5},
        'combo2': {'descrição': '1 Café e 1 Sanduíche', 'valor': 7.5}
    }

    def __init__(self):
        pass

    @staticmethod
    def mostrar_cardapio():
        print('##################### CARDÁPIO ###################### \n'
              '|   codigo  |         descrição         |  valor    | \n'
              '|-----------|---------------------------|-----------| ')
        for codigo, item in Cardapio._itens.items():
            print(f'| {codigo:<10}| {item["descrição"]:<27}| R$ {item["valor"]: .2f} |')

    @staticmethod
    def obter_cardapio():
        return Cardapio._itens.keys()

    @staticmethod
    def obter_cardapio_inteiro():
        return Cardapio._itens

from cardapio import Cardapio
from carrinho import Carrinho
from carrinho import Pagamento

itens_cardapio = Cardapio.obter_cardapio()
cliente = Carrinho()

Cardapio.mostrar_cardapio()
finalizar = False
while not finalizar:
    item_escolhido = cliente.escolher_item_cardapio()
    cliente.add_to_cart(item_escolhido)
    finalizar = cliente.finalizar_ou_continuar_comprando()

cliente.obter_carrinho()
pagamento = Pagamento(cliente.lista_de_pedidos, cliente.valor_total_compra)

forma_de_pagamento = pagamento.escolher_forma_de_pagamento()
pagamento.obter_carrinho()
pagamento.valor_total_a_pagar(forma_de_pagamento)

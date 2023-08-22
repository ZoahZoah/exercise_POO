class Utils:
    def __init__(self):
        pass

    @staticmethod
    def incrementar_quantidade(nome_item, quantidade, lista):
        for item in lista:
            if nome_item in item:
                if "quantidade" in item[nome_item]:
                    item[nome_item]["quantidade"] += quantidade
                else:
                    item[nome_item]["quantidade"] = quantidade
                return item[nome_item]
        print(f"Item '{nome_item}' não encontrado.")
        return None

    @staticmethod
    def encontrar_item_por_chave(nome_chave, lista):
        for item in lista:
            if nome_chave in item:
                return item
        return None

    @staticmethod
    def try_except_value_error(texto_variavel, texto_erro):
        while True:
            try:
                variavel_inteira_desejada = int(input(texto_variavel))
                return variavel_inteira_desejada
            except ValueError:
                print(texto_erro)
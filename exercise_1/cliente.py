class Cliente:

    def __init__(self, usuario, senha):
        print(f'Cadastrando usuário! Seja bem vindo {usuario}')
        self.__usuario = usuario.upper()
        self.__senha = senha.upper()

    @property
    def nome_cliente(self):
        return self.__usuario

    @property
    def senha_cliente(self):
        return self.__senha

    def cadastro_validado(self, usuario, senha):
        cadastro_valido = self.nome_cliente == usuario and self.senha_cliente == senha
        if (cadastro_valido is True):
            print('Bem vindo a biblioteca virtual!')
            return cadastro_valido


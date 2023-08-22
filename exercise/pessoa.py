class Pessoa:
    def __init__(self, cpf, nome, sexo, idade):
        self.__cpf = cpf
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    def __str__(self):
        return f'Nome: {self.__nome} \n' \
               f'CPF: {self.__cpf} \n' \
               f'Sexo: {self.__sexo} \n' \
               f'Idade: {self.__idade}'

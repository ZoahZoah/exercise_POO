from utils import Utils

class Funcionario:
    def __init__(self, numero_cracha, nome, tipo_vinculo, salario, valor_desconto, valor_a_receber):
        self.__cracha = numero_cracha
        self.__nome = nome
        self.__tipo_vinculo = tipo_vinculo
        self.__salario = salario
        self.__desconto = valor_desconto
        self.__valor_a_receber = valor_a_receber

    @property
    def cracha(self):
        return self.__cracha

    @cracha.setter
    def cracha(self, numero_cracha):
        self.__cracha = numero_cracha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tipo_vinculo(self):
        return self.__tipo_vinculo

    @tipo_vinculo.setter
    def tipo_vinculo(self, tipo_vinculo):
        self.__tipo_vinculo = tipo_vinculo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, valor_desconto):
        self.__desconto = valor_desconto

    @property
    def valor_a_receber(self):
        return self.__valor_a_receber

    @valor_a_receber.setter
    def valor_a_receber(self, valor_a_receber):
        self.__valor_a_receber = valor_a_receber


    @staticmethod
    def calcular_salario(valor_hora, qtde_hora):
        return valor_hora * qtde_hora

    @staticmethod
    def calcular_valor_receber(salario, desconto):
        salario_a_receber = salario - desconto
        return salario_a_receber

    @staticmethod
    def case_vinculo_normal():
        salario = Utils.try_except_value_error('Digite o salário mensal em reais: ', 'Por favor, digite apenas números.')
        return salario

    @staticmethod
    def case_vinculo_horista():
        valor_hora = Utils.try_except_value_error('Digite o valor recebido por hora trabalhada: ', 'Digite apenas números.')
        qtde_hora = Utils.try_except_value_error('Digite a quantidade de horas trabalhadas no mês: ', 'Digite apenas números.')
        salario = Funcionario.calcular_salario(valor_hora, qtde_hora)
        return salario

    @staticmethod
    def switch_case_tipo_de_vinculo(tipo_vinculo):
        switch_dic = {
            'H': Funcionario.case_vinculo_horista,
            'N': Funcionario.case_vinculo_normal
        }
        return switch_dic.get(tipo_vinculo)

    def __str__(self):
        return f'Crachá: {self.__cracha} \n' \
               f'Nome: {self.__nome} \n' \
               f'Tipo de Vínculo: {self.__tipo_vinculo} \n' \
               f'Salario: {self.__salario: .2f} \n' \
               f'Desconto: {self.__desconto: .2f} \n' \
               f'Valor a receber: R${self.__valor_a_receber: .2f}'
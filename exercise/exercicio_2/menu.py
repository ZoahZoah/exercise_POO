from utils import Utils
from funcionario import Funcionario

class Menu:
    tipos_de_vinculos = {'H': 'horista', 'N': 'normal'}
    def __init__(self):
        self.funcionarios = []



    def criar_funcionario(self):
        cracha = Utils.try_except_value_error('Digite o número do crachá do funcionário: ', 'Por favor, digite apenas números.')
        nome = input('Digite o nome do funcionário: ').capitalize()
        tipo_vinculo = 0
        salario = 0
        while True:
            tipo_vinculo = input('Digite a letra correspondente ao vínculo empregatício: \n'
                             'H - horista \n'
                             'N - normal \n').capitalize()
            if tipo_vinculo in Menu.tipos_de_vinculos:
                salario_vinculo = Funcionario.switch_case_tipo_de_vinculo(tipo_vinculo)
                salario = salario_vinculo()
                break
            else:
                print('Digite a letra conforme as disponibilizadas.')
        valor_desconto = Utils.try_except_value_error('Digite o desconto mensal em reais: ',
                                                        'Por favor, digite apenas números.')
        valor_a_receber = Funcionario.calcular_valor_receber(salario, valor_desconto)
        funcionario = Funcionario(cracha, nome, tipo_vinculo, salario, valor_desconto, valor_a_receber)
        self.funcionarios.append(funcionario)

    def mostrar_folha_de_pagamento(self):
        if not self.funcionarios:
            print('A lista está vazia.')
        else:
            for funcionario in self.funcionarios:
                print(f'---------------------------------------------------------------------------------- \n'
                      f'Funcionário: {funcionario.nome} | Crachá: {funcionario.cracha} | '
                      f'Tipo de Vínculo: {funcionario.tipo_vinculo} | Salario: R${funcionario.salario: .2f} | '
                      f'Desconto: R${funcionario.desconto: .2f} | '
                      f'Valor a receber: R${funcionario.valor_a_receber: .2f} \n'
                       '----------------------------------------------------------------------------------')

    def alterar_remuneracao(self):
        if not self.funcionarios:
            print('Não temos nenhum funcionário cadastrado.')
        else:
            numero_cracha = Utils.try_except_value_error('Digite o numero do crachá do funcionário a ser alterado: ', 'Digite apenas números.')
            funcionario_encontrado = None
            for funcionario in self.funcionarios:
                if numero_cracha == funcionario.cracha:
                    funcionario_encontrado = funcionario
                    break

            if funcionario_encontrado:
                salario_vinculo = Funcionario.switch_case_tipo_de_vinculo(funcionario_encontrado.tipo_vinculo)
                funcionario_encontrado.salario = salario_vinculo()
                valor_desconto = Utils.try_except_value_error('Digite o desconto mensal em reais: ',
                                                              'Por favor, digite apenas números.')
                funcionario_encontrado.valor_a_receber = Funcionario.calcular_valor_receber(funcionario_encontrado.salario, valor_desconto)
            else:
                print('Funcionário não encontrado.')

    def switch_case_menu(self, resposta_menu):
        switch_dict = {
            1: self.criar_funcionario,
            2: self.mostrar_folha_de_pagamento,
            3: self.alterar_remuneracao
        }
        return switch_dict.get(resposta_menu)

    def menu_interacao(self):
        while True:
            resposta_menu = Utils.try_except_value_error('Digite o número corresponde a ação: \n'
                                                         '(1) Criar Funcionário \n'
                                                         '(2) Mostrar folha de pagamento \n'
                                                         '(3) Alterar Remuneração \n'
                                                         '(4) Sair \n', 'Valor inválido.')
            if resposta_menu == 4:
                break
            elif 0 < resposta_menu < 4:
                 resposta_menu = self.switch_case_menu(resposta_menu)
                 resposta_menu()
            else:
                print('Valor inválido.')
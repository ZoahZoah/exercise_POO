from utils import Utils
from pessoa import Pessoa

class Menu:
    def __init__(self):
        self.lista_pessoas = []

    @staticmethod
    def case_masculino():
        sexo = 'Masculino'
        return sexo

    @staticmethod
    def case_feminino():
        sexo = 'Feminino'
        return sexo

    @staticmethod
    def switch_case_genero(sexo):
        switch_dict = {
            'M': Menu.case_masculino(),
            'F': Menu.case_feminino()
        }
        return switch_dict.get(sexo)

    @staticmethod
    def criar_pessoa():
        opcoes_sexo = ['Masculino', 'Feminino']
        cpf = Utils.try_except_value_error('Digite seu cpf: ', 'Digite apenas números.')
        nome = input('Digite seu nome: ').capitalize()
        sexo_opcoes = input('(M) - Masculino \n'
                     '(F) - Ferminino \n').capitalize()
        sexo = Menu.switch_case_genero(sexo_opcoes)
        idade = Utils.try_except_value_error('Digite sua idade: ', 'Digite apenas números.')
        return cpf, nome, sexo, idade

    def adicionar_pessoa(self, pessoa_a_adicionar):
        pessoa_nome = str(pessoa_a_adicionar.nome)
        pessoal_sexo = str(pessoa_a_adicionar.sexo)
        pessoa_idade = int(pessoa_a_adicionar.idade)
        pessoa = {'nome': pessoa_nome, 'sexo': pessoal_sexo, 'idade': pessoa_idade}
        pessoa_cpf = str(pessoa_a_adicionar.cpf)
        pessoa_dicionario = {pessoa_cpf: pessoa}
        self.lista_pessoas.append(pessoa_dicionario)

    def case_criar_pessoa(self):
        cpf, nome, sexo, idade = self.criar_pessoa()
        pessoa = Pessoa(cpf, nome, sexo, idade)
        self.adicionar_pessoa(pessoa)

    def case_mostrar_pessoa(self):
        if not self.lista_pessoas:
            print('A lista está vazia.')
        else:
            print('##################### Lista de Pessoas ###################### \n'
                  '|    CPF      |     Nome       |    Sexo   | Idade  | \n'
                  '|-------------|----------------|-----------|--------| ')
            for pessoa in self.lista_pessoas:
                cpf, dados_pessoa = list(pessoa.items())[0]
                print(f'| { cpf:<12}|'
                        f' {dados_pessoa["nome"]:<15}|'
                        f' {dados_pessoa["sexo"]:<10}|'
                        f'   {dados_pessoa["idade"]:<3}  | \n')


    def switch_case_opcoes_menu(self, escolha_menu):
        switch_dict = {
            1: self.case_criar_pessoa,
            2: self.case_mostrar_pessoa
        }
        return switch_dict.get(escolha_menu)

    def menu(self):
        lista_opcoes = [1, 2, 3]
        while True:
            try:
                escolha_menu = int(input('Menu: \n'
                  '1 - Criar pessoa \n'
                  '2 - Mostrar pessoa \n'
                  '3 - Sair \n'))
                if escolha_menu in lista_opcoes:
                    if escolha_menu == lista_opcoes[2]:
                        break
                    else:
                       opcoes_menu = self.switch_case_opcoes_menu(escolha_menu)
                       opcoes_menu()
                else:
                    print('Digite o valor corretamente')
            except ValueError:
                print('Digite o número correspondente a ação.')




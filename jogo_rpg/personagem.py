class Personagem:
    classes = ['Arqueiro', 'Mago', 'Espadachim']
    sexo_opcoes = ['Masculino', 'Feminino', 'Outro']
    def __init__(self, nome, sexo, classe):
        self._nome = nome
        self.sexo = sexo
        self.classe = classe

    def __str__(self):
        return  f'Nome: {self._nome} \n' \
                f'Sexo: {self.sexo}  \n' \
                f'Classe: {self.classe}'

    @staticmethod
    def definir_personagem_nome():
        nome = input('Digite o nome para o seu personagem: ').title()
        print(f'O nome definido foi: {nome}')
        return nome

    @staticmethod
    def definir_personagem_genero():
        m_f_o = ['M', 'F', 'O']
        while (True):
            letra = m_f_o
            sexo_protagonista = input('Digite o sexo do seu personagem: '
                                      f'({m_f_o[0]}) - Masculino, ({m_f_o[1]}) Feminino, ({m_f_o[2]}) Outro \n').capitalize()
            if (sexo_protagonista in letra):
                for sexo in Personagem.sexo_opcoes:
                    if (sexo.startswith(sexo_protagonista)):
                        sexo_protagonista = sexo
                        print(f'O sexo selecionado foi: {sexo_protagonista}')
                break
            else:
                print(
                    f'Hey, {sexo_protagonista} é um valor incorreto, por favor, digite conforma a letra correspondente.')
        return sexo_protagonista

    @staticmethod
    def definir_personagem_classe():
        while True:
            classes_iniciais = ['A', 'M', 'E']
            classe_personagem = input('Digite a letra da sua classe desejada: \n'
                           f'({classes_iniciais[0]}) Arqueiro, ({classes_iniciais[1]}) Mago, ({classes_iniciais[2]}) Espadachim \n').capitalize()
            if (classe_personagem in classes_iniciais):
                for classe in Personagem.classes:
                    if (classe.startswith(classe_personagem)):
                        classe_personagem = classe
                        print(f'A classe selecionada foi: {classe_personagem}')
                break
            elif (classe_personagem in Personagem.classes):
                break
            else:
                print(
                    f'Hey, {classe_personagem} é um valor incorreto, por favor, digite conforma a letra correspondente.')
        return classe_personagem

class Protagonista(Personagem):
    arqueiro = 'Arqueiro'
    arqueiro_status = {'HP': 13, 'Atk': 7, 'Atk Mg': 5, 'def': 6}
    mago = 'Mago'
    mago_status = {'HP': 10, 'Atk': 3, 'Atk Mg': 12, 'def': 5}
    espadachim = 'Espadachim'
    espadachim_status = {'HP': 20, 'Atk': 10, 'Atk Mg': 2, 'def': 8}
    conjunto_classes = []

    def __init__(self, nome, sexo, classe, nivel):
        super().__init__(nome, sexo, classe)
        for classes_disponiveis in Personagem.classes:
            if (classe == classes_disponiveis and classes_disponiveis == Protagonista.arqueiro):
                self.classe_status =  Protagonista.arqueiro_status
                break
            elif (classe == classes_disponiveis and classes_disponiveis == Protagonista.mago):
                self.classe_status =  Protagonista.mago_status
                break
            elif (classe == classes_disponiveis and classes_disponiveis == Protagonista.espadachim):
                self.classe_status =  Protagonista.espadachim_status
                break
        self.nivel = nivel
    def __str__(self):
        return  f'Nome: {self._nome} \n' \
                f'Sexo: {self.sexo}  \n' \
                f'Classe: {self.classe} \n' \
                f'Nível: {self.nivel} \n' \
                f'Status: {self.classe_status} \n'


    def subir_nivel(self, nivel):
        for i in self.classe_status:
            self.classe_status[i] += (2 * nivel)

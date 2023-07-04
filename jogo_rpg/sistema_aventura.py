class SistemaAventura:
    facil = 0
    medio = 1
    dificil = 2
    dificuldades = [facil, medio, dificil]
    def __init__(self, nivel):
        self.nivel = nivel
        if (self.nivel == 5):
            print(f'O nível inicial é: {nivel}, então iniciaremos no fácil.')
        elif (self.nivel == 3):
            print(f'O nível inicial é: {nivel}, então iniciaremos no médio.')
        elif (self.nivel == 1):
            print(f'O nível inicial é: {nivel}, então iniciaremos no dificil.')

    @staticmethod
    def definir_dificuldade_do_jogo():
        bool_nivel = False
        while (not bool_nivel):
            dificuldade = int(input('Vamos começar escolhendo o nível de dificuldade do jogo: \n'
                                    '[0] Fácil, [1] Médio, [2] Díficil '))
            if (dificuldade in SistemaAventura.dificuldades):
                for nivel in SistemaAventura.dificuldades:
                    if (dificuldade == nivel and nivel == 0):
                        print(f'O nível selecionado foi: {nivel}.')
                        nivel_protagonista = 5
                        bool_nivel = True
                        break
                    elif (dificuldade == nivel and nivel == 1):
                        print(f'O nível selecionado foi: {nivel}.')
                        nivel_protagonista = 3
                        bool_nivel = True
                        break
                    elif (dificuldade == nivel and nivel == 2):
                        print(f'O nível selecionado foi: {nivel}.')
                        nivel_protagonista = 1
                        bool_nivel = True
                        break
            else:
                print('Você não digitou um valor correto.')
        return nivel_protagonista

    @staticmethod
    def escolher_action():
        opcoes_actions = ['C', 'L']
        while (True):
            action = input('Sistema: Você tem duas opções: \n'
                           '(C) Correr, (L) Lutar').capitalize()
            if (action in opcoes_actions):
                break
            else:
                print('O valor digitado não corresponde ao solicitado')
        return action

    @staticmethod
    def escolher_onde_ir():
        opcoes_terreno = ['F', 'M', 'L']
        while True:
            terreno = input('Estamos iniciando uma nova aventura, por onde gostaria de seguir?   \n'
                            '(F) - Floresta, (M) - Montanha, (L) Lago ').capitalize()
            if (terreno in opcoes_terreno):
                if (terreno == opcoes_terreno[0]):
                    terreno = 'Floresta'
                    print(f'Você está seguindo para a {terreno}')
                elif (terreno == opcoes_terreno[1]):
                    terreno = 'Montanha'
                    print(f'Você está seguindo para a {terreno}')
                elif (terreno == opcoes_terreno[2]):
                    terreno = 'Lago'
                    print(f'Você está seguindo para o {terreno}')
                return terreno
                break
            else:
                print('O valor digitado não corresponde ao solicitado.')

    @staticmethod
    def batalha(protagonista, monstro):
        while (True):
            if (protagonista.classe_status['HP'] > 0 and monstro.status['HP'] > 0):
                actions = ['A', 'M', 'D']
                action = input('O que você gostaria de fazer: \n'
                               '(A) Atacar, (M) Magicar, (D) Defender').capitalize()
                if (action in actions):
                    if (action == 'A'):
                        monstro.status['HP'] = monstro.status['HP'] - (protagonista.classe_status['Atk'] - monstro.status['def'])
                        print(monstro.status['HP'])
                        if (monstro.status['HP'] > 0):
                            protagonista.classe_status['HP'] = protagonista.classe_status['HP'] - monstro.status['Atk'] - \
                                                               protagonista.classe_status['def'] // 2
                            print(protagonista.classe_status['HP'])
                    elif (action == 'M'):
                        monstro.status['HP'] = monstro.status['HP'] - (protagonista.classe_status['Atk Mg'] - monstro.status['def'])
                        print(monstro.status['HP'])
                        if (monstro.status['HP'] > 0):
                            protagonista.classe_status['HP'] = protagonista.classe_status['HP'] - (
                                    monstro.status['Atk'] - protagonista.classe_status['def'] // 2)
                            print(protagonista.classe_status['HP'])
                    elif (action == 'D'):
                        pass
                    else:
                        print('Comando inválido.')
            elif (protagonista.classe_status['HP'] <= 0 or monstro.status['HP'] <= 0):
                break
        print('Você venceu a luta!!')
    def __str__(self):
        return f'O nível atual é: {self.nivel}'
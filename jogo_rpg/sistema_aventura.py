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

    def qual_caminho_deseja_seguir(self):
        opcoes_terreno = ['F', 'M', 'L']
        terrenos = ['Floresta', 'Montanha', 'Lago']
        opcoes_actions = ['C', 'L']
        bool_action = False
        if (self.nivel == 5):
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
                    break
                else:
                    print('O valor digitado não corresponde ao solicitado.')
            if (terreno == terrenos[0]):
                print('Personagem Secundário: TOME CUIDADO!!! \n'
                      'Ao ouvir gritos, você olha para trás e vê monstros se aproximando! \n'
                      '.....................................................................')

                while (True):
                    action = input('Sistema: Você tem duas opções: \n'
                                   '(C) Correr, (L) Lutar').capitalize()
                    if (action in opcoes_actions):
                        break
                    else:
                        print('O valor digitado não corresponde ao solicitado')
                if (action == opcoes_actions[0]):
                    pass
                elif (action == opcoes_actions[1]):
                    pass
            elif (terreno == terrenos[1]):
                pass
            elif (terreno == terrenos[1]):
                pass
        elif (self.nivel == 3):
            pass
        elif (self.nivel == 1):
            pass

    def __str__(self):
        return f'O nível atual é: {self.nivel}'
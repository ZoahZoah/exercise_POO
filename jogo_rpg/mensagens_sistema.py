class MensagemSistema:
    def __init__(self):
        pass
    def mensagem_bem_vindo(self):
        print('-----------------------------------------------\n'
              'Bem vindo ao RPG do Zoah (atualmente em testes)\n'
              '-----------------------------------------------')

    def criacao_bem_sucedida(self, protagonista):
        print('--------------------------------------------\n'
              '-----Parabéns! Você criou o seu personagem: \n'
              f'{protagonista} \n')
from personagem import Personagem
from personagem import Protagonista
from personagem import Monstro
from mensagens_sistema import MensagemSistema
from sistema_aventura import SistemaAventura

# Facilitando a transcrição da classe ao passar o objeto para uma variável:
mensagens_sistema = MensagemSistema()
personagem = Personagem
sistema_aventura = SistemaAventura

# Inicio real do código:
mensagens_sistema.mensagem_bem_vindo()

#Definindo a dificuldade da aventura pelo nível inicial do personagem
dificuldade = sistema_aventura.definir_dificuldade_do_jogo()
print(dificuldade)
nivel_dificuldade = sistema_aventura(dificuldade)
print(nivel_dificuldade)

# Criando o personagem
nome_protagonista = personagem.definir_personagem_nome()
sexo_protagonista = personagem.definir_personagem_genero()
classe_protagonista = personagem.definir_personagem_classe()

# Registrando o personagem
protagonista = Protagonista(nome_protagonista, sexo_protagonista, classe_protagonista, dificuldade)
protagonista.subir_nivel(dificuldade)
mensagens_sistema.criacao_bem_sucedida(protagonista)

while (protagonista.classe_status['HP'] > 0):
        terrenos = ['Floresta', 'Montanha', 'Lago']

        terreno = sistema_aventura.escolher_onde_ir()
        if (terreno == terrenos[0]):
            opcoes_actions = ['C', 'L']
            print('Personagem Secundário: TOME CUIDADO!!! \n'
                  'Ao ouvir gritos, você olha para trás e vê monstros se aproximando! \n'
                  '.....................................................................')
            action = sistema_aventura.escolher_action()
            print(action)
            if (action == opcoes_actions[0]):
                print('Infelizmente você correu e o estranho acabou sendo atacado no seu lugar.')
            elif (action == opcoes_actions[1]):
                lobo = Monstro('Lobo', 'Animal')
                lobo.status_monstro()
                sistema_aventura.batalha(protagonista=protagonista, monstro=lobo)
                print('Personagem secundário: Obrigado pela ajuda, amigo, nos vemos por ai!')
        elif (terreno == terrenos[1]):
            pass
        elif (terreno == terrenos[1]):
            pass

from personagem import Personagem
from personagem import Protagonista
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
nivel_dificuldade = sistema_aventura(dificuldade)

# Criando o personagem
nome_protagonista = personagem.definir_personagem_nome()
sexo_protagonista = personagem.definir_personagem_genero()
classe_protagonista = personagem.definir_personagem_classe()

# Registrando o personagem
protagonista = Protagonista(nome_protagonista, sexo_protagonista, classe_protagonista, dificuldade)
protagonista.subir_nivel(dificuldade)
mensagens_sistema.criacao_bem_sucedida(protagonista)

while protagonista.classe_status['HP'] != 0:
    nivel_dificuldade.qual_caminho_deseja_seguir()
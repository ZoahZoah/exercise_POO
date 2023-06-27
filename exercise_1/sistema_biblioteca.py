from cliente import Cliente
from livro  import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()
cliente1 = Cliente('IVAN', '123')
cliente2 = Cliente('BORGES', '321')

livro1 = Livro('O menino, a Toupeira, a Raposa e o Cavalo', 'Charlie Mackesy', 3)
livro2 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exuéry', 5)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.livros_disponiveis()

usuario = input('Nome de usuário: ').upper()
senha = input('Digite a senha (apenas números): ')

cliente1_validado = cliente1.cadastro_validado(usuario, senha)
cliente2_validado = cliente2.cadastro_validado(usuario, senha)
if (cliente1_validado is True or cliente2_validado is True):
    nome_livro, livro_existe = biblioteca.buscar_livro()

    if (livro_existe is True):
        while True:
            resposta = int(input('Digite: '
                                 '(0) Pegar o livro   '
                                 '(1) Devolver livro'))
            if (resposta == 0):
                nome_livro.livro_emprestado()
                break
            elif (resposta == 1):
                nome_livro.livro_devolvido()
                break
            else:
                print('Valor digitado está incorreto.')


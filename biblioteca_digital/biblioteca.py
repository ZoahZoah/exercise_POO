class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro {livro.nome} foi adicionado!')

    def remover_livro(self, livro):
        self.livros.append(livro)

    def buscar_livro(self):
        nome_livro = input('Digite o nome do livro que deseja: ').upper()
        for livro in self.livros:
            achou_o_livro = nome_livro in livro.nome
            if (achou_o_livro is True):
                return livro, True
                break
            return None, False

    def livros_disponiveis(self):
        i = 1
        for livro in self.livros:
            print(f'[{i}] {livro.nome}')
            i += 1

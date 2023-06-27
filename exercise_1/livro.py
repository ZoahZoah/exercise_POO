class Livro:

    def __init__(self, nome, autor, numero_copias):
        self.nome = nome.upper()
        self.autor = autor.upper()
        self.numero_copias = numero_copias

    @property
    def nome_livro(self):
        return self.nome

    def quantidade_livro(self):
        return self.numero_copias

    def pesquisa_livro(self, nome_livro):
            self.nome.find(nome_livro)
            print()

    def livro_emprestado(self):
        quantidade_livros = Livro.quantidade_livro(self)
        if (quantidade_livros > 0):
            print('Parabéns! Espero que aproveite a leitura.')
            self.numero_copias -= 1

    def livro_devolvido(self):
        print('Obrigado por nos devolver o livro!')
        self.numero_copias += 1
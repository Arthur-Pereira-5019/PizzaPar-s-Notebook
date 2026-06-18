from Livros import *
class MochilaDeLivros:
    def __init__(self):
        self.livros = []

    def devolver(self, indice: int, bu_multa: int, bu_tempo_emprestimo: int):
        self.livros.pop(indice)

    def adicionar(self, livro: Livro):
        self.livros.append(livro)

    def devolverTudo(self):
        multa = 0


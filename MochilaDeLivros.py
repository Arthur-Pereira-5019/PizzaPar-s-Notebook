from Livros import *
class MochilaDeLivros:
    def __init__(self, ):
        self.livros = []
        self.multa = 0.0
        self.renovacoes = 0
        self.tempo_emprestimo = 0
        self.distancia = 0
        self.configurada = False

    def configurar(self, multa, renovacoes, tempo_emprestimo, distancia):
        self.multa = multa
        self.renovacoes = renovacoes
        self.tempo_emprestimo = tempo_emprestimo
        self.distancia = distancia
        self.configurada = True

    def devolver(self, indice: int, bu_multa: int, bu_tempo_emprestimo: int):
        self.livros.pop(indice)

    def adicionar(self, livro: Livro, dia: date):
        livro.pegar(dia,self.tempo_emprestimo)
        self.livros.append(livro)

    def devolverTudo(self):
        multa = 0

    def multaAcumulada(self):
        multa = 0.0
        for i in range (len(self.livros)):
            multa += self.livros[i].calcularMulta()
        return multa






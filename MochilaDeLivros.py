from Livros import *
class MochilaDeLivros:
    def __init__(self):
        self.livros: list[Livro] = []
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

    def devolver(self, indice: int, dia: date):
        livro = self.livros[indice]
        ex = livro.exibicao_simples()
        multa = livro.calcularMulta(self.multa,dia)
        self.livros.pop(indice)
        if multa > 0:
            print(f"{ex} devolvido com uma multa de {multa}R$.")
        else:
            print(f"{ex} devolvido sem multa.")
        self.organizar(dia)

    def adicionar(self, livro: Livro, dia: date):
        livro.pegar(dia,self.tempo_emprestimo)
        self.livros.append(livro)
        self.organizar(dia)

    def devolverTudo(self, dia: date):
        multa = self.multaAcumulada(dia)
        t = len(self.livros)
        self.livros.clear()
        print(f"{t} Livros devolvidos, custando {multa}R$ em Multa.")

    def multaAcumulada(self, dia: date):
        multa = 0.0
        for i in range (len(self.livros)):
            multa += self.livros[i].calcularMulta(self.multa,dia)
        return multa

    def exibicao(self, dia: date):
        for i in range (len(self.livros)):
            print(f"{i+1}. {self.livros[i].exibicao(self.multa,dia)}")

    def organizar(self, dia: date):
        self.livros = sorted(self.livros, key=lambda l: (l.calcularMulta(self.multa,dia), l.data_de_devolucao, l.titulo))

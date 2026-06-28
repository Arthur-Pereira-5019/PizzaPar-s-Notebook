from Livros import *
from Disciplina import *
class MochilaDeLivros:
    def __init__(self):
        self.livros: list[Livro] = []
        self.multa = 0.0
        self.renovacoes = 0
        self.tempo_emprestimo = 0
        self.configurada = False

    def configurar(self, multa, renovacoes, tempo_emprestimo):
        self.multa = multa
        self.renovacoes = renovacoes
        self.tempo_emprestimo = tempo_emprestimo
        self.configurada = True

    def devolver(self, indice: int, dia: date):
        livro = self.livros[indice-1]
        ex = livro.exibicao_simples()
        multa = livro.calcularMulta(self.multa,dia)
        self.livros.pop(indice-1)
        if multa > 0:
            print(f"{ex} devolvido com uma multa de {multa}R$.")
        else:
            print(f"{ex} devolvido sem multa.")
        self.organizar(dia)

    def renovar(self, indice: int, dia: date):
        livro = self.livros[indice]
        ex = livro.exibicao_simples()
        multa = livro.calcularMulta(self.multa, dia)
        if livro.gNRenovacoes() > self.renovacoes:
            print("Este exemplar está no limite de renovações, impossível renovar.")
            return
        self.livros[indice].nRenovacoes += 1
        self.livros[indice].renovar(dia,self.tempo_emprestimo)
        if multa > 0:
            print(f"{ex} renovado com uma multa de {multa}R$.")
        else:
            print(f"{ex} renovado sem multa.")
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
        livrosAtrasados = self.livrosAtrasados(dia)
        for i in range (len(livrosAtrasados)):
            multa += livrosAtrasados[i].calcularMulta(self.multa,dia)
        return multa

    def exibicao(self, dia: date):
        for i in range (len(self.livros)):
            print(f"{i+1}. {self.livros[i].exibicao(self.multa,dia)}")

    def organizar(self, dia: date):
        self.livros = sorted(self.livros, key=lambda l: (l.calcularMulta(self.multa,dia), l.data_de_devolucao, l.titulo))

    def livrosADevolverHoje(self, dia: date):
        devolver = []
        for i in range(len(self.livros)):
            if self.livros[i].dias_ate_vencer(dia) == 0:
                devolver.append(self.livros[i])
        return devolver

    def cruzarBibliografia(self, disciplina: DisciplinaCurricular):
        biblio = disciplina.getBibliografia()
        faltantes = []
        for i in range (len(biblio)):
            if biblio[i] in self.livros:
                continue
            else:
                faltantes.append(biblio[i])
        return faltantes

    def calcularDevolucao(self, dia):
        return dia + timedelta(self.tempo_emprestimo)

    def isConfigurada(self):
        return self.configurada

    def livrosAtrasados(self, dia):
        livrosAtrasados = []
        for i in range (len(self.livros)):
            if self.livros[i].em_atraso(dia):
                livrosAtrasados.append(self.livros[i])
        return livrosAtrasados

    def exibirAtrasos(self, dia: date):
        atrasados = self.livrosAtrasados(dia)
        nAtrasados = len(atrasados)
        if nAtrasados == 0:
            print("Nenhum livro atrasado para a data informada.")
        else:
            for i in range(nAtrasados):
                print(f"{i + 1}. {atrasados[i].exibicao(self.multa,dia)}")
            print("\n")

    def gerarResumo(self, dia):
        nAtrasados = len(self.livrosAtrasados(dia))
        nDevolver = len(self.livrosADevolverHoje(dia))

        print(f"Você está com {len(self.livros)} livro(s) em sua mochila")
        if nAtrasados > 0:
            print(self.textoAtraso(dia))
        if nDevolver > 0:
            print(f"{nDevolver} livro(s) deve(m) ser devolvido(s) hoje.")

    def textoAtraso(self, dia):
        nAtrasados = len(self.livrosAtrasados(dia))
        multaAcumulada = self.multaAcumulada(dia)
        return f"Existe(m) {nAtrasados} livro(s) atrasado(s), gerando uma multa de: {multaAcumulada:.2f}R$."

    def getLivros(self):
        return self.livros

    def getMulta(self):
        return self.multa
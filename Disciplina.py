from typing import Any

from Anotacoes import Anotacoes
from Listas import Listas
from Provas import Provas
from Duvidas import Duvidas
from datetime import date, timedelta
import ModuloTempo as mt

class Disciplina:
    idContador = 0
    #Um item de hora início para cada dia da semana, representando o começo da aula naquele dia. Se for mais fácil fazer os cálculos de conflito, salva como int ou string ou sla oq lilbro
    def __init__(self, nome, dias: list[int], duracao, horaInicio: list[float], horaFim: list[float]):
        self.nome = nome
        self.dias = dias
        self.duracao = duracao
        self.horaInicio = horaInicio
        self.horaFim = horaFim
        self.listaDePresenca = [False] * ((duracao // 7) * len(dias))
        self.marcadorPresenca = 0
        self.id = Disciplina.idContador
        Disciplina.idContador += 1

    def get_nome(self):
        return self.nome
    
    def get_dias(self):
        return self.dias
    
    def get_duracao(self):
        return self.duracao

    def getHoraHoje(self):
        return self.horaInicio

    def getHoraFim(self):
        return self.horaInicio

    def stringAulas(self):
        return f"{self.marcadorPresenca}/{len(self.listaDePresenca)}"

    def getHoraFimHoje(self, dds):
        return self.horaFim[self.dias.index(dds)]

    def getHoraInicioHoje(self, dds):
        return self.horaInicio[self.dias.index(dds)]

    def marcarPresenca(self, presenca: bool):
        self.listaDePresenca[self.marcadorPresenca] = presenca
        self.marcadorPresenca += 1


    def isConcluida(self):
        return self.marcadorPresenca+1 == len(self.listaDePresenca)

    def __eq__(self, other):
        return self.id == other.id

class DisciplinaEsportiva(Disciplina):
    def __init__(self, nome, dias, duracao, horaInicio, horaFim, diasDisputa: list[date]):
        super().__init__(nome, dias, duracao, horaInicio, horaFim)
        self.diasDisputa = diasDisputa
        
    def getDiasDisputa(self):
        return self.diasDisputa

    def getProximasDisputas(self, dia):
        disputas = self.diasDisputa
        retorno = []
        for i in range(len(disputas)):
            if disputas[i] > dia:
                retorno.append(disputas[i])
        return retorno

    def exibirDiasDisputa(self, dia):
        disputas = self.getProximasDisputas(dia)
        for i in range(len(disputas)):
            print(f"{i+1}mt.exibir_data(disputas[i])")

    def removerDisputaPeloIndice(self, indice: int, dia):
        disputas = self.getProximasDisputas(dia)
        self.diasDisputa.remove(disputas[indice])

    

class DisciplinaCurricular(Disciplina):
    def __init__(self, nome, dias, duracao, horaInicio, horaFim, aptidao):
        super().__init__(nome, dias, duracao, horaInicio, horaFim)
        self.anotacoes = []
        self.listas = []
        self.provas: list[Provas] = []
        self.duvidas = []
        self.bibliografia = []
        self.aptidao = aptidao
        
    def addAnotacoes(self, data, texto):
        self.anotacoes.append(Anotacoes(data, texto))
    
    def addListas(self, data):
        self.listas.append(Listas(data))
        
    def addProvas(self, data):
        possivel = True
        for i in range(len(self.provas)):
            if self.provas[i].getData == data:
                print("Erro: Já há uma prova registrada nesse dia e nesta disciplina!")
                possivel = False
        if possivel:
            self.provas.append(Provas(data))
            self.provas = sorted(self.provas, key=lambda p: (p.getData()))

    def addDuvidas(self, data, texto):
        self.duvidas.append(Duvidas(data, texto))
        
    def addBibliografia(self, livro):
        self.bibliografia.append(livro)

    def getProvas(self):
        return self.provas

    def getBibliografia(self):
        return self.bibliografia

    def nListasPreProva(self, prova: Provas):
        n = 0
        for i in range(len(self.listas)):
            if not self.listas[i].getFeita() and self.listas[i].getData() < prova.getData():
                n+=1
        return n

    def getProximaProva(self, dia: date) -> Provas | None:
        for i in range (len(self.provas)):
            if self.provas[i] > dia:
                return self.provas[i]
        return None

    def getListasPreProximaProva(self, dia):
        pp = self.getProximaProva(dia)
        if pp is None:
            return 0
        return self.nListasPreProva(pp)

    def diasAteAProximaProva(self, dia):
        pp = self.getProximaProva(dia)
        if pp is None:
            return float('inf')
        return timedelta(pp.getData() - dia)

    def getProvasAnteriores(self, dia):
        retorno = []
        for i in range (len(self.provas)):
            if self.provas[i].getData() < dia:
                retorno.append(self.provas[i])
        return retorno

    def getMediaIndefinida(self, dia):
        provasAnteriores = self.getProvasAnteriores(dia)
        nProvas = len(provasAnteriores)
        media = 0
        if nProvas == 0:
            return 6

        for i in range (nProvas):
            media += provasAnteriores[i].getNota()
        return media/nProvas

    def getMediaDefinida(self):
        media = 0
        nProvas = len(self.provas)
        if nProvas == 0:
            return 10

        for i in range(nProvas):
            media += self.provas[i].getNota()
        return media / nProvas

    def isApto(self, aptidoes):
        return aptidoes[self.aptidao]

    def calcFrequenciaParcial(self):
        presencas = 0
        if self.marcadorPresenca == 0:
            return 0
        for i in range (self.marcadorPresenca+1):
            if self.listaDePresenca[i]:
                presencas += 1
        return presencas / (self.marcadorPresenca / 100)

    def calcFrequenciaTotal(self):
        presencas = 0
        for i in range(len(self.listaDePresenca)):
            if self.listaDePresenca[i]:
                presencas += 1
        return presencas / ((len(self.listaDePresenca)) / 100)

    def getNListasAFazer(self):
        n = 0
        for i in range (len(self.listas)):
            if not self.listas[i].getFeita():
                n += 1
        return n

    def getMensagemAprovacao(self):
        if self.calcFrequenciaTotal() > 0.75:
            if self.getMediaDefinida() > 6.0:
                return f"Parabéns, você foi aprovado em {self.nome} com média {self.getMediaDefinida()}"
            return f"Infelizmente você não obteve aprovação em {self.nome}, sua média final atingida foi: {self.getMediaDefinida()}"
        return f"Infelizmente você não obteve aprovação em {self.nome} por motivos de frequência insuficiente."

    def darNotaPeloIndice(self, indice: int, nota):
        self.provas[indice].setNota(nota)


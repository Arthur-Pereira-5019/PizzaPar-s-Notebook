from typing import Any

from Anotacoes import Anotacoes
from Listas import Listas
from Provas import Provas
from Duvidas import Duvidas
from datetime import date, timedelta

class Disciplina:
    def __init__(self, nome, dias, duracao, horaInicio, horaFim):
        self.nome = nome
        self.dias = dias
        self.duracao = duracao
        self.horaInicio = horaInicio
        self.horaFim = horaFim
        self.presenca = [False]*((duracao//7)*len(dias))
        self.marcadorPresenca = 0

    def get_nome(self):
        return self.nome
    
    def get_dias(self):
        return self.dias
    
    def get_duracao(self):
        return self.duracao
    
    def get_horaInicio(self):
        return self.horaInicio

    def get_hora(self):
        return self.horaFim

    def marcarPresenca(self):
        self.presenca[self.marcadorPresenca] = True
        self.marcadorPresenca += 1





class DisciplinaEsportiva(Disciplina):
    def __init__(self, nome, dias, duracao, horaInicio, horaFim, diasDisputa):
        super().__init__(nome, dias, duracao, horaInicio, horaFim)
        self.diasDisputa = diasDisputa
        
    def getDiasDisputa(self):
        return(self.diasDisputa)
    

class DisciplinaCurricular(Disciplina):
    def __init__(self, nome, dias, duracao, horaInicio, horaFim, aptidao):
        super().__init__(nome, dias, duracao, horaInicio, horaFim)
        self.anotacoes = []
        self.listas = []
        self.provas = []
        self.duvidas = []
        self.bibliografia = []
        self.aptidao = aptidao
        
    def addAnotacoes(self, data, texto):
        self.anotacoes.append(Anotacoes(data, texto))
    
    def addListas(self, data):
        self.listas.append(Listas(data))
        
    def addProvas(self, data):
        for i in range(len(self.provas)):
            if self.provas[i].getData == data:
                print("Erro: Já há uma prova registrada nesse dia e nesta disciplina!")
            else:
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
            if self.provas[i] < dia:
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

    def isApto(self, aptidoes):
        return aptidoes[self.aptidao]


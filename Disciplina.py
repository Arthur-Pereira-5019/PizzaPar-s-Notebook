from Anotacoes import Anotacoes
from Listas import Listas
from Provas import Provas
from Duvidas import Duvidas

class Disciplina:
    def __init__(self, nome, dias, duracao, hora):
        self.nome = nome
        self.dias = dias
        self.duracao = duracao
        self.hora = hora
        
    def get_nome(self):
        return(self.nome)
    
    def get_dias(self):
        return(self.dias)
    
    def get_duracao(self):
        return(self.duracao)
    
    def get_hora(self):
        return(self.hora)
    

class DisciplinaEsportiva(Disciplina):
    def __init__(self, nome, dias, duracao, hora, diasDisputa):
        super().__init__(nome, dias, duracao, hora)
        self.diasDisputa = diasDisputa
        
    def getDiasDisputa(self):
        return(self.diasDisputa)
    

class DisciplinaCurricular(Disciplina):
    def __init__(self, nome, dias, duracao, hora, diasAtendimento):
        super().__init__(nome, dias, duracao, hora)
        self.diasAtendimento = diasAtendimento
        self.anotacoes = []
        self.listas = []
        self.provas = []
        self.duvidas = []
        self.bibliografia = []
        
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
        
    def addDuvidas(self, data, texto):
        self.duvidas.append(Duvidas(data, texto))
        
    def addBibliografia(self, livro):
        self.bibliografia.append(livro)

    def getProvas(self):
        return self.provas

    def getBibliografia(self):
        return self.bibliografia

    def nDisciplinasPreProva(self, prova: Provas):
        n = 0
        for i in range(len(self.listas)):
            if not self.listas[i].getFeita() and self.listas[i].getData() < prova.getData():
                n+=1
        return n
    
        
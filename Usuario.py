import re
from Disciplina import *
from MochilaDeLivros import *

class Usuario():
    def __init__(self, nome: str, email: str, senha: str, curso: str):
        self.aptidoes = []
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curso = curso
        self.publica = False
        self.disciplinas: list[Disciplina] = []
        self.mochilaDeLivros = MochilaDeLivros()

    def isPublica(self):
        return self.publica
    
    def switchPublicidade(self):
        self.publica = not self.publica
        
    def setAptidoes(self,novasAptidoes):
        self.aptidoes = novasAptidoes
    
    def setSenha(self, senha: str):
        self.senha = senha

    def getSenha(self):
        return self.senha
    
    def getEmail(self):
        return self.email

    def addDisciplina(self, nome, dias, duracao, hora):
        self.disciplinas.append(Disciplina(nome, dias, duracao, hora))

    def addDisciplinaEsportiva(self, nome, dias, duracao, hora, diasDisputa):
        self.disciplinas.append(DisciplinaEsportiva(nome, dias, duracao, hora, diasDisputa))

    def addDisciplinaCurricular(self, nome, dias, duracao, hora, diasAtendimento):
        self.disciplinas.append(DisciplinaCurricular(nome, dias, duracao, hora, diasAtendimento))

    def getDisciplinas(self):
        return self.disciplinas

    def setCurso(self, curso: str):
        self.curso = curso

    def setNome(self, nome: str):
        self.nome = nome


    # Restrição de só uma prova por disciplina
    def provasHoje(self,dia:date):
        provasHoje = []
        dcs = self.getDisciplinasCurriculares()
        for i in range(len(dcs)):
            disciplina = dcs[i]
            provas = disciplina.getProvas()
            for j in range(len(provas)):
                if provas[j].getData == dia:
                    provasHoje.append(disciplina)
        return provasHoje

    def getDisciplinasCurriculares(self) -> list[DisciplinaCurricular]:
        dcs = []
        disciplinas = self.disciplinas
        for i in range(len(disciplinas)):
            if isinstance(disciplinas[i], DisciplinaCurricular):
                dcs.append(self.disciplinas[i])
        return dcs

    def exibirDisciplinasCurriculares(self):
        dcs = self.getDisciplinasCurriculares()
        for i in range(len(dcs)):
            print(f"{i+1}. {dcs[i].get_nome()}")

    def getCurso(self):
        return self.curso

    def aptidoesString(self):
        return f"Aptidões"

    def removerDisciplinasCurriculares(self):
        dcs = self.getDisciplinasCurriculares()
        ldcs = len(dcs)
        for i in range(ldcs):
            self.disciplinas.remove(dcs[i])
        print(f"Removidas {ldcs} disciplinas curriculares com sucesso.")

    def removerTodasDisciplinas(self):
        lds = len(self.disciplinas)
        self.disciplinas = []
        print(f"Removidas {lds} disciplinas curriculares com sucesso.")

    def disciplinasSugeridas(self,n: int,dia: date):
        retorno = sorted(self.getDisciplinasCurriculares(), key=lambda d: (d.diasAteAProximaProva(dia), d.getMediaIndefinida(dia), d.isApto(self.aptidoes), d.getListasPreProximaProva(dia)))
        return retorno[0:n-1]

    def disciplinasDeHoje(self, dds):
        retorno = []
        for i in range(len(self.disciplinas)):
            if self.disciplinas[i].dias.contains(dds):
                retorno.append(self.disciplinas[i])
        return retorno

    def __str__(self):
        return f"{self.nome} - {self.email} ({self.curso})"

    def __eq__(self, other):
        return self.email == other.email
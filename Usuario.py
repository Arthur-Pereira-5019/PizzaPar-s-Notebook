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
        
    def setAptidoes(self,linguagens,matematica,humanas,naturezas):
        novasAptidoes = []
        if(linguagens):
            novasAptidoes.append("Linguagens")
        if(matematica):
            novasAptidoes.append("Matemática")
        if(humanas):
            novasAptidoes.append("Humanas")
        if(naturezas):
            novasAptidoes.append("Naturezas")
        self.aptidoes = novasAptidoes
    
    def setSenha(self, senha: str):
        senha = senha
    
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

    def provasHoje(self,dia:date):
        provasHoje = []
        for i in range(len(self.disciplinas)):
            disciplina = self.disciplinas[i]
            if isinstance(disciplina,DisciplinaCurricular):
                provas = disciplina.getProvas()
                for j in range(len(provas)):
                    if provas[j].getData == dia:
                        provasHoje.append(disciplina)
        return provasHoje

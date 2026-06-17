import re
class Usuario():
    def __init__(self, nome: str, email: str, senha: str, curso: str):
        self.aptidoes = []
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curso = curso
        self.publica = False
        self.bu_multa = 0
        self.bu_renovacoes = 0
        self.bu_tempo_emprestimo = 0
        self.bu_distancia = 0
    
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
        
    
    
from Anotacoes import Anotacoes

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
        
    def addAnotacoes(self, data, texto):
        self.anotacoes.append(Anotacoes(data, texto))
        
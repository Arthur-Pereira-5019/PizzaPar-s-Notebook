class Provas:
    def __init__(self, data):
        self.data = data
        self.nota = -1
        
    def setNota(self, nota):
        self.nota = nota
    
    def getNota(self):
        if self.nota != -1:
            return self.nota
        else:
            return 0

    def getData(self):
        return self.data
    
    
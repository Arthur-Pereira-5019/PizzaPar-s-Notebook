class Listas:
    def __init__(self, data):
        self.data = data
        self.feita = False
        
    def fazer(self):
        self.feita = True
    
    def getFeita(self):
        return self.feita

    def getFeitaString(self):
        if self.feita:
            return("Feita")
        return("Incompleta")

    def getData(self):
        return self.data
    
    
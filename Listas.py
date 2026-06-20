class Listas:
    def __init__(self, data):
        self.data = data
        self.feita = False
        
    def Fazer(self):
        self.feita = True
    
    def getFeita(self):
        return self.feita

    def getData(self):
        return self.data
    
    
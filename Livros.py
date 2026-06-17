from datetime import date, datetime, timedelta
class Livro():
    def __init__(self, nome: str, autor: str, edicao: int):
        self.nome = nome
        self.data_de_emprestimo = None
        self.autor = autor
        self.edicao = edicao
        self.emprestado = False

    def __init__(self, nome: str, data_de_emprestimo: date, autor: str, edicao: int):
        self.nome = nome
        self.data_de_emprestimo = data_de_emprestimo
        self.autor = autor
        self.edicao = edicao
        self.emprestado = True
    def pegar(self, dia: date):
        if(self.emprestado == False):
            self.emprestado = True
            self.data_de_emprestimo = dia
        else:
            print("Você já está com este livro!")
    def devolver(self):
        if(self.emprestado == True):
            self.emprestado = False
            self.data_de_emprestimo = None
        else:
            print("Você não possui este livro para devolvê-lo.")

    def em_atraso(self, dia: date):
        if(self.emprestado == True):
            offset = self.dias_ate_vencer(dia)
            if offset < 0:
                print(f"O livro está atrasado em {offset} dias")
            else:
                print(f"O livro não está atrasado.")
        else:
            print("Você não está com esse livro.")

    def dias_ate_vencer(self, dia: date):
        return (self.data_de_emprestimo-dia).days


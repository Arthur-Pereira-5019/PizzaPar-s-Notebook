from datetime import date, datetime, timedelta
class Livro:
    def __init__(self, titulo: str, autor: str, edicao: int):
        self.titulo = titulo
        self.data_de_emprestimo = None
        self.autor = autor
        self.edicao = edicao
        self.emprestado = False
        self.data_de_devolucao = None

    def pegar(self, dia: date, prazo_devolucao: int):
        if not self.emprestado:
            self.emprestado = True
            self.data_de_emprestimo = dia
            self.data_de_devolucao = dia + timedelta(prazo_devolucao)
        else:
            print("Você já está com este livro!")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            self.data_de_emprestimo = None
        else:
            print("Você não possui este livro para devolvê-lo.")

    def em_atraso(self, dia: date):
        if self.emprestado:
            offset = self.dias_ate_vencer(dia)
            if offset < 0:
                print(f"O livro está atrasado em {offset} dias")
            else:
                print(f"O livro não está atrasado.")
        else:
            print("Você não está com esse livro.")

    def dias_ate_vencer(self, dia: date):
        return (self.data_de_devolucao-dia).days

    def calcularMulta(self, taxa: float, dia: date):
        t = self.dias_ate_vencer(dia)
        if t > 0:
            return 0.0
        else:
            return t*taxa

    def exibicao(self,taxa,date):
        if not self.emprestado:
            return f"{self.titulo} {self.edicao}ed {self.autor}"
        return f"{self.titulo} {self.edicao}ed {self.autor}. Devolução: {self.data_de_devolucao}. Multa: {self.calcularMulta()}R$"

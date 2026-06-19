from datetime import date, datetime, timedelta
class ModuloTempo:
    offsetDias = 0
    dias_da_semana = {0:"Segunda-Feira",1:"Terça-Feira",2:"Quarta-Feira",3:"Quinta-Feira",4:"Sexta-Feira",5:"Sábado",6:"Domingo"}

    def data_de_hoje(self):
        return date.today()+timedelta(self.offsetDias)

    def dia_da_semana(self):
        return self.data_de_hoje().weekday()

    def exibir_dia_da_semana(self):
        return self.dias_da_semana[self.dia_da_semana()]

    def exibir_data(self):
        hoje = self.data_de_hoje()
        return f"{hoje.day}/{hoje.month}/{hoje.year} ({self.exibir_dia_da_semana()})"
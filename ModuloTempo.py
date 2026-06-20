from datetime import date, datetime, timedelta
offsetDias = 0
dias_da_semana = {0:"Segunda-Feira",1:"Terça-Feira",2:"Quarta-Feira",3:"Quinta-Feira",4:"Sexta-Feira",5:"Sábado",6:"Domingo"}

def data_de_hoje():
    return date.today()+timedelta(offsetDias)

def dia_da_semana():
    return data_de_hoje().weekday()

def exibir_dia_da_semana():
    return dias_da_semana[dia_da_semana()]

def exibir_data():
    hoje = data_de_hoje()
    return f"{hoje.day}/{hoje.month}/{hoje.year} ({exibir_dia_da_semana()})"
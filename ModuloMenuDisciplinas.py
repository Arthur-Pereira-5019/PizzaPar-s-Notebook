from datetime import date, datetime, timedelta
from UsuarioService import *
from Disciplina import *
from Livros import *
from MochilaDeLivros import *
import ModuloTempo as mt

def adicionar_disciplinas_curriculares(usuario_logado: Usuario):
    nome = input("Nome da Disciplina: ")
    dias = input("Dias de aula:\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n").split()
    invalido = True
    while invalido:
        invalido = False
        for i in dias:
            if i not in ['1', '2', '3', '4', '5']:
                invalido = True
                print("Data inválida, tente novamente")
                dias = input(
                    "Dias de aula:\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n").split()
    for j in range(len(dias)):
        dias[j] = int(dias[j]) - 1

    duracao = str(input("Duração da disciplina (em dias): "))
    print(type(duracao))
    invalido = True
    while invalido:
        invalido = False
        if not str(duracao).isnumeric():
            invalido = True
            print("Duração inválida, tente novamente")
            duracao = input("Duração da disciplina (em dias): ")

    horario = input("Horario (HH:MM): ")
    invalido = True
    while invalido:
        invalido = False
        if horario.split(":")[0].isnumeric() and horario.split(":")[1].isnumeric():
            if len(horario.split(":")) != 2 or len(horario.split(":")[0]) != 2 or len(
                    horario.split(":")[1]) != 2 or int(horario.split(":")[0]) >= 24 or int(
                    horario.split(":")[1]) >= 60:
                invalido = True
                print("Horário inválido, tente novamente")
                horario = input("Horario: ")
        else:
            invalido = True
            print("Horário inválido, tente novamente")
            horario = input("Horario: ")

    atendimento = input("Dias de Atendimento:\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n")
    invalido = True
    while invalido:
        invalido = False
        for i in dias:
            if i not in ['1', '2', '3', '4', '5']:
                invalido = True
                print("Data inválida, tente novamente")
                atendimento = input(
                    "Dias de Atendimento:\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n").split()

    horario = input("Horario (HH:MM): ")
    invalido = True
    while invalido:
        invalido = False
        if horario.split(":")[0].isnumeric() and horario.split(":")[1].isnumeric():
            if len(horario.split(":")) != 2 or len(horario.split(":")[0]) != 2 or len(
                    horario.split(":")[1]) != 2 or int(horario.split(":")[0]) >= 24 or int(
                horario.split(":")[1]) >= 60:
                invalido = True
                print("Horário inválido, tente novamente")
                horario = input("Horario: ")
        else:
            invalido = True
            print("Horário inválido, tente novamente")
            horario = input("Horario: ")
    ap_numero = 0
    while True:
        aptidao = input("Digite qual é a aptidao que melhor descreve essa disciplina? [Linguagens]/["
                        "Matematica]/Ciências [Humanas] e Sociais/Ciências da [Natureza]")
        aptidao = aptidao.lower()
        if aptidao == "linguagens":
            ap_numero = 0
            break
        elif aptidao == "matematica":
            ap_numero = 1
            break
        elif aptidao == "humanas":
            ap_numero = 2
            break
        elif aptidao == "natureza":
            ap_numero = 3
            break
    estado_disciplina = usuario_logado.addDisciplinaCurricular(nome, dias, duracao, horaInicio, horaFim, ap_numero)
    print("Disciplina registrada com sucesso! Agora vamos registrar a bibliografia dessa disciplina.")
    return "Cadastrando Livros 1", usuario_logado, estado_disciplina


def adicionar_disciplinas_esportivas(usuario_logado: Usuario):
    nome = input("Nome da Disciplina: ")
    print("Digite a lista de dias de disciplina, separados por espaços em branco.")
    dias = input("Dias de aula:\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n").split()
    invalido = True
    while invalido:
        invalido = False
        for i in dias:
            if i not in ['1', '2', '3', '4', '5']:
                invalido = True
                print("Data inválida, tente novamente")
                dias = input("Dias de aula:\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n").split()
    for j in range(len(dias)):
        dias[j] = int(dias[j])-1

    duracao = str(input("Duração da disciplina (em dias): "))
    print(type(duracao))
    invalido = True
    while invalido:
        invalido = False
        if not str(duracao).isnumeric():
            invalido = True
            print("Duração inválida, tente novamente")
            duracao = input("Duração da disciplina (em dias): ")

    horaInicio = input("Horario de inicio (HH:MM): ")
    invalido = True
    while invalido:
        invalido = False
        if horaInicio.split(":")[0].isnumeric() and horaInicio.split(":")[1].isnumeric():
            if len(horaInicio.split(":")) != 2 or len(horaInicio.split(":")[0]) != 2 or len(
                    horaInicio.split(":")[1]) != 2 or int(horaInicio.split(":")[0]) >= 24 or int(
                horaInicio.split(":")[1]) >= 60:
                invalido = True
                print("Horário inválido, tente novamente")
                horaInicio = input("Horario: ")
        else:
            invalido = True
            print("Horário inválido, tente novamente")
            horaInicio = input("Horario: ")

    horaFim = input("Horario de fim (HH:MM): ")
    invalido = True
    while invalido:
        invalido = False
        if horaFim.split(":")[0].isnumeric() and horaFim.split(":")[1].isnumeric():
            if len(horaFim.split(":")) != 2 or len(horaFim.split(":")[0]) != 2 or len(
                    horaFim.split(":")[1]) != 2 or int(horaFim.split(":")[0]) >= 24 or int(
                horaFim.split(":")[1]) >= 60:
                invalido = True
                print("Horário inválido, tente novamente")
                horaFim = input("Horario: ")
        else:
            invalido = True
            print("Horário inválido, tente novamente")
            horaFim = input("Horario: ")

    # dias_de_disputa = input("Dias de Disputa (DD/MM): ")
    # invalido = True
    # while invalido:
    #     invalido = False
    #     if dias_de_disputa.split("/")[0].isnumeric() and dias_de_disputa.split("/")[1].isnumeric():
    #         if len(dias_de_disputa.split("/")) != 2 or len(dias_de_disputa.split("/")[0]) != 2 or len(
    #                 dias_de_disputa.split("/")[1]) != 2 or (
    #                 int(dias_de_disputa.split("/")[0]) > 30 and int(dias_de_disputa.split("/")[1]) in [4, 6, 8, 10,
    #                                                                                                    12]) or (
    #                 int(dias_de_disputa.split("/")[0]) > 31 and int(dias_de_disputa.split("/")[1]) in [1, 3, 5, 7,
    #                                                                                                    9, 11]) or (
    #                 int(dias_de_disputa.split("/")[0]) > 28 and int(dias_de_disputa.split("/")[1]) in [
    #             2] and mt.ano_e_bissexto() == False) or (int(dias_de_disputa.split("/")[0]) > 29 and int(
    #             dias_de_disputa.split("/")[1]) == 2 and mt.ano_e_bissexto() == True) or int(
    #             dias_de_disputa.split("/")[1]) > 12:
    #             invalido = True
    #             print("Dias inválidos, tente novamente")
    #             dias_de_disputa = input("Dias de Disputa (DD/MM): ")
    #     else:
    #         invalido = True
    #         print("Dias inválidos, tente novamente")
    #         dias_de_disputa = input("Dias de Disputa (DD/MM): ")
    usuario_logado.addDisciplinaEsportiva(nome, dias, duracao, horaInicio, horaFim) #, dias_de_disputa )
    return "Menu",usuario_logado


def estado_consultando_esportivas(usuario_logado: Usuario):
    hoje = mt.data_de_hoje()
    print("Você deseja: [Remover] uma disciplina esportiva.\n[Adicionar] uma disciplina.\n[Marcar] um dia de "
          "disputa.\n[Desmarcar] uma disputa\n[Sair]")
    while True:
        op = input()
        op = op.lower()
        indice = 0
        if op == "remover" or op == "marcar" or op == "desmarcar":
            usuario_logado.exibirDisciplinasEsportivas()
            limite = len(usuario_logado.getDisciplinasEsportivas())
            while True:
                indice = int(input()) - 1
                if indice < 0 or indice >= limite:
                    print("Índice fora do escopo, digite novamente")
                else:
                    break
        if op == "remover":
            usuario_logado.removerDisciplinaEsportivaPeloIndice(indice)
            print("Disciplina removida com sucesso!")
            return "Consultando Esportivas", usuario_logado
        elif op == "adicionar":
            return "Adicionando Disciplinas 2", usuario_logado
        elif op == "marcar":
            # TODO Pega o input que tá no construtor de disciplinas esportivas, coloca no métod0 acessório ali
            usuario_logado.adicionaDisputas(indice)
        elif op == "desmarcar":
            disciplinaEsportiva = usuario_logado.getDisciplinaEsportivaPeloIndice(indice)
            disciplinaEsportiva.exibirDiasDisputa(hoje)
            limite = len(disciplinaEsportiva.getProximasDisputas(hoje))
            while True:
                indice = int(input()) - 1
                if indice < 0 or indice >= limite:
                    print("Índice fora do escopo, digite novamente")
                else:
                    break
            disciplinaEsportiva.removerDisputaPeloIndice(indice, hoje)
            print("Disputa removida da sua agenda com sucesso!")
        elif op == "Sair":
            return "Menu", usuario_logado
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")


def estado_consultando_curriculares(usuario_logado: Usuario):
    print("Você deseja: [Remover] uma disciplina curricular.\n[Adicionar] uma disciplina.\nConsultar suas [Provas],Consultar suas [listas]."
          "disputa.\n[Sair]")
    while True:
        op = input()
        op = op.lower()
        if op == "remover":
            usuario_logado.exibirDisciplinasEsportivas()
            limite = len(usuario_logado.getDisciplinasEsportivas())
            indice = 0
            while True:
                indice = int(input())-1
                if indice < 0 or indice >= limite:
                    print("Índice fora do escopo, digite novamente")
                else:
                    break
            usuario_logado.removerDisciplinaEsportivaPeloIndice(indice)
            print("Disciplina removida com sucesso!")
            estado = "Consultando Esportivas"
            break
        elif op == "adicionar":
            estado = "Adicionando Disciplinas"
            break
        elif op == "marcar":
            usuario_logado.exibirDisciplinasEsportivas()
            limite = len(usuario_logado.getDisciplinasEsportivas())
            indice = 0
            while True:
                indice = int(input())-1
                if indice < 0 or indice >= limite:
                    print("Índice fora do escopo, digite novamente")
                else:
                    break
            # TODO Pega o input que tá no construtor de disciplinas esportivas, coloca no métod0 acessório ali
            usuario_logado.adicionaDisputas(indice)
        elif op == "Sair":
            estado = "Menu"
            break
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")
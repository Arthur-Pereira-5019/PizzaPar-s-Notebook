from datetime import date, datetime, timedelta
from UsuarioService import *
from Disciplina import *
from Livros import *
from MochilaDeLivros import *
import ModuloTempo as mt

def adicionar_disciplinas_curriculares(usuario_logado: Usuario):
    dias_por_indice = {1:"Segunda", 2:"Terça", 3:"Quarta", 4:"Quinta", 5:"Sexta"}
    nome = input("Nome da Disciplina: ")
    dias = input("Dias de aula (Informe em lista separada por espaços):\n[1]- Segunda\n[2]- Terça\n[3]- Quarta\n[4]- Quinta\n[5]- Sexta\n").split()
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

    duracao = input("Duração da disciplina em dias (O sistema poderá arredondar o número de aulas): ")
    #print(type(duracao))
    invalido = True
    while invalido:
        invalido = False
        if not str(duracao).isnumeric():
            invalido = True
            print("Duração inválida, tente novamente.")
            duracao = input("Duração da disciplina em dias (O sistema poderá arredondar o número de aulas): ")
    duracao = int(duracao)

    horaInicio = []
    horaFim = []
    for i in range(len(dias)):
        print("Horário de inicio na", dias_por_indice[int(dias[i]) + 1], "(HH:MM): ", end='')
        horaInicio_try = input()
        invalido = True
        while invalido:
            invalido = False
            if horaInicio_try.split(":")[0].isnumeric() and horaInicio_try.split(":")[1].isnumeric():
                if len(horaInicio_try.split(":")) != 2 or len(horaInicio_try.split(":")[0]) != 2 or len(
                        horaInicio_try.split(":")[1]) != 2 or int(horaInicio_try.split(":")[0]) >= 24 or int(
                    horaInicio_try.split(":")[1]) >= 60:
                    invalido = True
                    print("Horário inválido, tente novamente")
                    horaInicio_try = input("Horario: ")
            else:
                invalido = True
                print("Horário inválido, tente novamente")
                horaInicio_try = input("Horário: ")
        horaInicio.append(horaInicio_try)

        print("Horário de fim na ", dias_por_indice[int(dias[i]) + 1], " (HH:MM): ", end='')
        horaFim_try = input()
        invalido = True
        while invalido:
            invalido = False
            if horaFim_try.split(":")[0].isnumeric() and horaFim_try.split(":")[1].isnumeric():
                if len(horaFim_try.split(":")) != 2 or len(horaFim_try.split(":")[0]) != 2 or len(
                        horaFim_try.split(":")[1]) != 2 or int(horaFim_try.split(":")[0]) >= 24 or int(
                    horaFim_try.split(":")[1]) >= 60:
                    invalido = True
                    print("Horário inválido, tente novamente")
                    horaFim_try = input("Horario: ")
            else:
                invalido = True
                print("Horário inválido, tente novamente")
                horaFim_try = input("Horario: ")
        horaFim.append(horaFim_try)
        disciplinasDeHoje = usuario_logado.disciplinasDeHoje(dias[i])
        for j in disciplinasDeHoje:
            hI = j.getHoraInicioHoje(dias[i])
            hF = j.getHoraFimHoje(dias[i])
            print((hI), (hF))
            if hI != "" and hF != "":
                if hI < horaInicio[-1] < hF or hI < horaFim[-1] < hF:
                    print("Cuidado! Há um conflito de horário com a disciplina:", j.get_nome())
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
    dias_por_indice = {1: "Segunda", 2: "Terça", 3: "Quarta", 4: "Quinta", 5: "Sexta"}
    nome = input("Nome da Disciplina Esportiva: ")
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

    duracao = input("Duração da disciplina em dias (O sistema poderá arredondar o número de aulas): ")
    #print(type(duracao))
    invalido = True
    while invalido:
        invalido = False
        if not str(duracao).isnumeric():
            invalido = True
            print("Duração inválida, tente novamente")
            duracao = input("Duração da disciplina em dias (O sistema poderá arredondar o número de aulas): ")

    duracao = int(duracao)

    horaInicio = []
    horaFim = []
    for i in range(len(dias)):
        print("Horario de inicio na ", dias_por_indice[int(dias[i]) + 1], " (HH:MM): ", end='')
        horaInicio_try = input()
        invalido = True
        while invalido:
            invalido = False
            if horaInicio_try.split(":")[0].isnumeric() and horaInicio_try.split(":")[1].isnumeric():
                if len(horaInicio_try.split(":")) != 2 or len(horaInicio_try.split(":")[0]) != 2 or len(
                        horaInicio_try.split(":")[1]) != 2 or int(horaInicio_try.split(":")[0]) >= 24 or int(
                    horaInicio_try.split(":")[1]) >= 60:
                    invalido = True
                    print("Horário inválido, tente novamente")
                    horaInicio_try = input("Horario: ")
            else:
                invalido = True
                print("Horário inválido, tente novamente")
                horaInicio_try = input("Horario: ")
        horaInicio.append(horaInicio_try)

        print("Horario de fim na ", dias_por_indice[int(dias[i]) + 1], " (HH:MM): ", end='')
        horaFim_try = input()
        invalido = True
        while invalido:
            invalido = False
            if horaFim_try.split(":")[0].isnumeric() and horaFim_try.split(":")[1].isnumeric():
                if len(horaFim_try.split(":")) != 2 or len(horaFim_try.split(":")[0]) != 2 or len(
                        horaFim_try.split(":")[1]) != 2 or int(horaFim_try.split(":")[0]) >= 24 or int(
                    horaFim_try.split(":")[1]) >= 60:
                    invalido = True
                    print("Horário inválido, tente novamente")
                    horaFim_try = input("Horario: ")
            else:
                invalido = True
                print("Horário inválido, tente novamente")
                horaFim_try = input("Horario: ")
        horaFim.append(horaFim_try)
        
        disciplinasDeHoje = usuario_logado.disciplinasDeHoje(dias[i])
        for j in disciplinasDeHoje:
            hI = j.getHoraInicioHoje(dias[i])
            hF = j.getHoraFimHoje(dias[i])
            print((hI), (hF))
            if hI != "" and hF != "":
                if hI < horaInicio[-1] < hF or hI < horaFim[-1] < hF:
                    print("Cuidado! Há um conflito de horário com a disciplina: ", j.get_nome())

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
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")
        if op == "remover":
            usuario_logado.removerDisciplinaEsportivaPeloIndice(indice)
            print("Disciplina removida com sucesso!")
            return "Consultando Esportivas", usuario_logado
        elif op == "adicionar":
            return "Adicionando Disciplinas 2", usuario_logado
        elif op == "marcar":
            # TODO Pega o input que tá no construtor de disciplinas esportivas, coloca no métod0 acessório ali
            usuario_logado.adicionaDisputas(indice)
            return "Consultando Esportivas", usuario_logado
        elif op == "desmarcar":
            disciplinaEsportiva = usuario_logado.getDisciplinaEsportivaPeloIndice(indice)
            disciplinaEsportiva.exibirDiasDisputa(hoje)
            limite = len(disciplinaEsportiva.getProximasDisputas(hoje))
            while True:
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")
            disciplinaEsportiva.removerDisputaPeloIndice(indice, hoje)
            print("Disputa removida da sua agenda com sucesso!")
            return "Consultando Esportivas", usuario_logado
        elif op == "sair":
            return "Menu", usuario_logado
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")


def estado_consultando_curriculares(usuario_logado: Usuario):
    print("Você deseja: [Remover] uma disciplina curricular.\n[Adicionar] uma disciplina.\nConsultar suas [Provas]\nConsultar suas [listas]\n[Sair]")
    while True:
        op = input()
        op = op.lower()
        if op == "remover":
            usuario_logado.exibirDisciplinasCurriculares()
            limite = len(usuario_logado.getDisciplinasCurriculares())
            indice = 0
            while True:
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")
            usuario_logado.removerDisciplinaCurricularPeloIndice(indice)
            print("Disciplina removida com sucesso!")
            return "Consultando Curriculares", usuario_logado
        elif op == "adicionar":
            return "Adicionando Disciplinas 1", usuario_logado
        elif op == "provas":

            estado_consultando_provas(usuario_logado)
            return "Consultando Curriculares", usuario_logado
        elif op == "listas":

            estado_consultando_listas(usuario_logado)
            return "Consultando Curriculares", usuario_logado
        elif op == "sair":
            return "Menu", usuario_logado
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")


def estado_consultando_listas(usuario_logado: Usuario):
    hoje = mt.data_de_hoje()
    limite = len(usuario_logado.getDisciplinasCurriculares())
    indice = 0
    usuario_logado.exibirDisciplinasCurriculares()
    while True:
        indice_str = input()
        if indice_str.isnumeric():
            indice = int(indice_str) - 1
            if indice < 0 or indice >= limite:
                print("Índice fora do escopo, digite novamente")
            else:
                break
        else:
            print("Índice inválido. Esperando um número.")

    print("Você deseja: [Remover] uma lista.\n[Adicionar] uma lista.\n[Fazer] uma lista\n[Sair]")
    while True:
        op = input()
        op = op.lower()
        if op == "remover":
            disciplinaCurricular = usuario_logado.getDisciplinaCurricularPeloIndice(indice)
            limite = len(disciplinaCurricular.getListas())
            disciplinaCurricular.exibirListas()
            while True:
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")
            print(disciplinaCurricular.getListas())
            disciplinaCurricular.removerListaPeloIndice(indice)
            print("Lista removida com sucesso!")
            return "Consultando Curriculares", usuario_logado

        elif op == "adicionar":
            usuario_logado.adicionaListas(indice)
            return "Consultando Curriculares", usuario_logado

        elif op == "fazer":
            disciplinaCurricular = usuario_logado.getDisciplinaCurricularPeloIndice(indice)
            limite = len(disciplinaCurricular.getListas())
            disciplinaCurricular.exibirListas()
            while True:
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")

            disciplinaCurricular.getListas()[indice].fazer()
            print("Nota registrada com sucesso!")
            return "Consultando Curriculares", usuario_logado

        elif op == "sair":
            return "Consultando Curriculares", usuario_logado
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")


def estado_consultando_provas(usuario_logado: Usuario):
    hoje = mt.data_de_hoje()
    limite = len(usuario_logado.getDisciplinasCurriculares())
    indice = 0
    usuario_logado.exibirDisciplinasCurriculares()
    while True:
        indice_str = input()
        if indice_str.isnumeric():
            indice = int(indice_str) - 1
            if indice < 0 or indice >= limite:
                print("Índice fora do escopo, digite novamente")
            else:
                break
        else:
            print("Índice inválido. Esperando um número.")

    print("Você deseja: [Remover] uma prova.\n[Adicionar] uma prova.\nDefinir a [nota] de uma prova\n[Sair]")
    while True:
        op = input()
        op = op.lower()
        if op == "remover":
            disciplinaCurricular = usuario_logado.getDisciplinaCurricularPeloIndice(indice)
            limite = len(disciplinaCurricular.getProvas())
            disciplinaCurricular.exibirDiasDeProva()
            while True:
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")
            disciplinaCurricular.removerProvaPeloIndice(indice)
            print("Prova removida com sucesso!")
            return "Consultando Curriculares", usuario_logado

        elif op == "adicionar":
            usuario_logado.adicionaProvas(indice)
            return "Consultando Curriculares", usuario_logado

        elif op == "nota":
            disciplinaCurricular = usuario_logado.getDisciplinaCurricularPeloIndice(indice)
            limite = len(disciplinaCurricular.getProvas())
            disciplinaCurricular.exibirDiasDeProva()
            while True:
                indice_str = input()
                if indice_str.isnumeric():
                    indice = int(indice_str) - 1
                    if indice < 0 or indice >= limite:
                        print("Índice fora do escopo, digite novamente")
                    else:
                        break
                else:
                    print("Índice inválido. Esperando um número.")

            nota = input("Nota a ser marcada: ")
            while True:
                if nota.isnumeric() and 0 <= float(nota) <= 10:
                    nota = float(nota)
                    break
                else:
                    print("Valor invalido, tente novamente")

            disciplinaCurricular.getProvas()[indice].setNota(nota)
            print("Nota registrada com sucesso!")
            return "Consultando Curriculares", usuario_logado

        elif op == "sair":
            return "Consultando Curriculares", usuario_logado
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")


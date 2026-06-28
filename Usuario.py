import re
from Disciplina import *
from MochilaDeLivros import *

class Usuario():
    def __init__(self, nome: str, email: str, senha: str, curso: str):
        self.aptidoes = [False, False, False, False]
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curso = curso
        self.publica = False
        self.disciplinas: list[Disciplina] = []
        self.mochilaDeLivros = MochilaDeLivros()

    def isPublica(self):
        return self.publica

    def switchPublicidade(self):
        self.publica = not self.publica

    def setAptidoes(self,novasAptidoes):
        self.aptidoes = novasAptidoes

    def setSenha(self, senha: str):
        self.senha = senha

    def getSenha(self):
        return self.senha

    def getEmail(self):
        return self.email

    def addDisciplinaEsportiva(self, nome, dias, duracao, horaInicio, horaFim):
        self.disciplinas.append(DisciplinaEsportiva(nome, dias, duracao, horaInicio, horaFim))

    def addDisciplinaCurricular(self, nome, dias, duracao, horaInicio, horaFim, aptidao):
        disciplina = DisciplinaCurricular(nome, dias, duracao, horaInicio, horaFim, aptidao)
        self.disciplinas.append(disciplina)
        return disciplina

    def getDisciplinas(self):
        return self.disciplinas

    def setCurso(self, curso: str):
        self.curso = curso

    def setNome(self, nome: str):
        self.nome = nome


    # Restrição de só uma prova por disciplina
    def provasHoje(self,dia:date):
        provasHoje = []
        dcs = self.getDisciplinasCurriculares()
        for i in range(len(dcs)):
            disciplina = dcs[i]
            provas = disciplina.getProvas()
            for j in range(len(provas)):
                if provas[j].getData() == dia:
                    provasHoje.append(disciplina)
        return provasHoje

    def disputasHoje(self,dia:date):
        disputasHoje = []
        des = self.getDisciplinasEsportivas()
        for i in range(len(des)):
            disciplina = des[i]
            disputas = disciplina.getDiasDisputa()
            for j in range(len(disputas)):
                if disputas[j] == dia:
                    disputasHoje.append(disciplina)
        return disputasHoje

    def getDisciplinasCurriculares(self) -> list[DisciplinaCurricular]:
        dcs = []
        disciplinas = self.disciplinas
        for i in range(len(disciplinas)):
            if isinstance(disciplinas[i], DisciplinaCurricular):
                dcs.append(self.disciplinas[i])
        return dcs

    def getDisciplinasEsportivas(self) -> list[DisciplinaEsportiva]:
        des = []
        disciplinas = self.disciplinas
        for i in range(len(disciplinas)):
            if isinstance(disciplinas[i], DisciplinaEsportiva):
                des.append(self.disciplinas[i])
        return des

    def exibirDisciplinasCurriculares(self):
        dcs = self.getDisciplinasCurriculares()
        if dcs != []:
            for i in range(len(dcs)):
                print(f"{i+1}. {dcs[i].get_nome()}")
        else:
            print("Nenhuma disciplina curricular cadastrada.")

    def exibirDisciplinasEsportivas(self):
        des = self.getDisciplinasEsportivas()
        if des != []:
            for i in range(len(des)):
                print(f"{i+1}. {des[i].get_nome()}")
        else:
            print("Nenhuma disciplina esportiva cadastrada.")

    def getCurso(self):
        return self.curso

    def removerDisciplinasCurriculares(self):
        dcs = self.getDisciplinasCurriculares()
        ldcs = len(dcs)
        for i in range(ldcs):
            self.disciplinas.remove(dcs[i])
        print(f"Removidas {ldcs} disciplinas curriculares com sucesso.")

    def removerTodasDisciplinas(self):
        lds = len(self.disciplinas)
        self.disciplinas = []
        print(f"Removidas {lds} disciplinas curriculares com sucesso.")

    def removerDisciplinaCurricularPeloIndice(self, indice: int):
        dcs = self.getDisciplinasCurriculares()
        self.disciplinas.remove(dcs[indice])


    def adicionaDisputas(self, indiceRef):
        disciplinaRef = self.getDisciplinaEsportivaPeloIndice(indiceRef)
        indice = self.disciplinas.index(disciplinaRef)
        if indice is not None:
            dias_de_disputa = input("Dia de Disputa (DD/MM/YYYY): ")
            invalido = True
            while invalido:
                invalido = False
                if len(dias_de_disputa.split("/")) == 3:
                    if dias_de_disputa.split("/")[0].isnumeric() and dias_de_disputa.split("/")[1].isnumeric() and dias_de_disputa.split("/")[2].isnumeric():
                        if (len(dias_de_disputa.split("/")[0]) != 2 or len(dias_de_disputa.split("/")[1]) != 2
                                or (
                                int(dias_de_disputa.split("/")[0]) > 30 and int(dias_de_disputa.split("/")[1]) in [4, 6, 8,
                                                                                                                   10,
                                                                                                                   12]) or (
                                int(dias_de_disputa.split("/")[0]) > 31 and int(dias_de_disputa.split("/")[1]) in [1, 3, 5,
                                                                                                                   7,
                                                                                                                   9,
                                                                                                                   11]) or (
                                int(dias_de_disputa.split("/")[0]) > 28 and int(dias_de_disputa.split("/")[1]) in [
                            2] and mt.ano_e_bissexto() == False) or (int(dias_de_disputa.split("/")[0]) > 29 and int(
                            dias_de_disputa.split("/")[1]) == 2 and mt.ano_e_bissexto() == True) or int(
                            dias_de_disputa.split("/")[1]) > 12):
                            invalido = True
                            print("Dia inválido, tente novamente")
                            dias_de_disputa = input("Dia de Disputa (DD/MM/YYYY): ")
                    else:
                        invalido = True
                        print("Dias inválidos, tente novamente")
                        dias_de_disputa = input("Dia de Disputa (DD/MM/YYYY): ")
                else:
                    invalido = True
                    print(dias_de_disputa)
                    print("Formato inválido, tente novamente")
                    dias_de_disputa = input("Dia de Disputa (DD/MM/YYYY): ")
            dias_de_disputa = date(int(dias_de_disputa[6::]), int(dias_de_disputa[3:5:]), int(dias_de_disputa[:2:]))
            colisao = self.stringColisao(dias_de_disputa)
            self.disciplinas[indice].addDisputa(dias_de_disputa)
            if colisao != "":
                print(f"Há uma colisão de eventos neste dia com uma {colisao}, se certifique de atender ao mais importante e se organizar com antecedência.")

    def stringColisao(self, dia):
        if self.provasHoje(dia):
            return "prova"
        elif self.disputasHoje(dia):
            return "outra disputa"
        return ""

    def getDisciplinaCurricularPeloIndice(self, indice: int):
        dcs = self.getDisciplinasCurriculares()
        return dcs[indice]

    def getDisciplinaEsportivaPeloIndice(self, indice: int) -> DisciplinaEsportiva:
        dcs = self.getDisciplinasEsportivas()
        return dcs[indice]

    def removerDisciplinaEsportivaPeloIndice(self, indice: int):
        des = self.getDisciplinasEsportivas()
        self.disciplinas.remove(des[indice])

    def encontraDisciplinaPeloId(self, id):
        for i in range(len(self.disciplinas)):
            if self.disciplinas[i].id == id:
                return self.disciplinas[i]
        return None

    def disciplinasSugeridas(self,n: int,dia: date):
        retorno = sorted(self.getDisciplinasCurriculares(), key=lambda d: (d.pesoParaEstudar(dia,self.aptidoes)),reverse=True)
        return retorno[0:n]

    def getAptidoes(self):
        return self.aptidoes

    def disciplinasDeHoje(self, dds):
        retorno = []
        for i in range(len(self.disciplinas)):
            if dds in self.disciplinas[i].dias:
                retorno.append(self.disciplinas[i])
        return retorno

    def getDisciplinasConcluidas(self):
        retorno = []
        dcs = self.disciplinas
        for i in range(len(dcs)):
            if dcs[i].isConcluida():
                retorno.append(dcs[i])
        for i in range (len(retorno)):
            self.disciplinas.remove(retorno[i])
        return retorno

    def aptidoesToString(self):
        apt = ""
        if self.aptidoes[0]:
            apt += "Linguagens, "
        if self.aptidoes[1]:
            apt += "Matemática, "
        if self.aptidoes[2]:
            apt += "Ciências Humanas e Sociais, "
        if self.aptidoes[3]:
            apt += "Ciências da Natureza."
        if len(apt) == 0:
            return f"Nenhuma aptidão"
        if apt[len(apt) - 2:len(apt)] == ", ":
            apt = apt[0:len(apt) - 2] + "."
        return f"{apt}"

    def publicidadeToString(self):
        if self.isPublica():
            return "Pública"
        return "Privada"

    def getNListasAFazer(self):
        dcs = self.getDisciplinasCurriculares()
        total = 0
        for i in range (len(dcs)):
            total += dcs[i].getNListasAFazer()
        return total

    def darNotaParaDisciplinaPeloIndice(self, indiceRef: int, indiceProva:int, nota):
        dc = self.getDisciplinaCurricularPeloIndice(indiceRef)
        indice = self.disciplinas.index(dc)
        self.disciplinas[indice].darNotaPeloIndice(indiceProva, nota)


    def adicionaProvas(self, indiceRef):
        disciplinaRef = self.getDisciplinaCurricularPeloIndice(indiceRef)
        indice = self.disciplinas.index(disciplinaRef)
        if indice is not None:
            dias_de_prova = input("Dia de Prova (DD/MM/YYYY): ")
            invalido = True
            while invalido:
                invalido = False
                if len(dias_de_prova.split("/")) == 3:
                    if dias_de_prova.split("/")[0].isnumeric() and dias_de_prova.split("/")[1].isnumeric() and dias_de_prova.split("/")[2].isnumeric():
                        if (len(dias_de_prova.split("/")[0]) != 2 or len(dias_de_prova.split("/")[1]) != 2
                                or (
                                int(dias_de_prova.split("/")[0]) > 30 and int(dias_de_prova.split("/")[1]) in [4, 6, 8,
                                                                                                                   10,
                                                                                                                   12]) or (
                                int(dias_de_prova.split("/")[0]) > 31 and int(dias_de_prova.split("/")[1]) in [1, 3, 5,
                                                                                                                   7,
                                                                                                                   9,
                                                                                                                   11]) or (
                                int(dias_de_prova.split("/")[0]) > 28 and int(dias_de_prova.split("/")[1]) in [
                            2] and mt.ano_e_bissexto() == False) or (int(dias_de_prova.split("/")[0]) > 29 and int(
                            dias_de_prova.split("/")[1]) == 2 and mt.ano_e_bissexto() == True) or int(
                            dias_de_prova.split("/")[1]) > 12):
                            invalido = True
                            print("Dia inválido, tente novamente")
                            dias_de_prova = input("Dia de Prova (DD/MM/YYYY): ")
                    else:
                        invalido = True
                        print("Dias inválidos, tente novamente")
                        dias_de_prova = input("Dia de Prova (DD/MM/YYYY): ")
                else:
                    invalido = True
                    #print(dias_de_prova)
                    print("Formato inválido, tente novamente")
                    dias_de_prova = input("Dia de Prova (DD/MM/YYYY): ")
                dias_de_prova = date(int(dias_de_prova[6::]), int(dias_de_prova[3:5:]), int(dias_de_prova[:2:]))
                if dias_de_prova.weekday() in self.disciplinas[indice].get_dias():
                    #self.disciplinas[indice].addProvas(dias_de_prova)
                    print(
                        f"Sucesso, prova marcada no dia: {mt.exibir_data(dias_de_prova)} às {self.disciplinas[indice].getHoraInicioHoje(dias_de_prova.weekday())}")
                else:
                    print(dias_de_prova.weekday())
                    print(self.disciplinas[indice].get_dias())
                    print("Erro, prova marcada no dia sem a disciplina!")
                    dias_de_prova = input("Dia de Prova (DD/MM/YYYY): ")
                    invalido = True
            colisao = self.stringColisao(dias_de_prova)
            self.disciplinas[indice].addProvas(dias_de_prova)
            if colisao != "":
                print(f"Há uma colisão de eventos neste dia com uma {colisao}, se certifique de atender ao mais importante e se organizar com antecedência.")

    def adicionaListas(self, indiceRef):
        hoje = mt.data_de_hoje()
        disciplinaRef = self.getDisciplinaCurricularPeloIndice(indiceRef)
        indice = self.disciplinas.index(disciplinaRef)
        self.disciplinas[indice].addListas(hoje)
        print("Lista adicionada com sucesso")

    # def marcarProvaNaDisciplina(self, indiceRef: int, data: date):
    #     dc = self.getDisciplinaCurricularPeloIndice(indiceRef)
    #     indice = self.disciplinas.index(dc)
    #     if data.weekday() in self.disciplinas[indice].get_dias():
    #         self.disciplinas[indice].addProvas(data)
    #         print(f"Sucesso, prova marcada no dia: {mt.exibir_data(data)} às {self.disciplinas[indice].getHoraInicioHoje(data.weekday())}")
    #     else:
    #         print("Erro, prova marcada no dia sem a disciplina!")

    def marcarPresencaPeloId(self, id: int, presenca: bool):
        for i in range(len(self.disciplinas)):
            if self.disciplinas[i].id == id:
                self.disciplinas[i].marcarPresenca(presenca)

    def adicionarBibliografiaADisciplina(self, id: int, livro: Livro):
        for i in range (len(self.disciplinas)):
            if self.disciplinas[i].id == id:
                self.disciplinas[i].addBibliografia(livro)

    def __str__(self):
        return f"{self.nome} - {self.email} ({self.curso} | Aptidões: {self.aptidoesToString()})"

    def __eq__(self, other):
        return self.email == other.email
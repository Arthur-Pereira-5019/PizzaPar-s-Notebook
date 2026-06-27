from datetime import date, datetime, timedelta
from UsuarioService import *
from Disciplina import *
from Livros import *
from MochilaDeLivros import *
import ModuloTempo as mt
import ModuloMenuDisciplinas as moduloMenuDisciplinas
import ModuloMenuAcademicoGeral as moduloMenuAcademico

us = UsuarioService()
usuario_logado: Usuario = None
estado_disciplina = None
estado = "Menu"

def estado_hoje():
    global estado
    hoje = mt.data_de_hoje()
    print(mt.exibir_data_hoje())
    print("")

    livrosADevolver = usuario_logado.mochilaDeLivros.livrosADevolverHoje(hoje)
    if len(livrosADevolver) != 0:
        print("Livros à Devolver Hoje:")
        for i in range(len(livrosADevolver)):
            print(livrosADevolver[i].exibicao_simples())
        print("")
    else:
        print("Sem livros à devolver hoje. \n")
    provasHoje = usuario_logado.provasHoje(hoje)
    if len(provasHoje) != 0:
        print("Provas de hoje:")
        for i in range (len(provasHoje)):
            print(f"Prova de {provasHoje[i].get_nome()} às {provasHoje[i].getHoraInicioHoje(mt.dia_da_semana())}")
        print("")
    else:
        print("Sem nenhuma prova hoje!")

    disputasHoje = usuario_logado.disputasHoje(hoje)
    if len(disputasHoje) > 0:
        print("Você tem disputas hoje!")
        for i in range(len(disputasHoje)):
            print(f"{i+1}. {disputasHoje[i].get_nome()}")
        print("")
    else:
        print("Você não tem nenhuma disputa hoje!")

    aulasHoje = usuario_logado.disciplinasDeHoje(mt.dia_da_semana())
    if len(aulasHoje) > 0:
        print("Hoje você tem as seguintes aulas: ")
        for i in range(len(aulasHoje)):
            print(f"{i+1}. [{aulasHoje[i].stringAulas()}] {aulasHoje[i].get_nome()} às {aulasHoje[i].getHoraInicioHoje(mt.dia_da_semana())}")
        print("")
    else:
        print("Hoje você não tem nenhuma aula, aproveite o descanso para estudar mais!")

    print(f"Você tem {usuario_logado.getNListasAFazer()} listas à fazer.")
    estado = "Menu"

def estado_configurando_conta():
    global estado
    while True:
        print(f"Nome: {usuario_logado.nome}")
        print(f"Conta: {usuario_logado.publicidadeToString()}")
        print(f"Curso: {usuario_logado.getCurso()}")
        print(f"Aptidões: {usuario_logado.aptidoesToString()}")
        print("Você pode mudar as seguintes configurações da sua conta:\nAlterar as suas [Aptidoes]\nTrocar de [curso]\nTrocar de [Nome]\nTrocar [Privacidade] da conta\n[Excluir] sua conta\n[Sair]")
        op = input().lower()
        if op == "aptidoes":
            napts = [False]*4
            print("Para configurar as aptidões, responda com S para cada uma que você possui, qualquer outra entrada será interpretada como um Não.")
            aptLinguagens = input("Linguagens: ")
            aptMatematica = input("Matemática: ")
            aptHumanas = input("Ciências Humanas e Sociais: ")
            aptNaturezas = input("Ciências da Natureza: ")
            if aptLinguagens == "S":
                napts[0] = True
            if aptMatematica == "S":
                napts[1] = True
            if aptHumanas == "S":
                napts[2] = True
            if aptNaturezas == "S":
                napts[3] = True
            usuario_logado.setAptidoes(napts)
            print("Aptidões atualizadas com sucesso!")
        elif op == "curso":
            print("Prossiga com cautela, você pode perder dados relevantes das suas disciplinas:")
            print("Você deseja trocar de curso e: \nRemover todas disciplinas [curriculares]\nRemover [todas] disciplinas\n[Revisar] disciplinas manualmente posteriormente\n[Sair].")
            opd = ""
            while True:
                opd = input().lower()
                if opd == "curriculares":
                    usuario_logado.removerDisciplinasCurriculares()
                    break
                elif opd == "todas":
                    usuario_logado.removerTodasDisciplinas()
                    break
                elif opd == "revisar" or opd == "sair":
                    break
                else:
                    print("Comando não identificado, cheque a ortografia e tente novamente.")
            if opd != "sair":
                curso = input("Digite o nome do novo curso que você deseja entrar: ")
                usuario_logado.setCurso(curso)
                print("Curso alterado com sucesso!")
        elif op == "nome":
            novo_nome = input("Digite seu novo nome de usuário: ")
            usuario_logado.setNome(novo_nome)
            print("Nome alterado com sucesso!")
        elif op == "excluir":
            prosseguir = input("Você tem certeza que deseja fazer isso? Essa operação é irreversível! [S/N]")
            if prosseguir == "S":
                us.excluirConta(usuario_logado)
                print("Conta excluída com sucesso!")
                estado = "Fora"
                break
            else:
                continue
        elif op == "privacidade":
            usuario_logado.switchPublicidade()
            if usuario_logado.isPublica():
                print("Sua conta agora é pública!")
            else:
                print("Sua conta agora é privada!")
        elif op == "sair":
            estado = "Menu"
            break
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")

def estado_fim_do_dia():
    global estado
    print("Encerrando o dia...")
    disciplinas_hoje = usuario_logado.disciplinasDeHoje(mt.dia_da_semana())
    if len(disciplinas_hoje) == 0:
        estado = "Menu"
        mt.proximo()
        return
    print("O dia foi letivo? [S/N]")
    while True:
        dl = input()
        if dl == "S":
            print("Marque S para as disciplinas que você esteve presente, qualquer outra entrada será entendida como ausência.")
            for i in range(len(disciplinas_hoje)):
                p = input(f"{disciplinas_hoje[i].get_nome()}: ")
                if p == "S":
                    usuario_logado.marcarPresencaPeloId(disciplinas_hoje[i].id,True)
                else:
                    usuario_logado.marcarPresencaPeloId(disciplinas_hoje[i].id,False)
            break
        elif dl == "N":
            print("Marcando presença para todas disciplinas de hoje, bom descanso.")
            for i in range(len(disciplinas_hoje)):
                usuario_logado.marcarPresencaPeloId(disciplinas_hoje[i].id, True)
            break
        else:
            print("Comando não compreendido, cheque a ortografia e tente novamente.")
    mt.proximo()
    estado = "Menu"

def estado_configurando_mochila():
    global estado
    print("Preencha os campos abaixo para configurar sua mochila de livros. Preencha o número de renovações com -1 para retornar ao menu principal.")
    while True:
        n_renovacoes = int(input("Digite o número máximo de renovações da biblioteca que você consulta: "))
        if n_renovacoes == -1:
            estado = "Menu"
            break
        multa = float(input("Digite a multa por dia da sua biblioteca em R$: "))
        if multa < 0:
            print("Por favor, digite um valor de multa válido.")
            continue
        dias_emprestimo = int(input("Digite o número de dias que um empréstimo/renovação te permite ficar com exemplar em sua biblioteca: "))
        if dias_emprestimo < 0:
            print("Por favor, digite um número de dias válido.")
            continue
        usuario_logado.mochilaDeLivros.configurar(multa,n_renovacoes,dias_emprestimo)
        print("Agora sim, podemos olhar sua mochila!")
        estado = "Mochila"
        break

def estado_mochila():
    global estado
    hoje = mt.data_de_hoje()
    if usuario_logado.mochilaDeLivros.isConfigurada():
        usuario_logado.mochilaDeLivros.gerarResumo(hoje)
        estado = "Mochila Opcoes"
    else:
        print("Pelo que parece sua mochila de livros ainda não está configurada, vamos resolver isso!")
        estado = "Configurando Mochila"

def estado_adicionando_livro():
    global estado
    hoje = mt.data_de_hoje()
    while True:
        opa = input("Você deseja adicionar um livro com base na bibliografia de alguma disciplina? [S/N/C]")
        opa = opa.lower()
        if opa == "s":
            disciplinas = usuario_logado.getDisciplinasCurriculares()
            if len(usuario_logado.getDisciplinasCurriculares()) != 0:
                usuario_logado.exibirDisciplinasCurriculares()
                i = int(input("Digite o índice da disciplina que você deseja consultar bibliografia: "))
                if 0 < i <= len(disciplinas):
                    biblio = usuario_logado.mochilaDeLivros.cruzarBibliografia(disciplinas[i - 1])
                    if len(biblio) == 0:
                        print("A sua bibliografia para esta disciplina está completa.")
                    else:
                        print("Faltam estes livros em sua bibliografia: ")
                        for j in range(len(biblio)):
                            print(f"{j + 1}. {biblio[j].exibicao_simples()}")
                        k = (input(
                            "Digite o índice do livro que você deseja adicionar a sua mochila. Ou preencha com sair para retornar ao menu principal."))
                        if k.lower() == "sair":
                            estado = "Menu"
                            break
                        k = int(k)
                        if 0 < k <= len(biblio):
                            usuario_logado.mochilaDeLivros.adicionar(biblio[k - 1], hoje)
                            print(
                                f"{biblio[k - 1].exibicao_simples()} adicionado à mochila com sucesso. Sua data de devolução é: {mt.exibir_data(usuario_logado.mochilaDeLivros.calcularDevolucao(hoje))}")
                        else:
                            print("Índice fora do limite da bibliografia, verifique a ortografia do comando e tente novamente.")
                else:
                    print("Índice fora do limite do número de disciplinas, verifique a ortografia do comando e tente novamente.")
            else:
                print("Você não está em nenhuma disciplina curricular no momento.")
        elif opa == "n":
            estado = "Cadastrando Livros 2"
            break
        elif opa == "c":
            estado = "Menu"
            break
        else:
            print("Comando não compreendido, cheque a ortografia do comando.")

def estado_mochila_opcoes():
    global estado
    hoje = mt.data_de_hoje()
    taxa = usuario_logado.mochilaDeLivros.getMulta()
    print("\nPara exibir informações mais detalhadas. Você pode:\nConsultar [Atrasos]\nConsultar Bibliografia ["
          "Faltante]\nConsultar seus [Emprestimos]\n[Renovar] seus livros\n[Devolver] seus livros\n[Adicionar] um "
          "livro à mochila\n[Reconfigurar] sua mochila.\n[Sair] para voltar ao menu principal.")
    while True:
        op = input().lower()
        estado = "Menu"
        if op == "atrasos":
            usuario_logado.mochilaDeLivros.exibirAtrasos(hoje)
        elif op == "faltante":
            disciplinas = usuario_logado.getDisciplinas()
            faltantes = []
            print("Faltam os seguintes livros na sua mochila: ")
            for i in range(len(disciplinas)):
                faltantes.extend(usuario_logado.mochilaDeLivros.cruzarBibliografia(disciplinas[i]))
            for i in range(len(faltantes)):
                print(f"{i+1}. {faltantes[i].exibicao_simples()}")
        elif op == "emprestimos":
            usuario_logado.mochilaDeLivros.exibicao(hoje)
        elif op == "renovar":
            usuario_logado.mochilaDeLivros.exibicao(hoje)
            while True:
                i = int(input("Digite o índice do livro a ser renovado: "))
                i = int(i) - 1
                if 0 <= i < len(usuario_logado.mochilaDeLivros.getLivros()):
                    usuario_logado.mochilaDeLivros.renovar(i,hoje)
                    break
                else:
                    print("Digite um índice que esteja compreendido pela lista de livros emprestados.")
        elif op == "devolver":
            usuario_logado.mochilaDeLivros.exibicao(hoje)
            while True:
                i = (input("Digite o índice do livro a ser renovado. Preencha o índice com [tudo] para devolver todos "
                              "os livros simultaneamente: "))
                if i.lower() == "tudo":
                    usuario_logado.mochilaDeLivros.devolverTudo(hoje)
                    break
                i = int(i)-1
                if 0 <= i < len(usuario_logado.mochilaDeLivros.getLivros()):
                    usuario_logado.mochilaDeLivros.devolver(int(i),hoje)
                    break
                else:
                    print("Digite um índice que esteja compreendido pela lista de livros emprestados.")
        elif op == "adicionar":
            estado = "Adicionar Livro"
        elif op == "reconfigurar":
            estado = "Configurando Mochila"
        elif op == "sair":
            estado = "Menu"
        else:
            estado = "Mochila Opcoes"
            print("Comando não compreendido, verifique a ortografia dele. ")

        if estado != "Mochila Opcoes":
            break

def estado_cadastrando_livros(disciplina: DisciplinaCurricular):
    global estado
    global usuario_logado
    hoje = mt.data_de_hoje()
    print("Informe os campos abaixo para registrar o novo livro. Preencha o título com sair para encerrar o registro.")
    contador = 1
    while True:
        print(f"{contador}.")
        titulo = input("Digite o título do livro: ")
        if titulo.lower() == "sair":
            estado = "Menu"
            break
        autor = input("Autor do livro: ")
        if disciplina is None:
            l = Livro(titulo,autor)
            usuario_logado.mochilaDeLivros.adicionar(l,hoje)
        else:
            l = Livro(titulo,autor)
            usuario_logado.adicionarBibliografiaADisciplina(disciplina.id,l)
        contador += 1


def estado_registrando():
    global estado
    global usuario_logado
    print("Preencha os campos abaixo, preencha o nome com sair para retornar.")
    while True:
        nome = input("Digite o seu nome de usuário: ")
        if nome.lower() == "sair":
            estado = "Fora"
            break
        email = input("Digite o E-Mail da sua conta: ")
        if not us.verificar_email(email):
            continue
        senha = input("Digite a senha da sua conta: ")
        if not validarSenha(senha):
            continue
        curso = input("Digite o principal curso no qual você está estudando: ")
        r = us.registrar(nome,email,senha,curso)
        if not r is None:
            usuario_logado = r
            estado = "Menu"
            break

def estado_login():
    global estado
    global usuario_logado
    print("Preencha os campos abaixo, preencha o E-Mail com Sair para retornar.")
    while True:
        email = input("Digite o email da sua conta: ")
        if email.lower() == "sair":
            estado = "Menu"
            break
        senha = input("Digite a senha da sua conta: ")
        r = us.login(email,senha)
        if not r is None:
            usuario_logado = r
            estado = "Menu"
            break

def estado_fora():
    global estado
    global usuario_logado
    usuario_logado = None
    while True:
        opcao = input("Você deseja realizar [Login] ou se [Registrar]? ")
        if opcao.lower() == "login":
            estado = "Logando"
            break
        elif opcao.lower() == "registrar":
             estado = "Registrando"
             break
        else:
            print("Operação não identificada, tente novamente.")

def estado_menu():
    global estado
    while True:
        opcao = input("O que você deseja realizar?\nVer o resumo de [Hoje]\nConsultar [Mochila] de Livros\n[Sugerir] "
                      "Estudos\nBuscar [Parceiros] de Estudos\nConsultar [Situacao] das notas e frequência.\nEncerrar o "
                      "[Dia]\nConsultar seus registros para as disciplinas [esportivas]\nConsultar seus registros para as disciplinas [curriculares]\n[Configuracoes] da sua Conta\nEfetuar [Logout]\n")
        match opcao.lower():
            case "hoje":
                estado = "Hoje"
            case "mochila":
                estado = "Mochila"
            case "sugerir":
                estado = "Sugerindo Estudos"
            case "parceiros":
                estado = "Parceiros de Estudos"
            case "situacao":
                estado = "Situacao Academica"
            case "dia":
                estado = "Fim do Dia"
            case "configuracoes":
                estado = "Configurando Conta"
            case "curriculares":
                estado = "Consultando Curriculares"
            case "esportivas":
                estado = "Consultando Esportivas"
            case "logout":
                print("Saindo...\n")
                estado = "Fora"
            case _:
                print("Comando não compreendido, cheque a ortografia do comando e tente novamente.")
        if estado != "Menu":
            break


def state_resolver():
    global estado
    global usuario_logado
    global estado_disciplina
    disciplinasConcluidas = usuario_logado.getDisciplinasConcluidas()
    if len(disciplinasConcluidas) != 0:
        print(f"{len(disciplinasConcluidas)} se encerraram hoje! Removeremos elas automaticamente para você. Aqui estão os resultados... ")
        for i in range(len(disciplinasConcluidas)):
            print(disciplinasConcluidas[i].getMensagemAprovacao())
        print("")
    if estado == "Fora":
        estado_fora()
    elif estado == "Logando":
        estado_login()
    elif estado == "Registrando":
        estado_registrando()
    elif estado == "Menu":
        estado_menu()
    elif estado == "Configurando Mochila":
        estado_configurando_mochila()
    elif estado == "Mochila":
        estado_mochila()
    elif estado == "Mochila Opcoes":
        estado_mochila_opcoes()
    elif estado == "Cadastrando Livros 1":
        estado_cadastrando_livros(estado_disciplina)
    elif estado == "Cadastrando Livros 2":
        estado_cadastrando_livros(None)
    elif estado == "Parceiros de Estudos":
        print("Encontrando usuários que estudam no mesmo curso que você... ")
        us.buscaParceiros(usuario_logado)
        print("")
        estado = "Menu"
    elif estado == "Configurando Conta":
        estado_configurando_conta()
    elif estado == "Adicionando Disciplinas 1":
        estado, usuario_logado, estado_disciplina = moduloMenuDisciplinas.adicionar_disciplinas_curriculares(usuario_logado)
    elif estado == "Adicionando Disciplinas 2":
        estado, usuario_logado = moduloMenuDisciplinas.adicionar_disciplinas_esportivas(usuario_logado)
    elif estado == "Consultando Esportivas":
        estado, usuario_logado = moduloMenuDisciplinas.estado_consultando_esportivas(usuario_logado)
    elif estado == "Consultando Curriculares":
        estado, usuario_logado = moduloMenuDisciplinas.estado_consultando_curriculares(usuario_logado)
    elif estado == "Hoje":
        estado_hoje()
    elif estado == "Fim do Dia":
        estado_fim_do_dia()
    elif estado == "Situacao Academica":
        estado, usuario_logado = moduloMenuAcademico.estado_situacao_academica(estado, usuario_logado)
    elif estado == "Adicionar Livro":
        estado_adicionando_livro()
    elif estado == "Sugerindo Estudos":
        estado, usuario_logado = moduloMenuAcademico.estado_sugerindo_estudos(estado,usuario_logado)
    else:
        print("Sistema em estado ilegal, retornando ao Menu!")
        estado = "Menu"

# Para fins de teste DO NOT SHIP
us.registrar("Arthur","peneir20@gmail.com","abC..123","CC")
us.registrar("Arthur1","peneir21@gmail.com","abC..123","CC")
us.registrar("Arthur2","peneir22@gmail.com","abC..123","CC")
us.registrar("Arthur3","peneir23@gmail.com","abC..123","Agronomia")
us.registrar("Caio","cndelpizzo@gmail.com","abC..123","Agronomia")
us.usuarios[0].switchPublicidade()
us.usuarios[1].switchPublicidade()
us.usuarios[3].switchPublicidade()
us.usuarios[4].switchPublicidade()
us.usuarios[0].addDisciplinaCurricular("Português",[0,1,2],7,["10:00","09:00","08:00"],["12:00","14:00","10:00"],0)
us.usuarios[0].addDisciplinaCurricular("Matemática",[2,3,4],7,["08:00","09:00","14:00"],["10:00","14:00","16:00"],1)

us.usuarios[0].adicionarBibliografiaADisciplina(0,Livro("Dicionário","Aurélio"))
us.usuarios[0].adicionarBibliografiaADisciplina(0,Livro("Brás Cubas","Machado de Assis"))

us.usuarios[0].adicionarBibliografiaADisciplina(1,Livro("Elementos","Euclides"))
us.usuarios[0].adicionarBibliografiaADisciplina(1,Livro("Discrete Mathematics","Kolman"))

us.usuarios[0].mochilaDeLivros.configurar(1.50,2,2)
#us.usuarios[0].marcarProvaNaDisciplina(0,date(2026,6,25))
#us.usuarios[0].marcarProvaNaDisciplina(0,date(2026,6,29))
#us.usuarios[0].marcarProvaNaDisciplina(0,date(2026,6,30))
#us.usuarios[0].marcarProvaNaDisciplina(1,date(2026,6,24))
#us.usuarios[0].darNotaParaDisciplinaPeloIndice(0,0,7)
#us.usuarios[0].darNotaParaDisciplinaPeloIndice(0,1,8)
#us.usuarios[0].darNotaParaDisciplinaPeloIndice(0,2,4)
#us.usuarios[0].darNotaParaDisciplinaPeloIndice(1,0,5)
us.usuarios[0].disciplinas[0].addProvas(date(2026,7,1))
us.usuarios[0].disciplinas[1].addProvas(date(2026,7,1))

usuario_logado = us.usuarios[0]
estado = "Sugerindo Estudos"
while True:
    state_resolver()
    


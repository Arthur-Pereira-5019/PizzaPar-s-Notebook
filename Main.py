from datetime import date, datetime, timedelta
from UsuarioService import *
from Disciplina import *
from Livros import *
from MochilaDeLivros import *
import ModuloTempo as mt

us = UsuarioService()
usuario_logado: Usuario = None
estado_disciplina = None
estado = "Fora"

def estado_hoje():
    hoje = mt.data_de_hoje()
    print(mt.exibir_dia_da_semana())
    print("\n")

    livrosADevolver = usuario_logado.mochilaDeLivros.livrosADevolverHoje(hoje)
    if len(livrosADevolver) != 0:
        print("Livros à Devolver Hoje:")
        for i in range(len(livrosADevolver)):
            print(livrosADevolver[i].exibicao_simples())
        print("\n")
    else:
        print("Sem livros à devolver hoje. \n")
    disciplinas = usuario_logado.provasHoje(hoje)
    if len(disciplinas) != 0:
        print("Provas de hoje:")
        for i in range (disciplinas):
            print(f"Prova de {disciplinas[i].get_nome()} às {disciplinas[i].get_hora()}")

def estado_configurando_conta():
    global estado
    print("Você pode mudar as seguintes configurações da sua conta:\nAlterar as suas [Aptidões]\nTrocar de [curso]\nTrocar de [Nome]\nTrocar [Privacidade] da conta\n[Sair]")
    while True:
        op = input().lower()
        if op == "Aptidões":
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
        elif op == "curso":
            print("Prossiga com cautela, você pode perder dados relevantes das suas disciplinas:")
            print("Você deseja trocar de curso e: \nRemover todas disciplinas [curriculares]\nRemover [todas disciplinas]\n[Revisar] disciplinas manualmente posteriormente\n[Sair].")
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
                curso = input("Digite o nome do novo curso que você deseja entrar.")
                usuario_logado.setCurso(curso)
                print("Curso alterado com sucesso!")
        elif op == "nome":
            novo_nome = input("Digite seu novo nome de usuário: ")
            usuario_logado.setNome(novo_nome)
            print("Nome alterado com sucesso!")
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
            usuario_logado.exibirDisciplinasCurriculares()
            i = int(input("Digite o índice da disciplina que você deseja consultar bibliografia"))
            if i > 0 or i <= len(disciplinas):
                biblio = usuario_logado.mochilaDeLivros.cruzarBibliografia(disciplinas[i - 1])
                if len(biblio) == 0:
                    print("A sua bibliografia para esta disciplina está completa.")
                else:
                    print("Faltam estes livros em sua bibliografia: ")
                    for j in range(len(biblio)):
                        print(f"{i + 1}. {biblio[i].exibicaoSimples()}")
                    k = (input(
                        "Digite o índice do livro que você deseja adicionar a sua mochila. Ou preencha com sair para retornar ao menu principal."))
                    if k.lower() == "sair":
                        estado = "Menu"
                        break
                    k = int(k)
                    if k > 0 or k <= len(disciplinas):
                        usuario_logado.mochilaDeLivros.adicionar(biblio[k - 1], hoje)
                        print(
                            f"{biblio[k - 1].exibicaoSimples()} adicionado à mochila com sucesso. Sua data de devolução é: {usuario_logado.mochilaDeLivros.calcularDevolucao(hoje)}")
                    else:
                        print("Índice fora do limite da bibliografia, verifique a ortografia do comando e tente novamente.")
            else:
                print("Índice fora do limite do número de disciplinas, verifique a ortografia do comando e tente novamente.")
        elif opa == "n":
            estado = "Cadastrando Livros 2"
        elif opa == "c":
            estado = "Menu"
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
                faltantes.append(usuario_logado.mochilaDeLivros.cruzarBibliografia(disciplinas))
            for i in range(len(faltantes)):
                faltantes[i].exibicaoSimples(hoje)
        elif op == "emprestimos":
            usuario_logado.mochilaDeLivros.exibicao(hoje)
        elif op == "renovar":
            usuario_logado.mochilaDeLivros.exibicao(hoje)
            i = int(input("Digite o índice do livro a ser renovado: "))
            usuario_logado.mochilaDeLivros.renovar(i,hoje)
        elif op == "devolver":
            usuario_logado.mochilaDeLivros.exibicao(hoje)
            i = (input("Digite o índice do livro a ser renovado. Preencha o índice com [tudo] para devolver todos "
                          "os livros simultaneamente: "))
            if i.lower() == "tudo":
                usuario_logado.mochilaDeLivros.devolverTudo(hoje)
            usuario_logado.mochilaDeLivros.devolverTudo(int(i),hoje)
        elif op == "adicionar":
            estado = "Adicionar Livro"
        elif op == "reconfigurar":
            estado = "Configurando Mochila"
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
    while True:
        titulo = input("Digite o título do livro: ")
        if titulo.lower() == "sair":
            estado = "Menu"
            break
        autor = input("Autor do livro: ")
        edicao = int(input("Digite o número da edição do livro: "))
        if disciplina is None:
            l = Livro(titulo,autor,edicao)
            usuario_logado.mochilaDeLivros.adicionar(l,hoje)
        else:
            l = Livro(titulo,autor,edicao)
            disciplina.addBibliografia(l)


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
        opcao = input("O que você deseja realizar?\nVer o resumo de [Hoje]\nConsultar [Mochila] de Livros\n[Sugerir "
                      "Estudos]\nBuscar [Parceiros] de Estudos\n[Consultar Situação] das notas.\nEncerrar o "
                      "[Dia]\n[Adicionar] disciplinas\n[Configurações] da sua Conta\nEfetuar [Logout]\n")
        match opcao.lower():
            case "hoje":
                estado = "Hoje"
            case "mochila":
                estado = "Mochila"
            case "sugerir estudos":
                estado = "Sugerindo Estudos"
            case "parceiros":
                estado = "Parceiros de Estudos"
            case "consultar situação":
                estado = "Situacao Academica"
            case "dia":
                estado = "Fim do Dia"
            case "configurações":
                estado = "Configurando Conta"
            case "adicionar":
                estado = "Adicionando Disciplinas"
            case "logout":
                print("Saindo...\n")
                estado = "Fora"
            case _:
                print("Comando não compreendido, cheque a ortografia do comando e tente novamente.")
        if estado != "Menu":
            break


def state_resolver():
    global estado
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


def adicionar_disciplinas():
    print(type(usuario_logado))
    
us.registrar("Arthur","peneir20@gmail.com","abC..123","CC")
us.registrar("Arthur1","peneir21@gmail.com","abC..123","CC")
us.registrar("Arthur2","peneir22@gmail.com","abC..123","CC")
us.registrar("Arthur3","peneir23@gmail.com","abC..123","Agronomia")
us.registrar("Caio","cndelpizzo@gmail.com","abC..123","Agronomia")
us.usuarios[0].switchPublicidade()
us.usuarios[1].switchPublicidade()
us.usuarios[3].switchPublicidade()
us.usuarios[4].switchPublicidade()
while True:
    print(estado)
    state_resolver()
    


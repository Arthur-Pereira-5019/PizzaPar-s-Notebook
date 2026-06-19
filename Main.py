from datetime import date, datetime, timedelta
from UsuarioService import *
from Disciplina import *
from Livros import *
from MochilaDeLivros import *
from ModuloTempo import *

us = UsuarioService()
mt = ModuloTempo()
usuario_logado: Usuario = None
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

def estado_configurando_mochila():
    global estado
    print("Preencha os campos abaixo para configurar sua mochila de livros. Preencha o número de renovações com -1 para retornar ao menu principal.")
    while True:
        n_renovacoes = int(input("Digite o número máximo de renovações da biblioteca que você se consulta: "))
        if n_renovacoes == -1:
            estado = "Menu"
            break
        multa = float(input("Digite a multa por dia da sua biblioteca em R$: "))
        dias_emprestimo = int(input("Digite o número de dias que um empréstimo/renovação te permite ficar com exemplar em sua biblioteca: "))
        usuario_logado.mochilaDeLivros.configurar(multa,n_renovacoes,dias_emprestimo)

def estado_mochila():
    global estado
    hoje = mt.data_de_hoje()
    if usuario_logado.mochilaDeLivros.isConfigurada():
        return
    else:
        estado = "Configurando Mochila"




def estado_cadastrando_livros(disciplina: DisciplinaCurricular, emprestando: bool):
    global estado
    global usuario_logado
    hoje = mt.data_de_hoje()
    print("Informe os campos abaixo para registrar o novo livro. Preencha o nome com sair para encerrar o registro.")
    while True:
        titulo = input("Digite o título do livro: ")
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
        if not us.validarSenha(senha):
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
        opcao = input("O que você deseja realizar?\nVer o resumo de [Hoje]\n[Consultar Mochila] de Livros\n[Sugerir Estudos]\nBuscar [Parceiros de Estudos]\n[Consultar Situação] das notas de hoje.\n[Encerrar o dia]\n[adicionar disciplinas]\n[Configurações] da sua Conta\n")
        match opcao.lower():
            case "hoje":
                estado = "Hoje"
            case "consultar mochila":
                estado = "Mochila"
            case "sugerir estudos":
                estado = "Sugerindo Estudos"
            case "parceiros de estudos":
                estado = "Parceiros de Estudos"
            case "consultar situação":
                estado = "Situacao Academica"
            case "encerrar o dia":
                estado = "Fim do Dia"
            case "configurações":
                estado = "Configurando Conta"
            case "adicionar disciplinas":
                estado = "Adicionando Disciplinas"

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



            
            

def adicionar_disciplinas():
    print(type(usuario_logado))
    

while True:
    print(estado)
    state_resolver()
    


from UsuarioService import *

us = UsuarioService()
usuario_logado = None
estado = "Fora"

def estado_registrando():
    print("Preencha os campos abaixo, preencha o nome com Sair para retornar.")
    while True:
        nome = input("Digite o seu nome de usuário: ")
        if(nome.lower() == "Sair"):
            break
        email = input("Digite o E-Mail da sua conta: ")
        if(not us.verificar_email(email)):
            continue
        senha = input("Digite a senha da sua conta:" )
        if(not us.validarSenha(senha)):
            continue
        curso = input("Digite o principal curso no qual você está estudando:" )
        r = us.registrar(nome,email,senha,curso)
        if(not r == None):
            usuario_logado = r
            estado = "Menu"
            break

def estado_login():
    print("Preencha os campos abaixo, preencha o E-Mail com Sair para retornar.")
    while True:
        nome = input("Digite o nome da sua conta: ")
        if(email.lower() == "Sair"):
            break
        senha = input("Digite a senha da sua conta:" )
        r = us.login(email,senha)
        if(not r == None):
            usuario_logado = r
            estado = "Menu"
            break

def estado_fora():
    global estado
    while True:
        opcao = input("Você deseja realizar [Login] ou se [Registrar]? ")
        if(opcao.lower() == "login"):
            estado = "Logando"
            break
        elif(opcao.lower() == "registrar"):
             estado = "Registrando"
             break
        else:
            print("Operação não identificada, tente novamente.")

def state_resolver():
    global estado
    if estado == "Fora":
        estado_fora()
    elif estado == "Logando":
        estado_login()
    elif estado == "Registrando":
        estado_registrando()

while True:
    state_resolver()
    


from Usuario import *

class UsuarioService():
    usuarios = []
    
    def login(self, email: str, senha: str):
        encontrado = False
        for i in range (len(usuarios)):
            if(usuario[i].getEmail() == email):
                encontrado = True
                if(usuario[i].getSenha() == senha):
                    return usuario[i]
                else:
                    print("Senha incorreta, digite novamente.")
                    return None
        if(encontrado == False):
            print("Usuário não encontrado, verifique a ortografia do E-Mail.")
            return None
    
    def registrar(self, nome: str, email: str, senha: str, curso: str):
        nu = Usuario(nome,email,senha,curso)
        usuarios.append(nu)
        print("Usuário registrado com sucesso!")
        return nu
    
    def verificar_email(self, email: str):
        for i in range (usuarios):
            if usuarios[i].getEmail() == email:
                print("Usuário com este E-Mail já registrado, faça login ou cheque a ortografia do E-Mail")
                return False
        return True
    
    def validarSenha(self,senha):
        if(re.match("^.{8,}$",senha)):
            if(re.match("/\\d/",senha)):
                if(re.match("^(?=.*[A-Z]).+$",senha)):
                    return True
                else:
                    print("A senha precisa ter pelo menos um maiúsculo")
            else:
                print("A senha precisa possuir pelo menos um número")
        else:
            print("A senha precisa possuir pelo menos 8 caracteres.")
        return False
from Usuario import *


def validarSenha(senha):
    if re.match("^.{8,}$", senha):
        if re.match("^.*\d.*$", senha):
            if re.match("^(?=.*[a-z]).+$", senha):
                if re.match("^(?=.*[A-Z]).+$", senha):
                    return True
                else:
                    print("A senha precisa ter pelo menos um caractere maiúsculo")
            else:
                print("A senha precisa ter pelo menos um caractere minúsculo")
        else:
            print("A senha precisa possuir pelo menos um número")
    else:
        print("A senha precisa possuir pelo menos 8 caracteres.")
    return False


class UsuarioService():
    usuarios:list[Usuario] = []
    
    def login(self, email: str, senha: str):
        #global self.usuarios
        encontrado = False
        for i in range (len(self.usuarios)):
            if self.usuarios[i].getEmail() == email:
                encontrado = True
                if self.usuarios[i].getSenha() == senha:
                    return self.usuarios[i]
                else:
                    print("Senha incorreta, digite novamente.")
                    return None
        if encontrado == False:
            print("Usuário não encontrado, verifique a ortografia do E-Mail.")
            return None
    
    def registrar(self, nome: str, email: str, senha: str, curso: str):
        #global self.usuarios
        nu = Usuario(nome,email,senha,curso)
        self.usuarios.append(nu)
        print("Usuário registrado com sucesso!")
        return nu
    
    def verificar_email(self, email: str):
        #global self.usuarios
        #print(self.usuarios)
        for i in range(len(self.usuarios)):
            if self.usuarios[i].getEmail() == email:
                print("Usuário com este E-Mail já registrado, faça login ou cheque a ortografia do E-Mail")
                return False
        return True

    def buscaParceiros(self,usuario: Usuario):
        curso = usuario.getCurso()
        c = 1
        for i in range(len(self.usuarios)):
            su = self.usuarios[i]
            if su.isPublica() and su.getCurso() == curso and su != usuario:
                print(f"{c}. {su}")
                c += 1
        if c == 1:
            print("Nenhum usuário encontrado.")

    def excluirConta(self, usuario: Usuario):
        self.usuarios.remove(usuario)
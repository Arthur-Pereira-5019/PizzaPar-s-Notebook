import re
class Usuario():
    def __init__(self, nome: str, email: str, senha: str, curso: str, publica: bool):
        self.aptidoes = []
        self.nome = nome
        self.email = email
        self.senha = self.validarSenha(senha)
        self.curso = curso
        self.publica = publica
    
    def isPublica(self):
        return self.publica
    
    def switchPublicidade(self):
        self.publica = not publica
        
    def setAptidoes(self,linguagens,matematica,humanas,naturezas):
        novasAptidoes = []
        if(linguagens):
            novasAptidoes.append("Linguagens")
        if(matematica):
            novasAptidoes.append("Matemática")
        if(humanas):
            novasAptidoes.append("Humanas")
        if(naturezas):
            novasAptidoes.append("Naturezas")
        self.aptidoes = novasAptidoes
    
    def setSenha(self, senha):
        if(validarSenha(senha)):
            senha = str(senha)
        
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
    
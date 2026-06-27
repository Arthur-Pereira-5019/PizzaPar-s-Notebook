from datetime import date, datetime, timedelta

from UsuarioService import *
from Disciplina import *
from Livros import *
from MochilaDeLivros import *
import ModuloTempo as mt
import ModuloMenuDisciplinas as moduloMenuDisciplinas

def estado_situacao_academica(estado, usuario: Usuario):
    hoje = mt.data_de_hoje()
    disciplinas = usuario.getDisciplinasCurriculares()
    for i in range (len(disciplinas)):
        print(disciplinas[i].get_nome())
        print(f"Frequência parcial: {disciplinas[i].calcFrequenciaParcial():.2f}% | Frequência Total: {disciplinas[i].calcFrequenciaTotal():.2f}% | Nota Parcial: {disciplinas[i].getMediaIndefinida(hoje)}")
        print("")
    return "Menu", usuario

def estado_sugerindo_estudos(estado, usuario: Usuario):
    hoje = mt.data_de_hoje()
    n = 0
    print(f"Quantas disciplinas você pretende estudar hoje? (Seu valor será limitado à {len(usuario.getDisciplinasCurriculares())}): ")
    while True:
        n = int(input())
        if n < 1:
            print("Valor inválido, digite novamente.")
        else:
            break
    print("Com base no tempo até as próximas provas, sua média atual, suas aptidões e o número de listas até a próxima prova...")
    disciplinas = usuario.disciplinasSugeridas(n,hoje)
    for i in range(len(disciplinas)):
        d = disciplinas[i]
        print(f"{i+1}. {d.stringMotivacaoParaEstudar(hoje,usuario.aptidoes)}")
    return "Menu", usuario

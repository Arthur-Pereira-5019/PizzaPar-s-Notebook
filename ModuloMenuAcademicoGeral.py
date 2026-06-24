from datetime import date, datetime, timedelta

from Main import usuario_logado
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
        print(f"Frequência parcial: {disciplinas[i].calcFrequenciaParcial()} Frequência Total: {disciplinas[i].calcFrequenciaTotal()} Nota Parcial: {disciplinas[i].getMediaIndefinida(hoje)}")
        print("")
    return "Menu", usuario
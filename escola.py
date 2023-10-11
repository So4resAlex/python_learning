#!/usr/bin/env python3
"""Exibe relatóriode crianças por atividade.

Imprimir a lista de crinaças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"

#Dados
sala1 = ["Erick", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
#aula_musica = ["Erick", "Carlos", "Maria"]
#aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

#Listaralunos em cada atividade por sala 
aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)
print("Ingles sala 1", aula_ingles_sala1)
print("Ingles sala 2", aula_ingles_sala2)



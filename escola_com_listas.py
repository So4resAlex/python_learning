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
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês",aula_ingles),
    ("Musica",aula_musica),
    ("Danca",aula_danca)
]

#Listaralunos em cada atividade por sala 

for nome_atividade, atividade in atividades:
    print()
    print(f"Alunos da atividade de {nome_atividade}")
    print("-" * 35)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print(f"sala 1", atividade_sala1)
    print(f"sala 2", atividade_sala1)
    print("-" * 35)



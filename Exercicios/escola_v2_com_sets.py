#!/usr/bin/env python3
"""Exibe relatóriode crianças por atividade.

Imprimir a lista de crinaças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

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
    print(f"Alunos da atividade de {nome_atividade}\n")
    print("-" * 35)
    
    #Alunos da sala 1 que tem intersecção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    print()
    print("#" * 40)

#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
criancas = {
    "sala1": ["Erick", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"],
    "sala2": ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
    "Inglês": ["Erick", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erick", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Listar alunos em cada atividade por sala
for nome_atividade, alunos_atividade in atividades.items():
    print()
    print(f"Alunos da atividade de {nome_atividade}\n")
    print("-" * 35)
    
    alunos_sala1 = [aluno for aluno in criancas["sala1"] if aluno in alunos_atividade]
    alunos_sala2 = [aluno for aluno in criancas["sala2"] if aluno in alunos_atividade]

    print("Sala1", alunos_sala1)
    print("Sala2", alunos_sala2)
    print()
    print("#" * 40)



for teste in criancas.items():
    teste2 = teste in atividades.items()
    print (teste2)
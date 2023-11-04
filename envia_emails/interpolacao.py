#!/usr/bin/env python3
"""Utilizando o arquivo tmpl.txt gera um modelo de e-mail
para cada cada contato salvo no arquivo emails.txt, as
pace holders são preenchidas por interpolação de strings.

Execução: Chame o script passando logo após os arguemntos de nome
do arquivo contendo os contatos e logo após o template da mensagem
Ex: ./interpolacao.py emails.txt tmpl.txt

__version__ = "0.1.1"
__author__ = "Alex Soares"
__license__ = "Unlicense"
"""
import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de e-mails")
    sys.exit(1)

file_name = arguments[0]
template_name = arguments[1]
path = os.curdir



templatepath = os.path.join(path, template_name)

filepath = os.path.join(path, file_name)
clientes = []
for line in open(filepath):
    name, email = line.split(",")
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "name" : name,
            "produto" : "caneta",
            "texto" : "Escrever bem",
            "link" : "https://linkaqui",
            "quantidade" : 1,
            "preco" : 50.5,
            "email" : email,
        }
    )
print("_" * 50)
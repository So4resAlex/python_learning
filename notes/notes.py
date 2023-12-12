#!/usr/bin/env python3

"""Bloco de notas

./notes.py new "Minha nota"
tag: tech
text:
Anotação geral sobre tech

./notes.py read --tag=tech
"""
__version__ = "0.0.1"
__author__ = "Alex Soares"
__license__ = "Unlicense"

import os 
import sys

cmds = ["read", "new"]
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"Please must specify subcomand {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    
    
    
    
while True:

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower
        except IndexError:
            arg_tag = input("Qual é a TAG: ").strip().lower()
            
            
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError as e:
            print(str(e))
            print("[ERROR] Informe um titulo para sua nota")
            title = input("Qual é o titulo: ").strip().title()
            #sys.exit(1)
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),

        ]
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    cont = input(f"Quer continuar {arguments[0]} notas [S/N]").strip().lower()
    if cont != "y":
        break
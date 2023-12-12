#!/usr/bin/env python3
"""Calculadora prefix

Funcionamento:

[operações] [n1] [n2]


Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ ./prefixcalc.py sum 5 2
7

$ ./prefixcalc.py mul 10 5
50

Os resultados serão salvos em 'prefizcalc.log' 
"""

__version__ = "0.1.0"
__author__ = "Alex Soares"
__license__ = "Unlicense"

import sys 
import os
from datetime import datetime
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

#Nossa instancia
log = logging.Logger("Alex", log_level)
#Level
ch = logging.StreamHandler()
ch.setLevel(log_level)
#Formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#Destino
log.addHandler(ch)


while True:
    arguments = sys.argv[1:]

    if not arguments:
        operations = input("operacao: ")
        n1 = input("n1: ")
        n2 = input("n2: ")
        arguments = [operations, n1, n2]
    elif len(arguments) != 3:
        log.error("Numero de argumentos invalidos, exemplo de uso ex: `sum 5 5")
        sys.exit(1)

    operations, *nums = arguments

    valid_operations = ("sum","mul","sub", "div")
    if operations not in valid_operations:
        log.error("Operação invalida, as operações validas são %s", valid_operations)

    valid_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            log.error("Número %s é invalido", num)
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        valid_nums.append(num)

    try:
        n1, n2 = valid_nums

    except ValueError as e:
        log.error("%s", e)
        sys.exit(1)
        
    if operations == "sum":
        result = n1 + n2
    elif operations == "sub":
        result = n1 - n2
    elif operations == "mul":
        result = n1 * n2
    elif operations == "div":
        result = n1 / n2

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().strftime('%H:%M:%S')
    user = os.getenv('USER', 'sei la quem foi')

    try:
        with open(filepath, "a") as file_:
            file_.write(f"O usuário, {user}, usou a calculadora as {timestamp} e fez a operacao a seguir, {operations}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        log.error("%s", e)
        sys.exit(1)

    #print (f"O resultado é {result}")
    
    if input("Pressione enter para continuar ou s para para \n"):
        break
    
    #TODO VAlidar laço e documentar 
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
"""

__version__ = "0.1.0"
__author__ = "Alex Soares"
__license__ = "Unlicense"

import sys

arguments = sys.argv[1:]

if not arguments:
    operations = input("operacao: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operations, n1, n2]
elif len(arguments) != 3:
    print ("Numero de argumentos invalidos")
    print("ex: `sum 5 5")
    sys.exit(1)

operations, *nums = arguments

valid_operations = ("sum","mul","sub", "div")
if operations not in valid_operations:
    print("Operacao invalida")
    print(f"As operacoes validas sao {valid_operations}")

valid_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero {num} é invalido")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

n1, n2 = valid_nums

if operations == "sum":
    result = n1 + n2
elif operations == "sub":
    result = n1 - n2
elif operations == "mul":
    result = n1 * n2
elif operations == "div":
    result = n1 / n2

print (f"O resultado é {result}")


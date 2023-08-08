#!/usr/bin/env python3
"""Hello World multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução: 

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Alex"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")[:5]
msg = "hello World"

if current_language == "pt_BR":
    msg = "Olá mundo"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"

print (msg)


#LANG=en_ZA.UTF-8

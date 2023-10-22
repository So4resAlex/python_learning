#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a
mensagem correspondente

Como usar: 

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou 
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Alex Soares"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")[:5]

msg = {
    "en_US": "Hello, world!",
    "en_ZA": "Hello, world!",
    "pr_BR": "Olá, mundo",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Holla, Mundo!",
    "fr_FR": "Bonjuor, Monde!",
}

print(msg[current_language])


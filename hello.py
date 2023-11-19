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
import sys
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

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Chose a language")


current_language = current_language[:5]


msg = {
    "en_US": "Hello, world!",
    "ZA": "Hello, world!",
    "pr_BR": "Olá, mundo",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Holla, Mundo!",
    "fr_FR": "Bonjuor, Monde!",
}

try:
    message = msg[current_language]
    
except KeyError:
    print(f"Language is invalid, choose from: {list(msg.keys())}")    
    sys.exit(1)
    
print(message * int(arguments["count"]))


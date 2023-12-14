#!/usr/bin/env python3

import logging
import sys

log = logging.Logger("alerta") #Criando a instancia de log

#Criando o dicionario
info = { 
    "temperatura" : None,
    "umidade" : None
}

#Salvando as chaves do dicionario em outro objeto
keys = info.keys

#Interando sobre as chaves
for key in keys():
    #Adicionado tratamento de execção para valor invalido
    try:
        info[key] = float(input(f"Qual é a {key}?".strip()))
    except ValueError:
        log.error(f"O valo da {key.capitalize()} foi informado de maneira invalida")
        sys.exit(1)

#Exportando os valores
temp = info["temperatura"]
umidade = info["umidade"]

#Comparações
if temp > 45:
    print("Alerta, CALOR EXTREMO")
elif temp * 3 >= umidade:
    print("Alera, CALOR UMIDO")
elif temp >= 10 and temp <= 30:
    print("Tempo de boa")
elif temp >= 0 and temp <= 10:
    print("Frio bagarai")
elif temp < 0:
    print("Congelemo")

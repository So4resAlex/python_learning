#!/usr/bin/env python3
"""
Cadastro de produto
"""
__author__ = "Alex Soares"
__license__ = "Unlicense"
__version__ = "0.1.0"

import pprint

produto = {
"nome" : "Caneta",
"cores" : ["Azul", "Verde"],
"preco" : 3.23,
"dimensao" : {
"dimensao_altura" : 10.1,
"dimensao_largura" : 0.8,
},
"codigo" : 7855,
"codebar" : None,
}

cliente = {
    "nome" : "Alex"
}

compra = {
    "cliente" : cliente,
    "produto" : produto,
    "quantidade" : 3
}

total_compra = compra["quantidade"] * compra['produto']['preco']

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
      
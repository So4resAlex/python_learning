#!/usr/bin/env python3
"""
Cadastro de produto
"""
__author__ = "Alex Soares"
__license__ = "Unlicense"
__version__ = "0.1.0"

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
compra = ("Bruno", produto["nome"], 3)
total_compra = compra[2] * produto["preco"]

print(f"O cliente {compra[0]} comprou {compra[1]}"
      f"e pagou o total de {total_compra}")
      
#!/usr/bin/env python
"""Imprime a tabiada do 1 ao 10.

---Tabuada do 1---
    1 x 1
    2 x 2
    3 x 3
...
--------------
---Tabuada do 2---
    2 x 1
    4 x 2
...
--------------
"""
__version__ = "0.1.0"
__author__ = "Alex Soares"

numeros = list(range (1,11))
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print ("#" * 18)

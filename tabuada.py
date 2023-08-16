#!/usr/bin/env python
"""Imprime a tabiado do 1 ao 10

---Tabuada do 1---
    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
##################
Tabuada do 2
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
...
##################
"""

__


numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}\n"))
    print("#" * 18)

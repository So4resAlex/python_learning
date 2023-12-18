#!/usr/bin/env python3

import sys
import logging

quartos = {}

try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco.strip()),
            "disponivel": True
        }
except FileNotFoundError:
    logging.error("Arquivo não existe")
    sys.exit(1)

print("Reservas Hotel Debian")
print("-" * 40)
print("Lista de quartos disponiveis")
print("x" * 40)
for codigo, dados in quartos.items():
    nome = dados["nome"]
    preco = dados["preco"]
    disponivel = "🚫" if not dados['disponivel'] else "👍"
    print(f"{codigo} - {nome} - R$ {preco:.2f} - {disponivel}")
    
nome = input("Qual seu nome: ").strip()
try:
    num_quarto = int(input("Qual é o numero do quarto?").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"Quarto {num_quarto} esta ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Digite apenas numeros")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe")
    sys.exit(1)
try:
    dias = int(input("Quantos dias deseja reservar?"))
except ValueError:
    logging.error("Digite apenas numeros")
    sys.exit(1)
print(nome, num_quarto, dias)
    
    

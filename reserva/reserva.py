#!/usr/bin/env python3

import sys
import logging

ocupados = {}

try:
    for line in open("reservas.txt"):
        nome,num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)


quartos = {}

try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco.strip()),
            "disponivel": False if int(codigo) in ocupados else True 
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)

nome_cliente = input("Qual seu nome: ").strip()
if len(ocupados) == len(quartos):
    print(f"Sinto muito {nome_cliente} hotel lotado")
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

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]

total = preco_quarto * dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome_cliente}, {num_quarto},{dias}\n")

print(f"Olá {nome_cliente}, você esta reservando o quarto {nome_quarto} por {dias} e isso custara {total:.2f}")
    
    

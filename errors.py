#!/usr/bin/env python3

import sys
import os

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") #Race condiction
    names = open("names.txt").readlines()
else:
    print("Error: File names.txt not found")
    sys.exit(1)

# LBYL - Look Before You Leap - Olhe antes de pular

if len(names) >= 4:
    print(names[4])
else:
    print("Error: Missing name in the list")
    sys.exit(1)
    




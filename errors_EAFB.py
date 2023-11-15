#!/usr/bin/env python3
import os
import sys

#EAFB - Easy to AsK Forgiveness than permission
#É mais facil perdão doque perdão

try:
    names = open("names.txt").readlines()
except FileNotFoundError:
    print("[ERROR] File names.txt not found")
    sys.exit(1)
finally:
    print ("Passou pelo finaly")
try:
    print(names[2])
except:
    print("[ERROR] Missing name in the list")
    sys.exit(1)
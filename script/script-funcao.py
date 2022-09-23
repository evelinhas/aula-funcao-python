#!/usr/bin/env python3

"""função exibir nome 
"""
__version__ = "0.0.1"
__author__ = "Evelin Haslinger"
__license__ = "GNU v3"

from unicodedata import name
from xml.sax.handler import property_interning_dict


def exibir_nome(input_name):
    print("O nome escolhido foi:") 
    print(input_name)



print("Escreva um nome:")
name=input()
exibir_nome(name)
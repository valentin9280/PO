#!/usr/bin/python

"""hello.py:simple hello world"""
import sys

from random import randrange 
 
nombrePropose = 0
 

print("\t\t\t\t PLUS OU MOINS \n\n")
 
nombreMystere = randrange(1, 30)
 
while nombrePropose != nombreMystere:
     
    print("Quel est le nombre ?")
    nombrePropose = input()
    nombrePropose = int(nombrePropose)
 
    if nombrePropose < nombreMystere:
        print("C'est trop petit !\n")
 

    elif nombrePropose > nombreMystere:
        print("C'est trop grand !\n")
 
    else:
        print("Felicitations\n")



"""
INF 8212 - Introduction aux systèmes informatiques
Travaille Pratique #01
Nom du programme: Conversion entre bases
Description: Ce programme permet de faire des conversions entre les bases 2, 10 et 16.
Auteure: Nathalia Cruz (CRUN13318501)
Date: Octobre 2023
Version du programme: 1.0
"""

import sys

#Variables et saisies
base_source = input("Saisir la base source (2, 10 or 16): ")
base_destination = input("Saisir la base destination: (2,10 or 16): ")
nombre_a_convertir = input("Saisir le nombre a convertir: ")


#Validation des saisies
saisie_valide = True

##Validation si la base source existe
if base_source != "2" and base_source != "10" and base_source != "16":
    print ("La base source n'est pas valide.")
    saisie_valide = False

##Validation si la base de destination existe
if base_destination != "2" and base_destination != "10" and base_destination != "16":
    print ("La base destination n'est pas valide.")
    saisie_valide = False   

##Validation si la base source est différente de la base de destination
if base_source == base_destination:
   print ("La base source est égal a la base destination.")
   saisie_valide = False                   

##Validation si le nombre à convertir est bien exprimé dans la base source
if base_source == "2":
    for i in nombre_a_convertir:
     if i != "0" and i != "1":
        print ("Nombre a convertir n'est pas valide")
        saisie_valide = False

if base_source == "10":
    for i in nombre_a_convertir:
     if i != "0" and i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9":
        print ("Nombre a convertir n'est pas valide")
        saisie_valide = False

if base_source == "16":
    for i in nombre_a_convertir:
     if i != "0" and i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "A" and i != "B" and i != "C" and i != "D" and i != "E" and i != "F":
        print ("Nombre a convertir n'est pas valide")
        saisie_valide = False

##Arreter le programe si la saisie n'est pas valide
if saisie_valide == False:
    sys.exit ()


#Traitement: conversion de bases
nombre_resultat = ""

##Convertir la base source 16 ou 2 en base destination 10
if base_destination == "10":
    dict = {"0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7","8":"8", "9":"9", 
            "A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15"} 
    
    somme = 0
    i = 0
    while i<len(nombre_a_convertir):

        nombre = nombre_a_convertir[i]
        nombre = dict[nombre]
        nombre = int(nombre)
        base = int(base_source)
        puissance = len(nombre_a_convertir) -1 -i

        somme = somme + (nombre * (base**puissance))
        i=i+1

    nombre_resultat = somme


##Convertir la base source 10 en base destination 16 ou 2
if base_source == "10":

    convertie = ""
    quociente = 1
    numerateur = int(nombre_a_convertir)
    diviseur = int(base_destination)
    dict = {"0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7","8":"8", "9":"9", 
            "10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"} 

    while quociente >=1:
        quociente = numerateur // diviseur
        reste = numerateur % diviseur
        
        numerateur = quociente

        reste_chaine = str(reste)
        convertie = dict[reste_chaine] + convertie 

    nombre_resultat = convertie


##Convertir la base source 16 en base destination 2
if base_source == "16" and base_destination == "2":
    dict = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", 
          "A":"1010", "B":"1011", "C": "1100", "D": "1101", "E": "1110", "F":"1111"} 
    
    convertie = ""
    for i in nombre_a_convertir:
        convertie = convertie + dict[i] 
    
    nombre_resultat = convertie

##Convertir la base source 2 en base destination 16
if base_source == "2" and base_destination == "16":   
    dict = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", 
            "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"} 

    numerateur = len(nombre_a_convertir)
    reste = numerateur % 4

    if reste == 3:
        nombre_a_convertir = "0" + nombre_a_convertir
    if reste == 2:
        nombre_a_convertir = "00" + nombre_a_convertir
    if reste == 1:
        nombre_a_convertir = "000" + nombre_a_convertir
   
    i=0
    convertie = ""
    while (i<len(nombre_a_convertir)-3):
        groupe = nombre_a_convertir[i:i+4]
        convertie = convertie + dict[groupe]
        i = i+4

    nombre_resultat = convertie


print (nombre_a_convertir,"en base", base_source,"donne", nombre_resultat, "en base", base_destination)

#Fin du script   
print("Fin normale du script")





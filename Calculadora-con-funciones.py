# Calculadora-con-funciones
Ejercicio calculadora con funciones de python 
def menu():
    print ("Menu\n---------")
    print ("0.- Sortir")
    print ("1.- Suma")
    print ("2.- Resta")
    print ("3.- Multiplicació")
    print ("4.- Divisió")
    print ("----------")
    valor = int(input("Introdueix una opció: "))
    return valor

def demana():
    num1 = int (input("Introdueix el núm. 1: "))
    num2 = int (input("Introdueix el núm. 2: "))
    return num1,num2

def suma(num1, num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplica(num1,num2):
    return num1*num2

def divideix(num1,num2):
    return num1/num2
    
valor = 10
while valor != 0:
    valor = menu()
    if valor <=4 and valor >=1:
        num1,num2 = demana()
    if valor == 1:
        resultat = suma(num1,num2)
    elif valor == 2:
        resultat = resta(num1,num2)
    elif valor == 3:
        resultat = multiplica (num1,num2)
    elif valor == 4:
        resultat = divideix (num1,num2)
    print ("El resultat de l'operació és", resultat)

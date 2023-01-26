# Exo 3
from random import random as rand
from math import sqrt
from exo2 import exponentielle
import matplotlib.pyplot as plt


# 1
def Sn1(n):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn
    """
    sum=0
    for i in range(1,n):
        sum+=rand()

    return sum

def estimateur_moyenne1(n):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn/n
    """
    return Sn1(n)/n

def graph1():
    """
    """
    ordonne = []
    
    for i in range(1,10000):
        ordonne.append(estimateur_moyenne1(i))

    plt.plot(ordonne)
    plt.show()



# 2
def Sn2(n,l):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn
    """
    sum=0
    for i in range(1,n):
        sum+=exponentielle(l)

    return sum

def estimateur_moyenne2(n,l):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn/n
    """
    return Sn2(n,l)/n

def graph2(l):
    ordonne = []
    
    for i in range(1,10000):
        ordonne.append(estimateur_moyenne2(i,l))

    plt.plot(ordonne)
    plt.show()

# 3
def simulateur3():
    """
    
    """
    u=rand()
    return sqrt(u)

def Sn3(n):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn
    """
    sum=0
    for i in range(1,n):
        sum+=simulateur3()

    return sum

def estimateur_moyenne3(n):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn/n
    """
    return Sn3(n)/n

def graph3():
    ordonne = []
    
    for i in range(1,10000):
        ordonne.append(estimateur_moyenne3(i))

    plt.plot(ordonne)
    plt.show()


if __name__ == "__main__":
    graph1()
    graph2(0.5)
    graph3()
# Exo 3
from random import random as rand
from exo2 import exponentielle


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


if __name__ == "__main__":
    for i in range(1,100):
        print(estimateur_moyenne2(i,0.5))

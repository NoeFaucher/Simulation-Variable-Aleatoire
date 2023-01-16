# Exo 3
from random import random as rand

def Sn(n,f):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn
    """
    sum=0
    for i in range(1,n):
        sum+=f()


def estimateur_moyenne(n,f):
    """
    Précondition : n>=1 entier, f fontion de simulation de la variable aléatoire
    Calcule Sn/n
    """
    return Sn(n,f)/n




if __name__ == "__main__":
    pass
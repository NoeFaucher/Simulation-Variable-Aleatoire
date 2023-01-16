# Exo 1
from random import random as rand 
from math import floor

# 1
def bernoulli(p):
    """
        Préconditon: p réel entre 0 et 1
        Simule une variable aléatoire suivant une loi de Bernoulli
    """
    u = rand()
    if u>p:
        return 0
    else:
        return 1


# 2
def binomiale(n,p):
    """  
        Précondition: p réel entre 0 et 1, n>0 entier 
        Simule une variable aléatoire suivant une loi Binomiale
    """
    res=0
    for i in range(1,n):
        res+=bernoulli(p)

    return res

# 3
def geometrique(p):
    """
        Préconditon: p réel entre 0 et 1
        Simule une variable aléatoire suivant une loi Géométrique
    """
    res=1
    while bernoulli(p)!=1 :
        res+=1

    return res



# 4
def uniforme1(k):
    """
        Précondition: k entier k>=2
        Simule une variable aléatoire suivant une loi Uniforme sur [1,k]
    """
    return floor(1+(k-1)*rand()+0.5)


# 5
def uniforme2():
    """
        Simule une variable aléatoire suivant une loi Uniforme sur [-1,1]
    """
    return 2*rand()-1



if __name__ == "__main__" :
    
    pass

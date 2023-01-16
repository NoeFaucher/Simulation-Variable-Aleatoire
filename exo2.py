# Exo 2
from random import random as rand
from math import log as ln, exp, factorial

# 1
def bernoulli(p):
    """
        Préconditon: p réel entre 0 et 1
        Simule une variable aléatoire suivant une loi de Bernoulli
    """
    u=rand()
    if (1-p > u):
        return 0
    else:
        return 1 

# 2
def geometrique(p):
    """
        Préconditon: p réel entre 0 et 1
        Simule une variable aléatoire suivant une loi Géométrique
    """
    u = rand()
    F=0
    x=0
    while(u>F):
        x+=1
        F=1-(1-p)**x

    return x


# 3
def poisson(l):
    """
        Préconditon: l réel
        Simule une variable aléatoire suivant une loi de Poisson
    """
    u = rand()
    F=exp(-l)
    x=0
    while(u>F):
        x+=1
        F+=(exp(-l)*(l**x))/factorial(x)

    return x



# 4
def exponentielle(l):
    """
        Préconditon: l réel
        Simule une variable aléatoire suivant une loi exponentielle
    """
    u=rand()
    return -ln(1-u)/l


if __name__ == "__main__":
    print(exponentielle(100))
    pass
# Exo 2
from random import random as rand
from math import log as ln

# 1
def bernoulli(p):
    """
        Préconditon: p réel entre 0 et 1
        Simule une variable aléatoire suivant une loi de Bernoulli
    """
    u=rand()
    if (1-p > u):
        return 0
    else :
        return 1   

# 2
def geometrique(p):
    """
        Préconditon: p réel entre 0 et 1
        Simule une variable aléatoire suivant une loi Géométrique
    """
    u = rand()
    return (ln(1-u)/ln(p))


# 3
def poisson(l):
    """
        Préconditon: l réel
        Simule une variable aléatoire suivant une loi de Poisson
    """

# 4
def exponentielle(l):
    """
        Préconditon: l réel
        Simule une variable aléatoire suivant une loi exponentielle
    """


if __name__ == "__main__":
    pass
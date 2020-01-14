def SolveurDichotomie(f,k,a,b,e):
    debut = a
    fin = b
    #calcul de la longueur de [a,b]
    ecart = b-a
    while ecart>e:
        #calcul du milieu
        m = (debut+fin)/2
        if f(m)>k:
            #la solution est inférieure à m
            fin = m
        else:
            #la solution est supérieure à m
            debut = m
        ecart = fin-debut
    return m

def SolveurBalayage(f,k,a,e):
    s = a
    while f(s) <= k  :
        s=s+e
    return s
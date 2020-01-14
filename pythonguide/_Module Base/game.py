from random import random

print (" Welcome to G1, le nombre mystère, V 1.0")
bestscore = 100
while True :
    score = 0
    mystValue = 1+ int( random() * 100)
    
    while True :
        Value = input ("Veuillez entrer une valeur entre 1 et 100 : ")
        inValue = int(Value)
        score = score + 1
        if inValue == mystValue :
            break
        elif inValue > mystValue :
            print( "La valeur mystère est plus basse..." )
        elif inValue < mystValue :
            print( "La valeur mystère est plus haute..." )
        else :
            print ( " Wait what ???? ")

    print ( "Bravo ! vous avez obtenue  le score de " + str(score) )
    if score <= bestscore and score != 0:
        bestscore = score
        print ( "NEW BEST SCORE !" )
    else:
        print ( "BESTSCORE : " + str(bestscore) )

    ingame = input ( "Voulez vous rejouer ? Y/N  ")
    if ingame != str("Y"):
        break
    else :
        print( "Ok let's go")



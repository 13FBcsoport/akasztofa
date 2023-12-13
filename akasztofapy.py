from random import choice

def beolvas(fajlnev) -> list:
    szavak_listaja=[]
    fajl = open('szavak.txt', "r", encoding="utf-8")
    for szo in fajl:
        szavak_listaja.append(szo.strip("\n"))
    
    fajl.close()
    return szavak_listaja

def sorsolo(lista):
    szo=choice(lista)
    return szo

def betu_hely_kiiro(szo, talalgatasok):
    visszaad = ""
    for betu in szo:
        if betu.lower() in [t.lower() for t in talalgatasok]:
            print(betu, end=" ")
            visszaad += betu
        else:
            print("_", end=" ")
            visszaad += "_"
    return visszaad
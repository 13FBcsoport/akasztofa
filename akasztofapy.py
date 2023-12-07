from random import choice

def beolvas(fajlnev)->list:
    szavak_listaja=[]
    fajl=open(fajlnev,"r" , encoding=("utf-8"))
    for szo in fajl:
        szavak_listaja.append(szo.strip("\n"))
    
    fajl.close()
    return szavak_listaja

def sorsolo(lista):
    szo = choice(lista)
    return szo

def betuhely_kiiro(szo, kar):
    visszaad = ''
    for betu in szo:
        if betu.lower() == kar.lower():
            print(betu, end=" ")
            visszaad += betu
        else:
            print("_", end=" ")
            visszaad += '_'
    return visszaad
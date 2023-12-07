from random import choice
def beolvas(fajlnev)->list:
    szavak_listaja=[]
    fajl=open(fajlnev,"r" , encoding=("utf-8"))
    for szo in fajl:
        szavak_listaja.append(szo.strip)
        print(szo.strip("\n"))
    
    fajl.close()
    return szavak_listaja

def randomszo(szavak: list):
    szo = choice(szavak)
    return szo

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

def Akasztofa():
    szavak = beolvas("szavak.txt")

    random_szo = sorsolo(szavak)
    print("A kiválasztott szó:", "_" * len(random_szo))

    min_probalkozasok = len(random_szo) + 3
    tippek = min_probalkozasok
    talalgatasok = []
    rossz_tippek = set()
    
    while tippek > 0:
        betu = input("Kérek egy betűt: ")

        if betu.lower() in random_szo.lower():
            tippek -= 1
        else:
            tippek -= 1
            print("Rossz tipp! Próbálkozások száma:", tippek)
            rossz_tippek.add(betu)
            print("Eddigi rossz tippek:", ", ".join(rossz_tippek))
            continue

        talalgatasok.append(betu)
        vissza = betu_hely_kiiro(random_szo, talalgatasok)
        
        print("Eddigi találgatások:", ", ".join(talalgatasok))
        print("Eddigi találgatások eredménye:", vissza)

        if "_" not in vissza:
            print("Gratulálok, megfejtetted a szót!")
            return
    
    print("Sajnálom, vesztettél. A helyes szó:", random_szo)
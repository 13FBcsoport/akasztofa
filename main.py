from akasztofapy import *

def jatek():
    szavak = beolvas("szavak.txt")

    random_szo = sorsolo(szavak)
    print("A kiválasztott szó:", "_" * len(random_szo))

    min_probalkozasok = len(random_szo) + 3
    probalkozasok = min_probalkozasok
    talalgatasok = []
    rossz_tippek = set()
    
    while probalkozasok > 0:
        betu = input("Kérek egy betűt: ")

        if betu.lower() in random_szo.lower():
            probalkozasok -= 1
        else:
            probalkozasok -= 1
            print("Rossz tipp! Próbálkozások száma:", probalkozasok)
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

jatek()
from akasztofapy import *
szavak = []
szavak = beolvas("szavak.txt")

random_szo = sorsolo(szavak)
print(random_szo)

kar = input("Kérem a betűt: ")

szavak = []
szavak = beolvas("szavak.txt")

random_szo = sorsolo(szavak)
print(random_szo)

betu = input("Kérek egy betűt: ")

vissza = betu_hely_kiiro(random_szo,betu)
print(vissza)
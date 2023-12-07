from akasztofapy import *
szavak = []
szavak=beolvas("szavak.txt")

random_szo = sorsolo(szavak)
print(random_szo)

kar = input("Kérem a betűt: ")

vissza = betuhely_kiiro(random_szo, kar)
print(vissza)
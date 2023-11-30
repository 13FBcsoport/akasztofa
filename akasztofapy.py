print('akasztofa')
uzenet=input("Kérek egy betut")


def beolvas(fajlnev:str)->list:
    fajl=open(fajlnev,"r" , encoding=("utf-8"))
    for f in fajl:
        f.split(",")
    fajl.close()
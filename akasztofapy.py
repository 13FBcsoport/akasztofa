
def beolvas(fajlnev:str)->list:
    fajl=open(fajlnev,"r" , encoding=("utf-8"))
    for f in fajl:
        szavak=f.strip(",")
    fajl.close()
    return szavak
'''
Created on Dec 27, 2017

@author: lazar
'''
zaposleni=[]
def ucitajZaposlenog(line):
    ime,prezime,username,password,pozicija=line.split("/")
    zaposleni={"ime":ime,"prezime":prezime,"username":username,"password":password,"pozicija":pozicija}
    
    return zaposleni
def prijava(zaposleni):
    while True:
        username=input("Korisnicko ime>>>>")
        password=input("Password>>>>")
        user=login(username,password,zaposleni)
        if user!=None:
            return user
def login(username, password,zaposleni):
    for z in zaposleni:
        if z["username"].lower()==username.lower() and z["password"].lower()==password.lower():
            return z
    return None
def ucitajZaposlenogIzFajla():
    zaposleni=[]
    for i in open("Zaposleni.txt","r"):
        zap=ucitajZaposlenog(i[:-1])
        zaposleni.append(zap)
    return zaposleni
    
def ZaposleniToString(z):
    return "/".join((z["ime"], z["prezime"],z["username"],z["password"],z["pozicija"]))

def dodajZaposlenog(z):
    zaposleni.append(z)
    
def snimiZaposlenog():
    file=open("Zaposleni.txt","w")
    for z in zaposleni:
        file.write(ZaposleniToString(z))
        file.write("\n")
        
def otpustiZaposlenog(username,pozicija):
    index=pronadjiIndexZaposlenog(username,pozicija)
    if index!=None:
        zaposleni.pop(index);   
    else:
        print("Ne postoji takav zaposleni")
    
def pronadjiIndexZaposlenog(username,pozicija):
    for i, z in enumerate(zaposleni):
        if z["username"]==username and z["pozicija"]==pozicija:
                return i
    
    return None 

def stampajSve():
    print("Zaposleni: ")
    with open('zaposleni.txt', 'r') as f:
            for i, line in enumerate(f):
                print('{}. {}'.format(i+1, line.strip()))

ucitajZaposlenogIzFajla()
        
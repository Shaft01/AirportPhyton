'''
Created on Jan 11, 2018

@author: lazar
'''
from projekat import Zaposleni,letovi

def meniZaSefa():
    print("Meni za sefove")
    print("1. Podmeni u vezi letova")
    print("2. Podmeni u vezi zaposlenih")
    print("3. Jos malo letova")
    print("4. Odjava")
    print("x. Izlaz" )

def meniZaRadnika():
    print("Meni za radnike")
    print("1. Podmeni u vezi letova")
    print("2. Jos malo letova")
    print("3.Odjava")
    print("x. Izlaz")
    
def main():
    komanda=""
    while komanda!="x":
        zaposlen=Zaposleni.ucitajZaposlenogIzFajla()
        prijavljeni=Zaposleni.prijava(zaposlen)
        print(prijavljeni["ime"]+" "+prijavljeni["prezime"]+" se uspesno prijavio na sistem")
        if prijavljeni["pozicija"]=="radnik":
            while True:            
                meniZaRadnika()
                komanda=input(">>>")
                if komanda=='1':
                    while komanda!="x":
                        print("1) Ispisi sve letove")
                        print("2) Pretraga letova")
                        print("3) Zamena informacija o letu")
                        print("4) Dodaj novi let")
                        print("5) Obrisi let")
                        print ("x) Nazad ")
                        komanda = input(">>>")
                        if komanda =='1':
                            istampajLetove()
                        elif komanda =='2':
                            komanda=""
                            while komanda!="x":
                                print ("1) Pretraga po sifri")
                                print ("2) Pretraga po kljucu")
                                print ("x) Nazad ")
                                komanda=input(">>>")
                                if komanda=='1':
                                    pronadjiLet()
                                    break
                                if komanda=='2':
                                    pronadjiLetAlt()
                                    break
                                if komanda=='x':
                                    break
                        elif komanda =='3': 
                            izmeniLet()
                        elif komanda =='4':
                            letovi.dodaj() 
                        elif komanda =='5':
                            obrisiLet()       
                elif komanda=='2':
                    while komanda!="x":
                        print("1) Rezervisi let, kupi kartu")
                        print("2) Izracunaj vreme leta")
                        print ("x) Nazad ")
                        komanda = input(">>>")
                        if komanda == '1':
                            racun()
                        elif komanda =='2':
                            izracunajVremeLeta()

                elif komanda=='3':
                    break;
                elif komanda=='x':
                    print ("Dovidjenja")
                    break
        elif prijavljeni['pozicija']=='sef':
            while True:            
                meniZaSefa()
                komanda=input(">>>")
                if komanda=='1':
                    while komanda!="x":
                        print("1) Istampaj sve letove")
                        print("2) Pretraga letova")
                        print("3) Zamena informacija o letu")
                        print("4) Dodaj novi let")
                        print("5) Obrisi let")
                        print ("x) Nazad ")
                        komanda = input(">>>")
                        if komanda =='1':
                            istampajLetove()
                        elif komanda =='2':
                            komanda=""
                            while komanda!="x":
                                print ("1) Pretraga po sifri")
                                print ("2) Pretraga po kljucu")
                                print ("x) Nazad ")
                                komanda=input(">>>")
                                if komanda=='1':
                                    pronadjiLet()
                                    break
                                if komanda=='2':
                                    pronadjiLetAlt()
                                    break
                                if komanda=='x':
                                    break
                        elif komanda =='3': 
                            izmeniLet()
                        elif komanda =='4':
                            letovi.dodaj()
                        elif komanda =='5':
                            obrisiLet()
                elif komanda=='2':
                    while komanda!="x":
                        print("1) Istampaj sve zaposlene")
                        print("2) Dodaj novog zaposlenog")
                        print("3) Daj otkaz zaposlenom")
                        print ("x) Nazad ")
                        komanda = input(">>>")
                        if komanda == '1':
                            Zaposleni.stampajSve()
                        elif komanda =='2':
                            zaposliRadnika()
                        elif komanda == '3':
                            otkaz()        
                elif komanda=='3':
                    while komanda!="x":
                        print("1) Rezervisi let, kupi kartu")
                        print("2) Izracunaj vreme leta")
                        print ("x) Nazad ")
                        komanda = input(">>>")
                        if komanda == '1':
                            racun()
                        elif komanda =='2':
                            izracunajVremeLeta()                        
                elif komanda=='4':
                    break;
                elif komanda=='x':
                    print ("Hvala lepo, dovidjenja")
                    break
        else:
            print ("nije prepoznata uloga") 
          
def istampajLetove():
    print("Ispisi sve letove")
    kljuc=input("Unesite po cemu zelite da sortirate sifraLeta|model|grad|vreme1(Polazak)|vreme2(Dolazak) ")
    l=letovi.sortiraj(kljuc,0)
    print(letovi.formatHeader())
    for i in range(len(l)):
        print(letovi.formatLet(l[i])) 
        
def pronadjiLet():          
    print(" Pretraga leta po sifri")
    sifra = input("Unesite sifru leta: ")
    s = letovi.nadjiLet(sifra)
    if s != None:
        print(letovi.formatHeader())
        print(letovi.formatLet(s))
    else:
        print("Ne postoji let sa tom sifrom: ", sifra) 
        
def pronadjiLetAlt():
    print("Pretraga leta po kljucu")
    pom=input("Unesite po kom kljucu zelite da nadjete let(sifraLeta|model|grad|)")
    pom2=input("Unesite koju vrednost trazite")
    s=letovi.nadjiLetPoKljucu(pom,pom2)
    if len(s)!=0:
        print(letovi.formatHeader())
        for i in range(len(s)):
            print(letovi.formatLet(s[i]))
    else:
        print("Ne postoji let sa tim kriterijumima: ")    
        
def izmeniLet():
    print(" izmena informacija o letu ")
    sifra = input("Unesite sifru leta: ")
    kljuc = input("Unesite kljuc (vreme1|vreme2|grad,)")
    vrednost = input("Unesite novu vrednost(vremena su u formatu hh:mm): ")
    letovi.izmeniLet(sifra, kljuc, vrednost)
    letovi.snimiLetove()
def obrisiLet():
    istampajLetove()
    sifra=input("Unesite sifru leta kojeg zelite da uklonite")
    letovi.obrisiLet(sifra) 
    
def racun():
    sifra=input("Unesite sifru leta za koji hocete da uzemete kartu")
    klasa=input("Unesite za koju klasu hocete (biznis|ekonomska)")
    karte=input("Uneiste koliko karata zelite da uzmete(najvise 5)")
    if int(karte)<=5:
        letovi.racun(sifra,klasa,karte)          
    else:
        print("Ne mozete uzeti vise od 5 karata za let")
        
def izracunajVremeLeta():
    istampajLetove()
    sifra=input("Unesite sifru leta za koji zelite da saznate trajanje leta")
    print("Vreme trajanja leta je: ",letovi.izracunajVremeLeta(sifra)," minuta")
    
def zaposliRadnika():
    zaposleni={}
    zaposleni["ime"]=input("Unesite ime radnika")
    zaposleni["prezime"]=input("Unesite prezime radnika")
    zaposleni["username"]=input("Unesite username radnika")
    zaposleni["password"]=input("Unesite sifru radnika")
    zaposleni["pozicija"]=input("Unesite poziciju randika(sef,radnik)")
    Zaposleni.dodajZaposlenog(zaposleni)
    Zaposleni.snimiZaposlenog()
        
def otkaz():
    user=input("Unesite username zaposlenog koga zelite da otpustite")
    pozicija=input("Unesite poziciju tog radnika koga zelite da otpustite")
    Zaposleni.otpustiZaposlenog(user,pozicija)
    

print("GlavniProgram", __name__)   
if __name__ == "__main__":
    main() 

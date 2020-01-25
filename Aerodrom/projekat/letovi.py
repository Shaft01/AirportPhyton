
letovi=[]
def stringToLet(line):
    sifraLeta,model,grad,vreme1,vreme2,biznis,ekonomska,brSlB,brSlE,cenaB,cenaE =line.split("|")
    let={"sifraLeta":sifraLeta,"model":model,"grad":grad,"vreme1":vreme1,"vreme2":vreme2,"biznis":biznis,"ekonomska":ekonomska,"brSlB":brSlB,"brSlE":brSlE,"cenaB":cenaB,"cenaE":cenaE}
    return let;
def letToString(let):
    return "|".join((let["sifraLeta"],let["model"],let["grad"],let["vreme1"],let["vreme2"],let["biznis"],str(let["ekonomska"]),str(let["brSlB"]),str(let["brSlE"]),let["cenaB"],let["cenaE"]))

def ucitajLetove():
    for line in open("Let.txt","r"):
        s=stringToLet(line[:-1])
        letovi.append(s)
        
def snimiLetove():
    fajl=open("Let.txt","w")
    for i in letovi:
        fajl.write(letToString(i))
        fajl.write("\n")
    fajl.close()
    
def nadjiLet(sifraLeta):
    for i in letovi:
        if i["sifraLeta"]==sifraLeta:
            return i
        
def nadjiLetPoKljucu(kljuc,vrednost):
    pom=[]
    for i in letovi:
        if(i[kljuc].upper()== vrednost.upper()):
            
            pom.append(i)
    return pom
    

def formatHeader():
    return "Sifra leta |Model aviona |Grad      |Polazak  |Dolazak  |Biznis klasa |Ekonomska klasa |Br slobodnih B|Br slobodnih E|Cena Biznis|Cena Ekonomska\n "  \
           "----------|-------------|----------|---------|---------|-------------|----------------|--------------|--------------|-----------|--------------"
           
def formatLet(l):
    return "{0:11}|{1:13}|{2:10}|{3:9}|{4:9}|{5:13}|{6:16}|{7:14}|{8:14}|{9:11}|{10:14}".format(l["sifraLeta"], l["model"], l["grad"], l["vreme1"], l["vreme2"], l["biznis"], l["ekonomska"], l["brSlB"], l["brSlE"], l["cenaB"], l["cenaE"])
def izmeniLet(sifra,kljuc,vrednost):
    l=nadjiLet(sifra)
    l[kljuc]=vrednost
    
def sortiraj(kljuc,pocetak):
    minPos=nadjiMin(letovi,kljuc,pocetak)
    
    letovi[pocetak],letovi[minPos]=letovi[minPos],letovi[pocetak]
    if pocetak<len(letovi)-1:
        sortiraj(kljuc,pocetak+1)
        
    return letovi
        
def nadjiMin(l,kljuc,pocetak):
    n=len(l)
    if n==0 and n<=pocetak:
        return -1
    
    mina=l[pocetak]
    minPos=pocetak
    for i in range(pocetak+1,n):
        if l[i][kljuc]<mina[kljuc]:
            mina=l[i]
            minPos=i
    return minPos

def dodajLet(l):
    letovi.append(l)
    
def izracunajVremeLeta(sifra):
    l=nadjiLet(sifra)
    if l!=None:
        v1=l["vreme1"].split(":")
        v2=l["vreme2"].split(":")
        
        vreme1=int(v1[0])*60+int(v1[1])
        vreme2=int(v2[0])*60+int(v2[1])
        resenje=vreme2-vreme1
        hours = abs(resenje / 60)
        minutes = abs(resenje%60)

        leni = "%d:%02d" % (hours, minutes)
    return leni

def dodaj():
    let = {}
    let["sifraLeta"]=input("Unesite sifru leta")
    let["model"]=input("Unesite model aviona")
    let["grad"]=input("Unesite grad")
    let["vreme1"]=input("Unesite vreme leta")
    let["vreme2"]=input("Unesite vreme dolaska")
    let["biznis"]=input("Unesite broj sedista biznins klase")
    let["ekonomska"]=input("Unesite broj sedista ekonomske")
    let["brSlB"]=let["biznis"]
    let["brSlE"]=let["ekonomska"]
    let["cenaB"]=input("Unesite cenu karte u biznis klasi")
    let["cenaE"]=input("Unesite cenu karte u ekonomskoj")
    dodajLet(let)
    snimiLetove()

def obrisiLet(sifra):
    index=nadji(sifra)
    if index!=None:
        letovi.pop(index)
    else:
        print("Ne postoji let sa tom sifrom")
        
    
def nadji(sifra):
    for i,l in enumerate(letovi):
        if l["sifraLeta"]==sifra:
            return i
    return None


    
def racun(sifraLeta,klasa,karte):
    let=nadjiLet(sifraLeta)
    
    if let!= None:
        if klasa.lower()=="ekonomska" or klasa.lower()=="biznis":
            izdajRacun(let,klasa,karte)
            stampajRacun(let,klasa,karte)
            snimiLetove()
        else:
            print("uneli ste neispravnu klasu")
    else:
        print("Let sa tom siform ne postoji")

def izdajRacun(let,klasa,karte):
    ukupno=0;
    
    for i in range(int(karte)):
        if  klasa.lower()=="ekonomska":
            if int(let["brSlE"]) >0:
                ukupno=ukupno+int(let["cenaE"])
                let["brSlE"]=int(let["brSlE"])-1
                i=i+1
        elif klasa.lower()=="biznis":
            if int(let["brSlB"])>0:
                ukupno=ukupno+int(let["cenaB"])
                let["brSlB"]=int(let["brSlB"])-1
                i=i+1
    snimiLetove()
    return ukupno

def stampajRacun(let,klasa,karte):
    print(racunHeader())
    i=0
    while i<int(karte):
        print(formatRacun(let,klasa))
        i=i+1
    print(" Ukupna cena karata je ",izdajRacun(let,klasa,karte))
    
def racunHeader():
    return "Sifra leta |Model aviona|Grad      |Polazak  |Dolazak  |Klasa    |Broj sedista|Cena(u evrima)\n "\
           "-----------|------------|----------|---------|---------|---------|------------|--------------" 
            
def formatRacun(let,klasa):
    cena=0
    brojSed=1
    if klasa.lower()=="ekonomska":
        cena=let["cenaE"];
        brojSed=str(int(let["ekonomska"])-int(let["brSlE"]))
        let["brSlE"]=int(let["brSlE"])-1
        
    elif klasa.lower()=="biznis":
        cena=let["cenaB"]
        brojSed=str(int(let["biznis"])-int(let["brSlB"]))
        let["brSlB"]=int(let["brSlB"])-1
    return "{0:11}|{1:12}|{2:10}|{3:9}|{4:9}|{5:9}|{6:12}|{7:14}".format(let["sifraLeta"],let["model"],let["grad"],let["vreme1"],let["vreme2"],klasa,brojSed,cena)

print("letovi",__name__)
ucitajLetove()



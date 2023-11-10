# Skriv en funksjon som leser inn ei fil på følgende format, som inneholder data fra en
# værstasjon for hvert døgn over mange år:
# Navn; Stasjonsid; Dato på formen DD.MM.ÅÅÅÅ; snødybde i centimeter; nedbør i millimeter;
# middeltemperatur; gjennomsnittlig skydekke i en skala fra 0 (skyfritt) til 8 (helt
# overskyet);høyeste middelvind i meter pr. sekund.
# Merk at ikke alle dataene eksisterer for alle dagene, det vil være et «-» tegn for slike
# manglende data.
# Funksjonen skal lagre disse dataene i en eller flere lister eller dictionaries. Funksjonen skal
# returnere disse listene eller dictionaryene. Det er en del av oppgaven at dere finner ut hvilke
# datastrukturer som er mest hensiktsmessige til dette.


from datetime import datetime

class vardata:
    def __init__(self, navn, stasjonsid, dato, snodybde, nedbor, middeltemperatur, skydekke, middelvind):
        self.navn = navn
        self.stasjonsid = stasjonsid
        self.dato = dato
        self.snodybde = snodybde
        self.nedbor = nedbor
        self.middeltemperatur = middeltemperatur
        self.skydekke = skydekke
        self.middelvind = middelvind

    def __str__(self):
        return f"Navn: {self.navn}\nStasjonsid: {self.stasjonsid}\nDato: {self.dato}\nSnodybde: {self.snodybde}\nNedbor: {self.nedbor}\
\nMiddeltemperatur: {self.middeltemperatur}\nSkydekke: {self.skydekke}\nMiddelvind: {self.middelvind}" 

var_data = []

while True:
    try:
        filnavn = input("Skriv inn filnavn: ")
        with open(filnavn, "r", encoding = "utf-8") as fil:
            fil.readline()
            for linje in fil:
                linje_split = linje.split(";")
                if linje_split[0]!="Venabu":
                    continue
                linje_split = [ord.replace(",", ".") for ord in linje_split]
                linje_split[2] = datetime.strptime(linje_split[2], "%d.%m.%Y").date()
                linje_split[-1]=linje_split[-1].strip("\n")
                for i, ord in enumerate(linje_split[3:]):
                    if ord == "-":
                        linje_split[i+3] = None
                    else:
                        linje_split[i+3] = float(ord)
                data_ver=vardata(linje_split[0], linje_split[1], linje_split[2], linje_split[3], linje_split[4], linje_split[5], linje_split[6], linje_split[7])
                var_data.append(data_ver)
                var_data.sort(key=lambda x: x.dato)
        break
    except FileNotFoundError:
        print("Finner ikke filen, prøv igjen")


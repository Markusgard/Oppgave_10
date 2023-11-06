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
        fil = open(filnavn, "r", encoding = "utf-8")
        for linje in fil:
            linje = linje.strip()
            linje = linje.split(";")
            for i in range(3, len(linje)):
                if linje[i] == "-":
                    linje[i] = None
                else:
                    linje[i] = float(linje[i])
            var_data.append(vardata(linje[0], linje[1], linje[2], linje[3], linje[4], linje[5], linje[6], linje[7]))
        break
    except FileNotFoundError:
        print("Finner ikke filen, prøv igjen")

for i in var_data:
    print(i)
    print("\n")

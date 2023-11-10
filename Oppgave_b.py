# Dere kan regne med at det er skiføre om snødybden på værstasjonen er 20 centimeter eller
# mer. Regn ut antall dager med skiføre for hver vintersesong i datasettet. En vintersesong
# strekker seg fra oktober ett år til juni året etterpå. Bruk funksjonen fra del 1 oppgave d) til å
# beregne antall dager med skiføre i hver skisesong. Dette vil kreve at dere lager egne lister for
# hver skisesong som dere kan bruke som input til funksjonen fra del 1 oppgave d)

from Oppgave_a import *

def liste(flytliste , enkeltverdi) :
    antall_i_flytlisten = 0
    for num in flytliste :
        if num >= enkeltverdi :
            antall_i_flytlisten += 1
    return antall_i_flytlisten

from datetime import datetime

# Definer vardata-klassen som i din opprinnelige kode

# Din vardata-klasse og databehandlingskode forblir uendret

# Funksjon for å beregne antall dager med skiføre for en gitt liste med data
def beregn_skiføre_dager(data_liste):
    skiføre_dager = 0
    for data in data_liste:
        if data.snodybde is not None and data.snodybde >= 20:
            skiføre_dager += 1
    return skiføre_dager

# Initialiser variabler for å holde styr på vintersesonger og skiføre dager
vintersesonger = []
nåværende_vintersesong = []
skiføre_dager_per_sesong = []

for data_innlegg in var_data:
    # Sjekk om gjeldende datainnlegg faller innenfor en vintersesong
    if data_innlegg.dato.month in [10, 11, 12] or (data_innlegg.dato.month == 1 and data_innlegg.dato.day <= 31):
        nåværende_vintersesong.append(data_innlegg)
    elif data_innlegg.dato.month in [2, 3, 4, 5] or (data_innlegg.dato.month == 6 and data_innlegg.dato.day <= 30):
        nåværende_vintersesong.append(data_innlegg)
    else:
        # Datainnlegget er utenfor gjeldende vintersesong
        if nåværende_vintersesong:
            # Beregn antall skiføre dager for gjeldende vintersesong og lagre resultatet
            skiføre_dager = beregn_skiføre_dager(nåværende_vintersesong)
            skiføre_dager_per_sesong.append(skiføre_dager)
            # Legg til data for gjeldende vintersesong i listen over alle vintersesonger
            vintersesonger.append(nåværende_vintersesong)
        # Tilbakestill listen for gjeldende vintersesong
        nåværende_vintersesong = []

# Skriv ut eller lagre resultatene
for i, vinter_data in enumerate(vintersesonger):
    print(f"Vintersesong {i + 1}: Skiføre Dager = {skiføre_dager_per_sesong[i]}")

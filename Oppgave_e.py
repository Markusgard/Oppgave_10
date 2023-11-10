from Oppgave_a import *
import matplotlib.pyplot as plt

# Definer vardata-klassen som i din opprinnelige kode

# Din vardata-klasse og databehandlingskode forblir uendret

# Funksjon for å beregne vekst for den tenkte planten
# Funksjon for å beregne vekst for den tenkte planten
def beregn_vekst(data_liste):
    vekst_resultat = 0
    for grader in data_liste:
        if grader.middeltemperatur is not None and grader.middeltemperatur > 5:
            vekst_resultat += grader.middeltemperatur - 5
    return vekst_resultat


# Initialiser variabler for å holde styr på veksten og år
år = []
vekst_per_år = []
nåværende_år = var_data[0].dato.year
nåværende_år_data = []

for data_innlegg in var_data:
    if data_innlegg.dato.year != nåværende_år:
        # Beregn vekst for det nåværende året
        vekst_resultat = beregn_vekst(nåværende_år_data)
        
        # Sjekk om året er gyldig (minst 300 dager med temperaturdata)
        if len(nåværende_år_data) >= 300:
            år.append(nåværende_år)
            vekst_per_år.append(vekst_resultat)
        
        # Oppdater nåværende år og tilbakestill data for det nye året
        nåværende_år = data_innlegg.dato.year
        nåværende_år_data = []

    nåværende_år_data.append(data_innlegg)

# Beregn vekst for det siste året i datasettet
vekst_resultat = beregn_vekst(nåværende_år_data)

# Sjekk om det siste året er gyldig (minst 300 dager med temperaturdata)
if len(nåværende_år_data) >= 300:
    år.append(nåværende_år)
    vekst_per_år.append(vekst_resultat)

# Plot vekst for hvert år
plt.plot(år, vekst_per_år, marker='o', linestyle='-', color='b')
plt.xlabel('År')
plt.ylabel('Vekst for den tenkte planten')
plt.title('Vekst for den tenkte planten per år')
plt.show()

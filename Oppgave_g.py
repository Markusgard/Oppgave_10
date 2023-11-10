from Oppgave_a import *
import matplotlib.pyplot as plt

# Definer vardata-klassen som i din opprinnelige kode

# Din vardata-klasse og databehandlingskode forblir uendret

# Funksjon for å finne antall penværsdager for et år
def antall_penværsdager(data_liste):
    penværsdager = 0
    for data in data_liste:
        if data.skydekke is not None and data.skydekke <= 3:
            penværsdager += 1
    return penværsdager

# Initialiser variabler for å holde styr på antall penværsdager og år
år = []
penværsdager_per_år = []
nåværende_år = var_data[0].dato.year
nåværende_år_data = []

for data_innlegg in var_data:
    if data_innlegg.dato.year != nåværende_år:
        # Sjekk om det nåværende året er gyldig (minst 300 dager med skydekke-data)
        skydekke_dager = sum(1 for data in nåværende_år_data if data.skydekke is not None)
        if skydekke_dager >= 300:
            # Finn antall penværsdager for det nåværende året
            penværsdager = antall_penværsdager(nåværende_år_data)
            år.append(nåværende_år)
            penværsdager_per_år.append(penværsdager)
        
        # Oppdater nåværende år og tilbakestill data for det nye året
        nåværende_år = data_innlegg.dato.year
        nåværende_år_data = []

    nåværende_år_data.append(data_innlegg)

# Sjekk om det siste året er gyldig (minst 300 dager med skydekke-data)
skydekke_dager = sum(1 for data in nåværende_år_data if data.skydekke is not None)
if skydekke_dager >= 300:
    # Finn antall penværsdager for det siste året i datasettet
    penværsdager = antall_penværsdager(nåværende_år_data)
    år.append(nåværende_år)
    penværsdager_per_år.append(penværsdager)

# Plot antall penværsdager for hvert år
plt.plot(år, penværsdager_per_år, marker='o', linestyle='-', color='b')
plt.xlabel('År')
plt.ylabel('Antall penværsdager')
plt.title('Antall penværsdager for hvert år')
plt.show()

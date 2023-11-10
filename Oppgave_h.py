from Oppgave_a import *
import matplotlib.pyplot as plt
import statistics




# Funksjon for å finne høyeste middelvind og medianvind for et år
def vinddata_for_år(data_liste):
    vindstyrker = []
    for data in data_liste:
        if data.middelvind is not None:
            vindstyrker.append(data.middelvind)
    if not vindstyrker:
        return None, None
    høyeste_vind = max(vindstyrker)
    vindstyrker.sort()
    median_vind = statistics.median(vindstyrker)
    return høyeste_vind, median_vind


år = []
høyeste_vind_per_år = []
median_vind_per_år = []
nåværende_år = var_data[0].dato.year
nåværende_år_data = []

for data_innlegg in var_data:
    if data_innlegg.dato.year != nåværende_år:
        # Sjekk om det nåværende året er gyldig (minst 300 dager med vinddata)
        vind_dager = sum(1 for data in nåværende_år_data if data.middelvind is not None)
        if vind_dager >= 300:
            # Finn høyeste middelvind og medianvind for det nåværende året
            høyeste_vind, median_vind = vinddata_for_år(nåværende_år_data)
            if høyeste_vind is not None and median_vind is not None:
                år.append(nåværende_år)
                høyeste_vind_per_år.append(høyeste_vind)
                median_vind_per_år.append(median_vind)
        
        # Oppdater nåværende år og tilbakestill data for det nye året
        nåværende_år = data_innlegg.dato.year
        nåværende_år_data = []

    nåværende_år_data.append(data_innlegg)

# Sjekk om det siste året er gyldig (minst 300 dager med vinddata)
vind_dager = sum(1 for data in nåværende_år_data if data.middelvind is not None)
if vind_dager >= 300:
    # Finn høyeste middelvind og medianvind for det siste året i datasettet
    høyeste_vind, median_vind = vinddata_for_år(nåværende_år_data)
    if høyeste_vind is not None and median_vind is not None:
        år.append(nåværende_år)
        høyeste_vind_per_år.append(høyeste_vind)
        median_vind_per_år.append(median_vind)

# Plot høyeste middelvind og medianvind for hvert år
plt.plot(år, høyeste_vind_per_år, marker='o', linestyle='-', color='b', label='Høyeste vind')
plt.plot(år, median_vind_per_år, marker='x', linestyle='--', color='r', label='Median vind')
plt.xlabel('År')
plt.ylabel('Vindstyrke (m/s)')
plt.title('Høyeste middelvind og medianvind for hvert år')
plt.legend()
plt.show()

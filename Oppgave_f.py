from Oppgave_a import *
import matplotlib.pyplot as plt

# Definer vardata-klassen som i din opprinnelige kode

# Din vardata-klasse og databehandlingskode forblir uendret

# Funksjon for å finne den lengste perioden med tørke (ingen nedbør)
def longest_zero_sequence(lst):
    max_len = 0
    curr_len = 0
    for num in lst:
        if num == 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len

# Initialiser variabler for å holde styr på tørkeperioder og år
år = []
lengste_tørke_per_år = []
nåværende_år = var_data[0].dato.year
nåværende_år_data = []

for data_innlegg in var_data:
    if data_innlegg.dato.year != nåværende_år:
        # Sjekk om det nåværende året er gyldig (minst 300 dager med nedbørsdata)
        nedbør_dager = sum(1 for data in nåværende_år_data if data.nedbor is not None)
        if nedbør_dager >= 300:
            # Finn den lengste tørkeperioden for det nåværende året
            lengste_tørke = longest_zero_sequence([1 if data.nedbor is None or data.nedbor == 0 else 0 for data in nåværende_år_data])
            år.append(nåværende_år)
            lengste_tørke_per_år.append(lengste_tørke)
        
        # Oppdater nåværende år og tilbakestill data for det nye året
        nåværende_år = data_innlegg.dato.year
        nåværende_år_data = []

    nåværende_år_data.append(data_innlegg)

# Sjekk om det siste året er gyldig (minst 300 dager med nedbørsdata)
nedbør_dager = sum(1 for data in nåværende_år_data if data.nedbor is not None)
if nedbør_dager >= 300:
    # Finn den lengste tørkeperioden for det siste året i datasettet
    lengste_tørke = longest_zero_sequence([1 if data.nedbor is None or data.nedbor == 0 else 0 for data in nåværende_år_data])
    år.append(nåværende_år)
    lengste_tørke_per_år.append(lengste_tørke)

# Plot den lengste tørkeperioden for hvert år
plt.plot(år, lengste_tørke_per_år, marker='o', linestyle='-', color='b')
plt.xlabel('År')
plt.ylabel('Lengste tørkeperiode (dager)')
plt.title('Lengste tørkeperiode for hvert år')

# Angi at x- og y-aksen skal vise heltall
plt.xticks([int(x) for x in plt.xticks()[0]])
plt.yticks([int(y) for y in plt.yticks()[0]])

plt.show()

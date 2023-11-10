from Oppgave_a import *
import matplotlib.pyplot as plt

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

# Beregn trenden for skiføre dager per sesong
år = [entry[0].dato.year for entry in vintersesonger]
trend = [0]  # Trenden for det første året (starter på 0 skiføre dager)
for i in range(1, len(skiføre_dager_per_sesong)):
    endring = skiføre_dager_per_sesong[i] - skiføre_dager_per_sesong[i - 1]
    trend.append(trend[-1] + endring)

# Plot trenden
plt.plot(år, trend)
plt.xlabel('Året skisesongen starter')
plt.ylabel('Antall dager med skiføre')
plt.title('Trenden for antall dager med skiføre per skisesong')
plt.show()


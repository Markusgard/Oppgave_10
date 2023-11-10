from Oppgave_a import *
import matplotlib.pyplot as plt


def gjennomsnittstemperatur_for_måned(data_liste, måned):
    gjennomsnittstemperaturer = []
    år_år = []  # Liste for å holde år
    for år in range(2006, 2019):  # Anta årene i datasettet
        måned_data = [data for data in data_liste if data.dato.year == år and data.dato.month == måned]
        temperaturer = [data.middeltemperatur for data in måned_data if data.middeltemperatur is not None]
        gjennomsnitt = sum(temperaturer) / len(temperaturer) if temperaturer else None
        if gjennomsnitt is not None:
            gjennomsnittstemperaturer.append(gjennomsnitt)
            år_år.append(str(år))
    
    return år_år, gjennomsnittstemperaturer

# Funksjon for å beregne differansen i gjennomsnittstemperatur mellom påfølgende år
def differanse_i_gjennomsnittstemperatur(gjennomsnittstemperaturer):
    differanser = [gjennomsnittstemperaturer[i] - gjennomsnittstemperaturer[i - 1] for i in range(1, len(gjennomsnittstemperaturer))]
    return differanser

# Initialiser variabler for å holde styr på gjennomsnittstemperaturer og differanser
år_år, gjennomsnittstemperaturer = gjennomsnittstemperatur_for_måned(var_data, måned=8)  # 8 for august
differanser = differanse_i_gjennomsnittstemperatur(gjennomsnittstemperaturer)

# Plot gjennomsnittstemperaturer
plt.figure(figsize=(12, 6))
plt.plot(år_år, gjennomsnittstemperaturer, marker='o', linestyle='-', color='b', label='Gjennomsnittstemperatur')
plt.xlabel('År')
plt.ylabel('Gjennomsnittstemperatur (°C)')
plt.title('Gjennomsnittstemperatur for august hvert år')

# Plot differanser
plt.plot(år_år[1:], differanser, marker='o', linestyle='-', color='r', label='Differanse')
plt.ylabel('Differanse i gjennomsnittstemperatur (°C)')

plt.legend()
plt.tight_layout()
plt.show()

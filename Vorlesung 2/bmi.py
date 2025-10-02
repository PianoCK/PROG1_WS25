# BMI Rechner
# Eingabe
gewicht_kg = input("Gib Dein Gewicht in kg ein:") # Achtung: ist ein string
groesse_cm = float(input("Gib Deine Größe in cm ein:")) # Erst input, dann Typumwandlung

# Typumwandlung
gewicht_kg = float(gewicht_kg) # Typ von str --> float
# groesse_cm = float(groesse_cm) # ist schon ein float --> siehe Zeile 4

# Verarbeitung
bmi = gewicht_kg / ((groesse_cm/100) ** 2)

# Ausgabe
print("Dein BMI ist", round(bmi,1))



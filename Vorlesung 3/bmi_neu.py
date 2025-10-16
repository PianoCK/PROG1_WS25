# BMI Rechner
# Eingabe
try:
    gewicht_kg = float(input("Gib Dein Gewicht in kg ein:")) 
    groesse_cm = float(input("Gib Deine Größe in cm ein:")) 
except:
    print("Das hat leider nicht geklappt. Bitte nur Zahlen eingeben")
    exit()

# Verarbeitung
bmi = gewicht_kg / ((groesse_cm/100) ** 2)

# Ausgabe
print("Dein BMI ist", round(bmi,1))



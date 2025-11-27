# Bei primitiven Datentypen wie int, str, bool, float machen wir immer ein 
# "Call by Value"
text1 = "Hallo"
text2 = text1
text1 = text1 + " Studys!"

print(text1)
print(text2)

# Bei allen anderen (komplexen) Datentypen machen wir ein "Call by Reference"
liste1 = [2, 3, 4]
print("Typ:", type(liste1))
print("Speicheradresse:", id(liste1))
print(liste1)


liste2 = liste1.copy()  # Das wäre ein komplette Kopie des Speichers
liste2 = liste1         # Die Referenz wird nur kopiert 
liste1.append(5)

print(liste1)
print(liste2)

def addiere_zu_liste(liste):
    liste.append("1")

addiere_zu_liste(liste1)
print(liste1)

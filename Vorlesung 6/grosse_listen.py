#        0 1 2 3 4 5  6 7 8 9 10                                   24 25
liste = [6,3,5,8,7,64,3,4,6,7,7,6,54,6,54,6,776,5,44,56,54,56,54,5,43,234]
liste2 = []

# Erste Methode für das Iterieren einer Liste
for i in range(len(liste)): # len(liste)=26, also Zahlen von 0..25
    if liste[i] > 50:
        liste2.append(liste[i])
print(liste2)

# Zweite Methode für das Iterieren einer Liste
for elem in liste:
    if elem > 50:
        print(elem)


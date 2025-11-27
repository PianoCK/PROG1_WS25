liste_klassisch = [1, True, "Hallo", 23.5]
telefonliste = {"Peter": "0152-98231155",
                "Jutta": "0171-8883211",
                "Kathrin": "0152-99966311",
                "Guido": "0177-1155669912"}
telefonliste["Jochen"] = "0161-39873231"
telefonliste["Lionel"] = "0178-99912331"

for element in liste_klassisch:
    print(element)

for element in telefonliste:
    print(element, telefonliste[element])
# Dictionary. Komplexität ist O(1)
# Key/Value-Paare
telefonliste = {"Peter": "0152-98231155",
                "Jutta": "0171-8883211",
                "Kathrin": {"telefonnummer": "0152-99966311",
                            "anschrift":"Hauptstr. 32"},
                "Guido": "0177-1155669912"}

telefonliste["Jochen"] = "0161-39873231"
telefonliste["Lionel"] = "0178-99912331"
telefonliste["Lionel"] = "0153-999442211"

print(telefonliste["Kathrin"]["anschrift"])
zwischenspeicher = telefonliste["Kathrin"]
telefonliste["NeueKathrin"] = zwischenspeicher
class Auto:
    def __init__(self, automarke):
        self.marke = automarke
        self.farbe = "rot"  
        self.__kmstand = 0   # privates Attribut, lässt sich nicht von "außen" ändern

    def fahren(self, km):
        if km >=0:
            self.__kmstand += km
        else:
            print("Fehler")

    def get_kmstand(self):
        return self.__kmstand

auto1 = Auto("BMW")
auto1.fahren(50)
auto1.fahren(23)
auto1.fahren(189)
print(auto1.get_kmstand())
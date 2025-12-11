# Kaffeemaschine
# strom: bool

class Kaffeemaschine:
    seriennummer = 100000001
    anzahl_kaffeemaschinen = 0

    def __init__(self):
        self.strom = False
        self.counter = 0 # Anzahl der Einheitskaffeezubereitungen
        self.seriennummer = Kaffeemaschine.seriennummer # Bei der Erstellung einer Kaffeemaschine erhält diese eine Seriennummer
        Kaffeemaschine.seriennummer += 1
        Kaffeemaschine.anzahl_kaffeemaschinen += 1

    def __del__(self):
        Kaffeemaschine.anzahl_kaffeemaschinen -= 1

    def __str__(self):
        return f"Jura {self.seriennummer}"

    def power_button(self):
        self.strom = not self.strom

    def checke_trester(self):
        if self.counter >= 5:
            print("Trester voll!!")

    def entleere_trester(self):
        self.counter = 0

    def kaffee_kochen(self):
        if self.strom:
            print("wwwwwwwwshhhhhhh......")
            self.counter += 1
            self.checke_trester()

class KaffeemaschineMitMilchaufschäumer(Kaffeemaschine):
    def milch_aufschäumen(self):
        print("Schhhhhhhhhhh....")


print("Aktuelle Seriennummer", Kaffeemaschine.seriennummer)
# Hier ist die Objekterstellung
jura_1000 = Kaffeemaschine()
jura_1001 = KaffeemaschineMitMilchaufschäumer()
jura_1001.power_button()
jura_1001.kaffee_kochen()
jura_1001.milch_aufschäumen()
print(f"Status Jura 1000 {jura_1000.strom} und Jura 1001 {jura_1001.strom}")
del jura_1000
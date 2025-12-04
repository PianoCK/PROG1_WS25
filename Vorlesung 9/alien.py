# Bei OOP können wir selber eigene Datentypen bauen!!!
class Alien:
    def __init__(self, alienname, health): # Diese magische Methode wird bei der Instanziierung aufgerufen
        self.health = health
        self.name = alienname

    def hit(self):
        self.health = self.health - 20
        if self.health <= 0:
            print(f"{self} destroyed")
        else:
            print(f"{self} get hit! {self} health = {self.health}")

    def roar(self):
        print(f"{self} Grrrrrr---roaoooor!!")

    def __repr__(self):  # Diese magische Methode wird bei print() aufgerufen
        return f"Alien('{self.name}', {self.health})"

alien1 = Alien("Goblin", 20)
alien2 = Alien("Boss", 100)  
alien2.roar()
alien2.hit()
alien1.hit()

class Ticket:
    ticketnummer = 1

    def __init__(self):
        self.ticketnummer = Ticket.ticketnummer
        Ticket.ticketnummer += 1
        self.gueltigkeit = True

    def scannen(self):
        self.gueltigkeit = False

class Konzert:
    def __init__(self, name):
        self.name = name
        self.tickets = []

eminem = Konzert("HH 03.05.2026")

for i in range(100):
    eminem.tickets.append(Ticket())


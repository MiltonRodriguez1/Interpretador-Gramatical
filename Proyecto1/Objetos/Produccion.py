class Produccion:
    Contador = 0
    NombreGram = ""
    Estado1 = ""
    Estado2 = ""
    Terminal = ""

    def __init__(self, nombreGram, estado1,estado2,terminal):
        self.NombreGram = nombreGram
        self.Estado1 = estado1
        self.Estado2 = estado2
        self.Terminal = terminal

    def Show(self):
        return self

    def setNombreGram(self, nombreGram):
        self.NombreGram = nombreGram

    def getNombreGram(self):
        return self.NombreGram

    def setEstado1(self, estado1):
        self.Estado1 = estado1

    def getEstado1(self):
        return self.Estado1

    def setEstado2(self, estado2):
        self.Estado2 = estado2

    def getEstado2(self):
        return self.Estado2

    def setTerminal(self, terminal):
        self.Terminal = terminal

    def getTerminal(self):
        return self.Terminal


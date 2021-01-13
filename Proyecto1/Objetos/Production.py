class Production:
    Contador = 0
    NombreGram = ""
    Cadena = ""
    EstadoInicial = ""
    Prducciones = ""
    Aceptacion = ""
    Id = 0

    def __init__(self, nombreGram, cadena):
        self.NombreGram = nombreGram
        self.Cadena = cadena

    def Show(self):
        return self

    def setNombreGram(self, nombreGram):
        self.NombreGram = nombreGram

    def getNombreGram(self):
        return self.NombreGram

    def setId(self, id):
        self.Id = id

    def getId(self):
        return self.Id

    def setCadena(self, cadena):
        self.Cadena = cadena

    def getCadena(self):
        return self.Cadena

    def setEstadoInicial(self, estadoInicial):
        self.EstadoInicial = estadoInicial

    def getEstadoInicial(self):
        return self.EstadoInicial

    def setPrducciones(self, prducciones):
        self.Prducciones = prducciones

    def getPrducciones(self):
        return self.Prducciones

    def setAceptacion(self, aceptacion):
        self.Aceptacion = aceptacion

    def getAceptacion(self):
        return self.Aceptacion
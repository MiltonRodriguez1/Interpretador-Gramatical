class AFD:
    Nombre = ""
    Contador = 0
    Estados = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    ContadorEstados = 0
    Alfabeto = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,4,3,44,45,46,47,48,49,50]
    ContadorAlfabeto = 0
    EstadoInicial = ""
    EstadoAceptacion = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    ContadorEstadoAceptacion = 0
    Transiciones = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    ContadorTransiciones = 0
    CadenasEvaluadas = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,4,3,44,45,46,47,48,49,50,51,52,53,54]
    ContadorCadenasEvaluadas = 0

    #Functions
    def __init__(self, nombre):
        self.Nombre = nombre
        
    def Show(self):
        return self

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setContadorEstado(self, numero):
        self.ContadorEstados = numero

    def getContadorEstado(self):
        return self.ContadorEstados

    def setEstados(self, estado):
        self.Estados[self.getContadorEstado()] = estado
        self.setContadorEstado(self.getContadorEstado()+1)
        

    def getEstados(self):
        return self.Estados
    #sd
    def setContadorTransiciones(self, numero):
        self.ContadorTransiciones = numero

    def getContadorTransiciones(self):
        return self.ContadorTransiciones

    def setTransiciones(self, estado):
        self.Transiciones[self.getContadorTransiciones()] = estado
        self.setContadorTransiciones(self.getContadorTransiciones()+1)
        

    def getTransiciones(self):
        return self.Transiciones

    #sd
    def setContadorCadenasEvaluadas(self, ContadorCadenasEvaluadas):
        self.ContadorCadenasEvaluadas = ContadorCadenasEvaluadas

    def getContadorCadenasEvaluadas(self):
        return self.ContadorCadenasEvaluadas

    def setCadenasEvaluadas(self, cadenaevaluada):
        self.CadenasEvaluadas[self.getContadorCadenasEvaluadas()] = cadenaevaluada
        self.setContadorCadenasEvaluadas(self.getContadorCadenasEvaluadas()+1)
        
        

    def getCadenasEvaluadas(self):
        return self.CadenasEvaluadas
    #sd


    def setContadorEstadoAceptacion(self, numero):
        self.ContadorEstadoAceptacion = numero

    def getContadorEstadoAceptacion(self):
        return self.ContadorEstadoAceptacion

    def setEstadoAceptacion(self, estado):
        self.EstadoAceptacion[self.getContadorEstadoAceptacion()] = estado
        self.setContadorEstadoAceptacion(self.getContadorEstadoAceptacion()+1)
        

    def getEstadoAceptacion(self):
        return self.EstadoAceptacion


    def setContadorAlfabeto(self, numero):
        self.ContadorAlfabeto = numero

    def getContadorAlfabeto(self):
        return self.ContadorAlfabeto

    def setAlfabeto(self, letra):
        self.Alfabeto[self.getContadorAlfabeto()] = letra
        self.setContadorAlfabeto(self.getContadorAlfabeto()+1)
        

    def getAlfabeto(self):
        return self.Alfabeto

    def getEstadoInicial(self):
        return self.EstadoInicial

    def setEstadoInicial(self, estado):
        self.EstadoInicial = estado
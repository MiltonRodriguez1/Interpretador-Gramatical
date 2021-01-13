import Objetos.AFD as AFD
global objeto
objeto = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

class ControladorAFD:
     #Search AFD
    def SearchAfd(nombre):
        c = False;
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == nombre:
                c = True
                return True
        return c

    #Return AFD
    def returnAfd(nombre):
        c = False;
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == nombre:
                return afdC
        return c
        
    #Create new AFD
    def newAfd(nombre):
        check = ControladorAFD.SearchAfd(nombre)
        
        if check != True:
            newObjetct = AFD.AFD(nombre)
            objeto[AFD.AFD.Contador] = newObjetct
            AFD.AFD.Contador = AFD.AFD.Contador +1
        return nombre
    
   

    def ShowAfd():
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            print("Nombre: ",afdC.getNombre())
        return False

    def NewState(name,state):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                inttent = True
                for j in range(afdC.getContadorEstado()):
                    if afdC.getEstados()[j] == state:
                        inttent = False
                if inttent == True:
                    afdC.setEstados(state)
                    return True
        return False

    def NewCadena(name,cadenaevaluada):
        #Create new Cadena
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                afdC.setCadenasEvaluadas(cadenaevaluada)
                return True
        return False
    def NewAlphabet(name,letter):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                inttent = True
                for j in range(afdC.getContadorAlfabeto()):
                    if afdC.getAlfabeto()[j] == letter:
                        inttent = False
                if inttent == True:
                    afdC.setAlfabeto(letter)
                    return True
        return False

    def SearchAlphabet(name,letter):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                inttent = True
                for j in range(afdC.getContadorAlfabeto()):
                    if afdC.getAlfabeto()[j] == letter:
                        inttent = False
                if inttent == True:
                    return True
        return False
    def Terminales(name):
        #Create new State
        Cadena = ""
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                
                for j in range(afdC.getContadorEstado()):
                    Cadena = Cadena +","+ afdC.getEstados()[j] 
                        
                
        return Cadena
    def NoTerminales(name):
        #Create new State
        Cadena = ""
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                
                for j in range(afdC.getContadorAlfabeto()):
                   Cadena= Cadena + ","+afdC.getAlfabeto()[j]

        return Cadena

    def InitialState(name,state):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                
                for j in range(afdC.getContadorEstado()):
                    if afdC.getEstados()[j] == state:
                        
                        afdC.setEstadoInicial(state)
                        return True
                
        return False


    def AcceptanceState(name,state):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                
                for j in range(afdC.getContadorEstado()):
                    if afdC.getEstados()[j] == state:
                        com = True
                        for k in range(afdC.getContadorEstadoAceptacion()):
                            if afdC.getEstadoAceptacion()[k] == state:
                                com = False
                        if com == True:
                            afdC.setEstadoAceptacion(state)
                            return True
                
        return False

    def TryAcceptanceState(name,state):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                
                for j in range(afdC.getContadorEstado()):
                    if afdC.getEstados()[j] == state:
                        com = True
                        for k in range(afdC.getContadorEstadoAceptacion()):
                            if afdC.getEstadoAceptacion()[k] == state:
                                com = False
                        if com == True:
                            
                            return True
                
        return False

    def TryState(name,state):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                
                for j in range(afdC.getContadorEstado()):
                    if afdC.getEstados()[j] == state:
                        
                        return True
                
        return False

    def InsertTransition(name,transition):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
            if afdC.getNombre() == name:
                afdC.setTransiciones(transition)
                return True
                
        return False

    def InsertCadena(name,cadena):
        #Create new State
        for i in range(AFD.AFD.Contador):
            afdC = AFD.AFD.Show(objeto[i])
           
            if afdC.getNombre() == name:
                for nd in range(afdC.getContadorCadenasEvaluadas()):
                    cade1 = ""
                    tcade1 = True
                    for pala in afdC.getCadenasEvaluadas()[nd]:
                        if tcade1 == True:
                            if pala == " ":
                                tcade1 = False
                            else:
                                cade1 = cade1 + pala

                    if cade1 == cadena:
                        return False
                    
                afdC.setCadenasEvaluadas(cadena)
                return True
                
        return False
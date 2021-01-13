import Objetos.Produccion as Production
global objeto
objeto = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
class ControladorProduccion:
    #New Production
    def existe(namegram,state1,terminal):
        for i in range(Production.Produccion.Contador):
            productions = Production.Produccion.Show(objeto[i])
            if productions.getNombreGram() == namegram and productions.getEstado1() == state1 and productions.getTerminal() == terminal:
                return True
        return False

    def newProduction(namegram,state1,state2,terminal):
       vres = ControladorProduccion.existe(namegram,state1,terminal)
       if vres == False:
            newPro= Production.Produccion(namegram,state1,state2,terminal)
            objeto[Production.Produccion.Contador] = newPro
            Production.Produccion.Contador = Production.Produccion.Contador+1
            return True
       else:
            return False
       

    def way(namegram,state1, terminal):
        for i in range(Production.Produccion.Contador):
            productions = Production.Produccion.Show(objeto[i])
            if productions.getNombreGram ()== namegram and productions.getEstado1() == state1:
                if terminal == "♥":
                    terminal = "epsilon"
                if productions.getTerminal() == terminal:
                    return productions.getEstado2()
        return False
                


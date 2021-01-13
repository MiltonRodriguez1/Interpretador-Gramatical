from graphviz import Digraph
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from msvcrt import getch
import Objetos.Production as Production
import Controladores.ControladorAFD as Prod
global objeto
global comprobador
global Cadena_Arbol
global comprobador1
global Cadena_Arbol1
global Contador1
global Contador2
objeto = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
comprobador = True
Cadena_Arbol = ""
comprobador1 = True
Cadena_Arbol1 = ""
Contador1 = 0
class ControladorProduccion:
    Contador2 = 0
    elementos=[]

    def __init__(self):
        self.elements = []

    def get_size(self):
        return len(self.elements)

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.pop()

    def get_peek(self):
        return self.elements[-1]

    def print_stack(self): 
        print(self.elementos)

    peek = property(fget=get_peek)
    size = property(fget=get_size)



    #New Production
    def existe(namegram,Cadena):
        for i in range(Production.Production.Contador):
            productions = Production.Production.Show(objeto[i])
            if productions.getNombreGram() == namegram and productions.getCadena() == Cadena:
                return True
        return False

    def newProduction(namegram,Cadena):
       vres = ControladorProduccion.existe(namegram,Cadena)
       if vres == False:
            newPro= Production.Production(namegram,Cadena)
            newPro.setId(Production.Production.Contador)
            objeto[Production.Production.Contador] = newPro
            Production.Production.Contador = Production.Production.Contador+1
            return True
       else:
            return False

    def ShowProduction(namegram,Cadena):
        for i in range(Production.Production.Contador):
            productions = Production.Production.Show(objeto[i])
            if productions.getNombreGram() == namegram and productions.getCadena() == Cadena:
                return productions
        return ""

    def Eliminar(namegram,Cadena):
        for i in range(Production.Production.Contador):
            productions = Production.Production.Show(objeto[i])
            if productions.getNombreGram() == namegram and productions.getCadena() == Cadena:
                newPro= Production.Production(" "," ")
                objeto[i] = newPro
                return True
        return False

    def Insertar_inicial(namegram,Cadena,noterminal,production):
        for i in range(Production.Production.Contador):
            productions = Production.Production.Show(objeto[i])
            if productions.getNombreGram() == namegram and productions.getCadena() == Cadena:
                productions.setEstadoInicial(noterminal)
                productions.setPrducciones(production)
                return True
        return False

    def recursividad(namegram,Cadena,Caracter):
        regresar = ""
        initi = True
        ini = ""
        for i in range(Production.Production.Contador):
           productions = Production.Production.Show(objeto[i])
           if productions.getNombreGram() == namegram and productions.getEstadoInicial() == Cadena:
               
               if initi == True:
                   ini = productions.getCadena()
                   initi = False
               a = True
               b = ""
               for j in productions.getPrducciones():
                   if a== True:
                       b = j
                       
                       a = False
               if b.isupper() == True:
                   
                   regresar = ControladorProduccion.recursividad(namegram,b,Caracter)
                   if regresar != "":
                    
                    return ini
                   
               else:
                   
                   if b == Caracter:
                       
                       return ini

           initi = True
           ini = ""
           Cadena_Arbol = ""
        return regresar

    def recursividad1(namegram,Cadena,Caracter):
        
        regresar = ""
        initi = True
        ini = ""
        for i in range(Production.Production.Contador):
           productions = Production.Production.Show(objeto[i])
           if productions.getNombreGram() == namegram and productions.getEstadoInicial() == Cadena:
               
               
               if initi == True:
                   ini = productions.getCadena()
                   initi = False
               a = True
               b = ""
               for j in productions.getPrducciones():
                   if a== True:
                       b = j
                       
                       a = False
               if b.isupper() == True:
                   
                   regresar = ControladorProduccion.recursividad(namegram,b,Caracter)
                   if regresar != "":
                    
                    return productions.getPrducciones()
                   
               else:
                   
                   if b == Caracter:
                       
                       return productions.getPrducciones()

           initi = True
           ini = ""
           Cadena_Arbol1 = ""
        return regresar
    def encontrar_ultimo(namegram,Estado,Caracter):
        regresar = ""
        initi = True
        ini = ""
        for i in range(Production.Production.Contador):
           productions = Production.Production.Show(objeto[i])
           if productions.getNombreGram() == namegram and productions.getEstadoInicial() == Estado:
               
               if initi == True:
                   ini = productions.getPrducciones()
                   initi = False
               a = True
               b = ""
               for j in productions.getPrducciones():
                   if j== " ":
                       b = ""
                   else:
                       b = b+ j
                       
               if b.isupper() == True:
                   
                   regresar = ControladorProduccion.encontrar_ultimo(namegram,b,Caracter)
                   if regresar != "":
                    
                    return regresar
                    
               else:
                   
                   if b == Caracter:
                       
                       return b

           initi = True
           ini = ""
           Cadena_Arbol = ""
        return regresar

    
    def Valid(namegram,Cadena, Prod,s,f,Produccion_inicial,pila,fx,inicial):
                   
                    

                    Val = False
                    
                    vali = ""
                    for ff in Prod:
                     if s.get_size() > 0:
                      
                      if s.get_peek() == "#" and f.get_size() <= 0 and pila.get_size() <= 0:
                            
                                Val = True
                        

                      elif ff == " ":
                          
                          if vali != "":
                            fx.attr('node', shape='circle')
                            fx.node(vali)
                            fx.edge(inicio, vali, "")
                            
                            if vali.isupper() == True:
                               
                               proc= ControladorProduccion.recursividad1(namegram,vali,s.get_peek())
                               
                               if proc != "":
                                   
                                   u = ""
                                   ty = True
                                   tyd = ""
                                   for le in proc:
                                       if le == " ":
                                           if ty== True:
                                               tyd = u
                                               ty = False
                                           pila.push(u)
                                           fx.attr('node', shape='circle')
                                           fx.node(u)
                                           f.edge(Vali, u, "")
                                           u = ""
                                       else:
                                            u = u + le
                                   pila.push(u)
                                   fx.attr('node', shape='circle')
                                   fx.node(u)
                                   fx.edge(vali, u, "")
                                   
                                   ControladorProduccion.Valid(namegram,Cadena, proc,s,f,Produccion_inicial,pila,fx,tyd)
                                   if pila.get_size() > 0:
                                    pila.pop()
                               
                                   

                            else:
                                if s.get_peek() == vali or s.get_peek() == "epsilon":
                                    fx.attr('node', shape='circle')
                                    fx.node(vali)
                                    fx.edge(inicio, vali, "")
                                    
                                    if pila.get_size() > 0:
                                        pila.pop()
                                    if s.get_size() > 0:
                                        s.pop()
                                else:
                                    return False
                            vali = ""

                      else:
                            vali = vali + ff
                     else:
                
                        return Val
                     if vali!="":
                        if vali.isupper() == True:
                               proc= ControladorProduccion.recursividad1(namegram,vali,s.get_peek())
                               
                               if proc != "":
                                   u = ""
                                   ty = True
                                   tyd = ""
                                   for le in proc:
                                       if le == " ":
                                           if ty== True:
                                               tyd = u
                                               ty = False
                                           pila.push(u)
                                           fx.attr('node', shape='circle')
                                           fx.node(u)
                                           fx.edge(vali, u, "")
                                           u = ""
                                       else:
                                            u = u + le

                                   fx.attr('node', shape='circle')
                                   fx.node(vali)
                                   ControladorProduccion.Valid(namegram,Cadena, proc,s,f,Produccion_inicial,pila,fx,tyd)
                                   
                                   print(proc+"#  ")
                                   
                                   if pila.get_size() > 0:
                                    pila.pop()

                        else:
                                if s.get_peek() == vali or s.get_peek() == "epsilon":
                                    
                                    if s.get_size() > 0:
                                        s.pop()
                                    
                                    if pila.get_size() > 0:
                                     pila.pop()
                                    if f.get_size() > 0:
                                        f.pop()
                                else:
                                    return False
                        vali = ""
                     
                    return Val

    
        
    def MethodValidar(namegram,Cadena):
        Validez = True
        entrada = True
        Produccion_inicial = ""
        CadenaValuada = ""
        Ca = ""
        Principio = True
        af = Prod.ControladorAFD.returnAfd(namegram)
        inicio = af.getEstadoInicial()
        
        for letra in Cadena:
            
            for i in range(Production.Production.Contador):
                productions = Production.Production.Show(objeto[i])
                
                if productions.getNombreGram() == namegram and productions.getEstadoInicial() == af.getEstadoInicial():
                    if Principio == True:
                        
                        Produccion_inicial = ControladorProduccion.recursividad(namegram,productions.getEstadoInicial(),letra)
                        
                        Principio = False

        if Produccion_inicial == "":
            return ""
        else:
           s = ControladorProduccion()
           e = ControladorProduccion()
           pila = ControladorProduccion()
           number = len(Cadena)
           for r in Cadena:
               number = number -1
               s.push(Cadena[number])
               

            
            
           pym = ControladorProduccion.ShowProduction(namegram,Produccion_inicial)
           g = ""
           number1 = len(pym.getPrducciones())
           for u in pym.getPrducciones():
               if u == " ":
                number = number -1
                e.push(g)
                g = ""
               else:
                   g = g+u
           f = ControladorProduccion()
           for i in range(e.get_size()):
               asd = e.pop()
               f.push(asd)
               
           fx = Digraph(format='png', name='salida')
           fx.attr(rankdir='LR', size='8,5')
           inicial = ""
           alov = True
           for alo in Produccion_inicial:
               if alov == True:
                    if alo == " ":
                        alov = False
                    else:
                        inicial = inicial + alo
           tryex= ControladorProduccion.Valid(namegram,Cadena, pym.getPrducciones(),s,f,Produccion_inicial,pila,fx,inicial)

           fx.attr('node', shape='none')
           fx.attr('edge', arrowhead='empty', arrowsize='1.5')
           fx.edge('', 'S', None)
           fx.render()      
           if tryex == True:
               return "Valida"
           else:
               return "Invalida"
           
           Cadena_Arbol = ""
           comprobador1 = True
           Cadena_Arbol1 = ""
           



    def Insertar_Aceptacion(namegram,Cadena,noterminal):
        for i in range(Production.Production.Contador):
            productions = Production.Production.Show(objeto[i])
            if productions.getNombreGram() == namegram and productions.getCadena() == Cadena:
                productions.setAceptacion(noterminal)
                return True
        return False


                    




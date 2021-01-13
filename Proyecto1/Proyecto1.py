#IMPORTS
import os

import Controladores.ControladorAFD as AFDControl
import Objetos.AFD as AFD
import Controladores.ControladorProduccion as ProductionControl
import Controladores.ControladorProduction as ProductionC
import Objetos.Produccion as Pproductions
import Objetos.Production as ProductionO
from graphviz import Digraph
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter
from msvcrt import getch
import random



#CARATULA
print("==========================================================")
print("||           LENGUAJES FORMALES Y DE PROGRAMACIÓN       ||")
print("||                       SECCION B-                     ||")
print("||                       201807435                      ||")
print("==========================================================")
input()
os.system("cls")

#MAIN_MENU  

Repeater = True
while Repeater == True:
    print("####################  MENU PRINCIPAL  ##################")
    print("1. Crear AFD")
    print("2. Crear Gramática")
    print("3. Evaluar Cadenas")
    print("4. Reportes")
    print("5. Cargar archivo de Entrada")
    print("6. Guardar")
    print("7. Gramáticas tipo2 y AP")
    print("0. Salir")
    try:
        option = int(input())
    except ValueError:
        print("Ingrese un numero")
        option = 7
    os.system("cls")
    if option == 1:
        #CREATE AFD
        print("Ingrese El Nombre del AFD")
        nameafd = input()
        AFDControl.ControladorAFD.newAfd(nameafd)
        os.system("cls")
        repeater1 = True
        while repeater1 == True:
            os.system("cls")
            print("********* MENU DEL AFD ",nameafd," *********")
            print("1. Ingresar Estados")
            print("2. Ingresar Alfabeto")
            print("3. Estado Inicial")
            print("4. Estados de aceptación")
            print("5. Transiciones")
            print("6. Ayuda")
            print("0. Menu Principal")
            try:
                optioncrear = int(input())
            except ValueError:
                print("Ingrese un numero")
                optioncrear = 7
            if optioncrear == 1:
                #Enter States
                repeatstates = True
                while repeatstates == True:
                    os.system("cls")
                    state = input("Ingrese el nombre del Estado: ")
                    state = state.upper()
                    trystate = AFDControl.ControladorAFD.SearchAlphabet(nameafd,state)
                    if trystate == False:
                        print("El Estado que esta intentado ingresar pertenece al alfabeto: Ingrese otro nombre de estado")
                    
                    else:
                        trystate = AFDControl.ControladorAFD.NewState(nameafd,state)
                        if trystate == False:
                            print("El Estado ya ha sido creado anteriormente: Estado No Creado")
                        else:
                            print("Estado Creado Correctamente")

                    print("Elija una Opcion")
                    print("1. Crear Otro Estado")
                    print("2. Salir")
                    try:
                        op = int(input())
                    except ValueError:
                        print("Ingrese un numero")
                        op = 2
                    if op == 2:
                        repeatstates = False
                        




            elif optioncrear == 2:
                #Enter alphabet
                repeatstates = True
                while repeatstates == True:
                    os.system("cls")
                    alphabet = input("Ingrese un elemento del Alfabeto: ")
                    alphabet=alphabet.lower()
                    trystate = AFDControl.ControladorAFD.NewAlphabet(nameafd,alphabet)
                    if trystate == False:
                        print("El elemento del Alfabeto ya ha sido creado")
                    else:
                        print("Alfabeto Ingresado Correctamente")

                    print("Elija una Opcion")
                    print("1. Ingresar otro elemento")
                    print("2. Salir")
                    try:
                        op = int(input())
                    except ValueError:
                        print("Ingrese un numero")
                        op = 2
                    if op == 2:
                        repeatstates = False
            elif optioncrear == 3:
                #Initial State
                print("Ingrese el estado inicial: ")
                initialstate = input()
                initialstate = initialstate.upper()
                tryinitial = AFDControl.ControladorAFD.InitialState(nameafd,initialstate)
                if tryinitial == True:
                    input("Estado Inicial Creado Correctamente, Presione Enter para continuar: ")
                else:
                    input("El Estado que desea nombrar no existe, Presione Enter para continuar")
            elif optioncrear == 4:
                #Acceptance States
                repeateracceptance = True
                while repeateracceptance == True:
                    print("Ingrese un estado de aceptacion: ")
                    initialstate = input()
                    initialstate = initialstate.upper()
                    tryinitial = AFDControl.ControladorAFD.AcceptanceState(nameafd,initialstate)
                    if tryinitial == True:
                             ProductionControl.ControladorProduccion.newProduction(nameafd,initialstate,"finish","epsilon")
                             transitiion1 = initialstate+ ";epsilon;"
                             AFDControl.ControladorAFD.InsertTransition(nameafd,transitiion1)
                             print("Ingrese 1 para Ingresar otro estado y 2 para continuar")
                             leerrepe = input()
                             if leerrepe == "1":
                                    repeateracceptance = True
                             else:
                                    repeateracceptance = False
                    else:
                        input("El Estado que desea nombrar no existe, Presione Enter para continuar")
                        repeateracceptance = False
            elif optioncrear == 5:
                #Transitions
                
                repeatTransition = True
                while repeatTransition == True:
                    os.system("cls")
                    print("*************** Ingresar Transiciones *******************")
                    print("1. Metodo Normal")
                    print("2. Metodo 1 ")
                    print("3. Metodo 2")
                    print("0. Salir")
                    option_transition = input()
                    if option_transition == "1":
                        repeater_M_normal = True
                        while repeater_M_normal == True:
                            os.system("cls")
                            print("Ingrese el Primer Estado")
                            E1 = input()
                            E1 = E1.upper()
                            trye1 = AFDControl.ControladorAFD.TryState(nameafd,E1)
                            if trye1 == True:
                                print("Ingrese el Segundo Estado")
                                E2 = input()
                                E2 = E2.upper()
                                trye2 = AFDControl.ControladorAFD.TryState(nameafd,E2)
                                if trye2 == True:
                                    print("Ingrese el lenguaje de relacion")
                                    E3 = input()
                                    E3 = E3.lower()
                                    trye3 = AFDControl.ControladorAFD.SearchAlphabet(nameafd,E3)
                                    if trye3 == False:
                                        preg = ProductionControl.ControladorProduccion.newProduction(nameafd,E1,E2,E3)
                                        if preg == False:
                                            print("La Producrrion ya a sido creada anteriormente o no puede dirigirse a dos estados diferentes con el mismo lenguaje")
                                        else:
                                            transitiion = E1+";"+E2+";"+E3
                                            AFDControl.ControladorAFD.InsertTransition(nameafd,transitiion)
                                        print("Desea ingresar otra Transition")
                                        print("1.Si")
                                        print("2.No")
                                        c1 = input()
                                        if c1 == "1":
                                            repeater_M_normal = True
                                        else:
                                            repeater_M_normal = False

                                    else:
                                        print("Error el elemento del lenguaje no existe, Empiece de Nuevo")
                                else:
                                    print("Error el Estado No Existe Empiece de Nuevo")
                            else:
                                print("Error el Estado No Existe Empiece de Nuevo")
                    elif option_transition == "2":
                        #Metodo 1
                        repeater_metodo1 = True
                        while repeater_metodo1 == True:
                            os.system("cls")
                            print("****************** METODO 1 *****************")
                            
                            print("Ingresar de la siguiente Manera:")
                            print("[terminales separados por comas] (Columnas)")
                            print("[no terminales separados por comas] (filas)")
                            print("[símbolos destino] (interior matriz por filas por comas y columnas por punto y coma)")
                            print("Ejemplo:")
                            print("[a, b]")
                            print("[A, B, C, D]")
                            print("[A, C; A, C; B, D; -, -]")
                            print("Presionar Enter Entre cada Linea")
                            Terminales = input()
                            Terminales = Terminales.strip()
                            
                            NoTerminales = input()
                            NoTerminales = NoTerminales.strip()
                            Simbolos = input()
                            Simbolos = Simbolos.strip()
                            terminales = ""
                            terminales =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                            contadorterminales = 0
                            noterminales = ""
                            noterminales =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                            contadornoterminales = 0
                            terminal = ""
                            a1 = True
                            for t in Terminales:
                                print(t)
                                if a1 == True:
                                    if t == "," or t == "]":
                                        
                                        terminal = terminal.lower()
                                        re = AFDControl.ControladorAFD.SearchAlphabet(nameafd,terminal)
                                        
                                        if re != True:
                                           pass
                                        else:
                                            terminales[contadorterminales] = terminal+""
                                            contadorterminales = contadorterminales + 1
                                        terminal = ""


                                    else:
                                        if t != "[" and t != "]":
                                            terminal = terminal +t
                                
                            terminal = ""
                            for n in NoTerminales:
                                
                                a1 = True
                                if a1 == True:
                                    if t == "," or t=="]":
                                        
                                        terminal = terminal.upper()
                                        
                                        re = AFDControl.ControladorAFD.TryState(nameafd,terminal)
                                        print(terminal)
                                        
                                        if re != True:
                                            pass
                                        else:
                                            noterminales[contadornoterminales] = terminal+""
                                            contadornoterminales = contadornoterminales + 1 
                                        terminal = ""

                                    elif n != "[" and n != "]":
                                        terminal = terminal +n
                                
                                        
                            contadorprosucciones = 0
                            contadorno = 0
                            for s in Simbolos:
                                teminal1 = ""
                                teminal2 = ""
                                t1 = True
                                t2 = True
                                if t1 == True:
                                    if s == "," or "]":
                                       if teminal1 != "-":
                                        ter1 = terminales[contadorprosucciones]
                                        print(ter1)
                                        note1 = noterminales[contadorno]
                                        print(note1)
                                        preg = ProductionControl.ControladorProduccion.newProduction(nameafd,note1,teminal1,ter1)
                                      
                                        if preg != False:
                                            trans = note1+";"+teminal1+";"+ter1
                                            AFDControl.ControladorAFD.InsertTransition(nameafd,trans)
                                        else:
                                            trans = note1 + ";"+teminal1+";"+ter1
                                            print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")
                                        terminal1 = ""
                                        contadorno = contadorno+1

                                    elif s == ";":
                                        
                                            if teminal1 != "-":
                                                ter1 = terminales[contadorprosucciones]
                                                note1 = noterminales[contadorno]
                                                print(ter1)
                                                print(note1)
                                                preg = ProductionControl.ControladorProduccion.newProduction(nameafd,note1,teminal1,ter1)
                                      
                                                if preg != False:
                                                    trans = note1 + ";"+teminal1+";"+ter1
                                                    AFDControl.ControladorAFD.InsertTransition(nameafd,trans)
                                                else:
                                                    trans = note1.upper() + ";"+teminal1.upper()+";"+ter1.lower()
                                                    print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")
                                        
                                            contadorno = 0
                                            contadorprosucciones = contadorprosucciones +1
                                            terminal1 = ""


                                    else:
                                        if s != "[" and s != "]":
                                            teminal1 = teminal1 + s
                            print("Guardado Correctamente")
                            print("Desea Ingresar Otra Codena: 1.Si cualquier tecla no")
                            leermetodo = input()
                            if leermetodo == "1":
                                repeater_metodo1 = True
                            else:
                                repeater_metodo1 = False

                    
                    elif option_transition == "3":
                        #Metodo 2
                        repeater_Op_3 = True
                        while repeater_Op_3 == True:
                            os.system("cls")
                            print("********************************** Metodo 2 *************************************")
                            print("Ingrese la transicion de la siguiente manera: No_Terminal,No_Terminal;Terminal")
                            print("Ejemplo: A,B;0")
                            Cade = input()
                            e1 = ""
                            e2 = ""
                            tt1 = ""
                            r1 = True
                            r2 = True
                            for ca in Cade:
                                if r1 == True:
                                    if ca == ",":
                                        r1 = False
                                    else:
                                        e1 = e1 +ca
                                elif r2 == True:
                                    if ca == ";":
                                        r2 = False
                                    else:
                                        e2 = e2 + ca
                                else:
                                    tt1 = tt1 + ca
                            resp = ProductionControl.ControladorProduccion.newProduction(nameafd,e1.upper(),e2.upper(),tt1.lower())
                            print(e1)
                            print(e2)
                            print(tt1)


                            if resp != False:
                                cade1 = e1.upper()+";"+e2.upper()+";"+tt1.lower();
                                AFDControl.ControladorAFD.InsertTransition(nameafd,cade1)
                            else:
                                print("La Cadena ya existe o no puede estar relacionado mas de un estado con un mismo terminal")
                            print("Guardado. Desea Ingresar otra cadena:  1.Si Cualquier tecla. No")
                            repe = input()
                            if repe == "1":
                                repeater_Op_3 = True
                            else:
                                repeater_Op_3 = False
                    else:
                        #Exit
                        repeatTransition = False

            elif optioncrear == 6:
                #Help
                print("==========================================================")
                print("||           LENGUAJES FORMALES Y DE PROGRAMACIÓN       ||")
                print("||                       SECCION B-                     ||")
                print("||                       Luis Yela                      ||")
                print("||                           5                          ||")
                print("==========================================================")
                input() 
            elif optioncrear == 0:
                #Main Menu
                repeater1 = False
                os.system("cls")


    elif option == 2:
        #CREATE GRAMMAR
        print("Ingrese el nombre de la gramatica")
        namegramar = input()
        AFDControl.ControladorAFD.newAfd(namegramar)
        RepeaterGramar = True
        while RepeaterGramar == True:
            os.system("cls")
            print("************************* GRAMATICA DE NOMBRE "+namegramar+" *************************")
            print("1. Ingresar NT")
            print("2. Ingresar Terminales")
            print("3. NT Inicial")
            print("4. Producciones")
            print("5. Mostrar gramática Transformada")
            print("6. Ayuda")
            print("0. Salir")
            optiongramar = input()
            if optiongramar == "1":
                #add NT
                os.system("cls")
                repeater_add_NT = True
                while repeater_add_NT == True:
                   name_NT = input("Ingrese Un estado No Terminal o el signo mas (+) para salir: ")
                   name_NT = name_NT.upper()
                   if name_NT == "+":
                       repeater_add_NT = False
                   else:
                        tryt_NT = AFDControl.ControladorAFD.NewState(namegramar,name_NT)
                        if tryt_NT == False:
                            print("El Estado ya ha sido creado anteriormente o pertence a un estado Terminal: Estado No Creado ")
                        else:
                            print("Estado Terminal Correctamente")


                
            elif optiongramar == "2":
                #add Finished
                os.system("cls")
                repeater_add_T = True
                while repeater_add_T == True:
                   name_T = input("Ingrese Un estado Terminal o el signo mas (+) para salir: ")
                   name_T = name_T.lower()
                   if name_T == "+":
                       repeater_add_T = False
                   else:

                        tryt_T = AFDControl.ControladorAFD.NewAlphabet(namegramar,name_T)
                        if tryt_T == False:
                            print("El Estado ya ha sido creado anteriormente o pertence a un estado No Terminal: Estado No Creado ")
                        else:
                            
                            print("Estado Terminal Creado Correctamente")
                
            elif optiongramar == "3":
                #Start NT
                os.system("cls")
                print("Ingrese un No Terminal inicial: ")
                initialstate1 = input()
                initialstate1 = initialstate1.upper()
                tryinitial1 = AFDControl.ControladorAFD.InitialState(namegramar,initialstate1)
                if tryinitial1 == True:
                    input("El No Terminal Inicial Creado Correctamente, Presione Enter para continuar: ")
                else:
                    input("El No Terminal que desea nombrar como inicial no existe, Error: Presione Enter para continuar")
            elif optiongramar == "5":
                #Transformation
                print("*****************************Gramatica Regular***************************************")
                nameafd1 = AFDControl.ControladorAFD.returnAfd(namegramar)
                for i in range(nameafd1.getContadorTransiciones()):
                    
                    transitions = nameafd1.getTransiciones()[i]
                    state1 = ""
                    state2 = ""
                    l = ""
                    a = True
                    b= True
                
                    for j in transitions:
                        if a == True:
                            if j == ";":
                                a=False
                            else:
                                state1 = state1 + j
                        elif b == True:
                            if j == ";":
                                b= False
                            else:
                                state2 = state2 + j
                        else:
                            l = l+j
                
                    cadena = state1+" → "+l +" "+state2
                    print(cadena)
                print("************************ Gramatica Con Recusividad Por La Izquierda **************************")
                input("Presione Enter Para Continuar....")
            elif optiongramar == "4":
                #Productions
                os.system("cls")
                repeater_Transition = True
                while repeater_Transition == True:
                    
                    print("Ingrese la gramatica de la siguiente forma separado por espacios NO_TERMINAL_1 > TERMINAL NO_TERMINAL_2")
                    typing = input()
                    Name_Carga_AFD = namegramar
                    State1 = ""
                    State2 = ""
                    Alph = ""
                    
                    b1 = True
                    b2 = True
                    b3 = True
                    b4 = True
                    for C_A in typing:
                        if b1 == True:
                            if C_A == " ":
                                b1 = False
                            else:
                                State1 = State1 + C_A
                        elif b2 == True:
                            if C_A == " ":
                                b2 = False
                        elif b3 == True:
                            if C_A == " ":
                                b3 = False
                            else:
                                State2 = State2 + C_A
                        elif b4 == True:
                            if C_A == "|":
                                if State2 == "epsilon":
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)

                                    
                                    AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1)
                                    
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,"finish",State2)
                                    if preg != False:
                                        trans = State1 + "; ;"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                    else:
                                        trans = State1 + "; ;"+State2
                                        print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")
                                else:
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")

                                    
                                    
                                    AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,State1+"'",State2)
                                    if preg != False:
                                        trans = State1 + ";"+State1+"';"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                        preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'","finish","epsilon")
                                        if preg1 != False:
                                                trans = State1 + "'; ;epsilon"
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                    else:
                                        trans = State1 + ";"+State1+"';"+State2
                                        print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")
                                            
                                b4 = False
                            elif C_A == " ":
                                    State1 = State1.upper()
                                    if Alph.isupper() == True:
                                        AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                        AFDControl.ControladorAFD.NewState(Name_Carga_AFD,Alph)

                                        
                                        AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)
                                        preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,Alph,State2)
                                        if preg != False:
                                            trans = State1 + ";"+Alph+";"+State2
                                            AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                        else:
                                            trans = State1 + ";"+Alph+";"+State2
                                            print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")

                                        b4 = False
                                    elif State2.isupper() == True:
                                        #Gramatica por la izquiera
                                            
                                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                            

                                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State2+"'")
                                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State2+"'")
                                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")
                                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1+"'")
                                            AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,Alph)
                                            preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'",State2+"'",Alph)
                                            if preg != False:
                                                trans = State1 + "';"+State2+"';"+Alph
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                            else:
                                                trans = State1 + "';"+State2+"';"+Alph
                                                print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")

                                            preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State2+"'","finish","epsilon")
                                            if preg1 != False:
                                                trans = State2 + "'; ;epsilon"
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)

                                            b4 = False

                            else:
                                Alph = Alph + C_A
                        else:
                            if C_A == " ":
                                State2 = ""
                                Alph = ""
                                b3 = True
                                b4 = True
                    if State1 != "" and State2 != "" and Alph != "" and State1 != " " and State2 != " " and Alph != " ":
                        State1 = State1.upper()
                        if Alph.isupper() == True:
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,Alph)

                            
                            AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)
                            preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,Alph,State2)
                            if preg != False:
                                trans = State1 + ";"+Alph+";"+State2
                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                            else:
                                trans = State1 + ";"+Alph+";"+State2
                                print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")

                        elif State2.isupper() == True:
                                        #Gramatica por la izquiera
                                            
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                            

                                            
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State2+"'")
                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State2+"'")
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")
                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1+"'")
                            AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,Alph)
                            preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'",State2+"'",Alph)
                            if preg != False:
                                trans = State1 + "';"+State2+"';"+Alph
                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                            else:
                                trans = State1 + "';"+State2+"';"+Alph
                                print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")

                            preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State2+"'","finish","epsilon")
                            if preg1 != False:
                                trans = State2 + "'; ;epsilon"
                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                    elif State1 != "" and State2 != "" and State1 != " " and State2 != " ":
                        if State2 == "epsilon":
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)

                                    
                                    AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1)
                                    
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,"finish",State2)
                                    if preg != False:
                                        trans = State1 + "; ;"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                    else:
                                        trans = State1 + "; ;"+State2
                                        print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")
                        else:
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")
                                    AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)

                                    
                                    
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,State1+"'",State2)
                                    if preg != False:
                                        trans = State1 + ";"+State1+"';"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                        preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'","finish","epsilon")
                                        if preg1 != False:
                                                trans = State1 + "'; ;epsilon"
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                    else:
                                        trans = State1 + ";"+State1+"';"+State2
                                        print("La Produccion "+trans +" Ya ha sido Creada o no Puede Relacionarse Dos No Terminales con el mismo Terminal")
                    print("************Producciones Creadas Correctamente***********")
                    print("Desea Ingresar otra produccion: ")
                    print("1.Si")
                    print("2.No")
                    res_gramar = input()
                    if res_gramar == "2":
                        os.system("cls")
                        repeater_Transition = False
                        
                        

            elif optiongramar == "6":
                #Help
                print("==========================================================")
                print("||           LENGUAJES FORMALES Y DE PROGRAMACIÓN       ||")
                print("||                       SECCION B-                     ||")
                print("||                       Luis Yela                      ||")
                print("||                           5                          ||")
                print("==========================================================")
                print("")
                input("Presione Enter Para Continuar...")
                os.system("cls")

            else:
                #Exit
                RepeaterGramar = False
                os.system("cls")

        
    elif option == 3:
        #EVALUATE CHAINS
        os.system("cls")
        Name_evaluate = input("Ingrese El Nombre de la Gramatica")
        check = AFDControl.ControladorAFD.SearchAfd(Name_evaluate)
        if check == True:
            
            repeater_evaluate = True
            while repeater_evaluate == True:
                os.system("cls")
                print("*********************** Menu de Evaluar Cadenas ***********************")
                print("1. Solo Validar")
                print("2. Ruta en AFD")
                print("3. Expandir con Gramatica")
                print("4. Ayuda")
                print("0. Salir")
                option_evaluate = input()
                if option_evaluate == "1":
                    #ONLY VALUATE
                    R_Only = True
                    os.system("cls")
                    print("*************** SOLO VALIDAR ******************")
                    while R_Only == True:
                        
                        
                        print("Ingrese La Cadena a evaluar")
                        Chain = input()
                        value = "Valida"
                        chain = Chain+"♥"
                        try_chain = True
                        stance = AFDControl.ControladorAFD.returnAfd(Name_evaluate)
                        actual_state = stance.getEstadoInicial()
                        for i in chain:
                            actual_state = ProductionControl.ControladorProduccion.way(Name_evaluate,actual_state,i)
                            if actual_state == False:
                                value = "Invalida"
                        print(Chain+ " Es: "+ value)                    
                        value = Chain +"|"+ value
                       
                        AFDControl.ControladorAFD.NewCadena(Name_evaluate,value)
                        answer = input("Desea Ingresar otra cadena: (1. Si) Cualquier Tecla (No) ")
                        if answer != "1":
                            R_Only = False
                elif option_evaluate == "2":
                    #DIRECTION IN AFD
                    os.system("cls")
                    R_Only = True
                    print("****************** RUTA EN AFD ******************")
                    while R_Only == True:
                        
                        print("Ingrese La Cadena a evaluar")
                        Chain = input()
                        value = "Valida"
                        Ruta_Afd = ""
                        chain = Chain+"♥"
                        try_chain = True
                        stance = AFDControl.ControladorAFD.returnAfd(Name_evaluate)
                        actual_state = stance.getEstadoInicial()
                        for i in chain:
                            stateP = actual_state
                            actual_state = ProductionControl.ControladorProduccion.way(Name_evaluate,actual_state,i)
                            if actual_state == False:
                                value = "Invalida"
                            else:
                                if i != "♥":
                                    Ruta_Afd = Ruta_Afd+stateP+","+actual_state+","+i+";"
                        
                        print("Ruta AFD: "+Ruta_Afd +" "+value)
                                            
                        value = Chain +"|"+ value
                       
                        AFDControl.ControladorAFD.NewCadena(Name_evaluate,value)
                        answer = input("Desea Ingresar otra cadena: (1. Si) Cualquier Tecla (No) ")
                        if answer != "1":
                            R_Only = False
                elif option_evaluate == "3":
                    #EXPANDIR
                    R_Only = True
                    os.system("cls")
                    print("************** EXPANDIR CON GRAMATICA*************")
                    while R_Only == True:
                        
                        print("Ingrese La Cadena a evaluar")
                        Chain = input()
                        value = "Valida"
                        Ruta_Afd = ""
                        evaluate_now = ""
                        chain = Chain+"♥"
                        try_chain = True
                        stance = AFDControl.ControladorAFD.returnAfd(Name_evaluate)
                        actual_state = stance.getEstadoInicial()
                        Ruta_Afd = actual_state
                        for i in chain:
                            stateP = actual_state
                            actual_state = ProductionControl.ControladorProduccion.way(Name_evaluate,actual_state,i)
                            if actual_state == False:
                                value = "Invalida"
                            else:
                                if i == "♥":
                                    i = "(epsilon)→"
                                evaluate_now = evaluate_now + i
                                if actual_state == "finish":
                                    actual_state = ""
                                Ruta_Afd = Ruta_Afd+"→"+evaluate_now+actual_state
                        
                        print("Ruta AFD: "+Ruta_Afd + " "+Chain+ " "+value)
                                            
                        value = Chain +"|"+ value
                       
                        AFDControl.ControladorAFD.NewCadena(Name_evaluate,value)
                        answer = input("Desea Ingresar otra cadena: (1. Si) Cualquier Tecla (No) ")
                        if answer != "1":
                            R_Only = False
                elif option_evaluate == "4":
                    #HELP
                    print("==========================================================")
                    print("||           LENGUAJES FORMALES Y DE PROGRAMACIÓN       ||")
                    print("||                       SECCION B-                     ||")
                    print("||                       Luis Yela                      ||")
                    print("||                           5                          ||")
                    print("==========================================================")
                    print("")
                    input("Presione Enter Para Continuar...")
                else:
                    #Exit
                    repeater_evaluate = False

        else:
            print("El Nombre de la Gramatica no existe")
    elif option == 4:
     repeater_Reports = True
     os.system("cls")
     while repeater_Reports == True:
      print("******************************* MENU REPORTES *******************************")
      print("1. Detalles")
      print("2. Generar Reporte")
      print("3. Ayuda")
      print("0. Salir")
      option_Reports = input()
      if option_Reports == "1":
        #Details
        print("************ Grmatica ***********")
        print("*          No Terminales        *")
        print("*           Terminales          *")
        print("*            Inicio             *")
        print("*          Producciones         *")
        print("*********************************")
        print("")
        print("*************** AFD *************")
        print("*             Alfabeto          *")
        print("*             Estados           *")
        print("*           Estado Inicial      *")
        print("        Estados de Aceptacion   *")
        print("                Grafo           *")
        print("*********************************")
        print("")
        input("Presione Enter Para Continuar....")
      elif option_Reports == "2":
        #REPORTS
        w,h= letter
        print("Ingrese el Nombre del AFD")
        name = input()
        trynameafd = AFDControl.ControladorAFD.SearchAfd(name);
        if trynameafd == True:
            c = canvas.Canvas(name+".pdf", pagesize=letter)
            h=h-50
            
            cadena12 = ""
            cadena1 = ""
            cadena3 = ""
            cadena4 = ""
            cadena5 = ""
            cadena6 = ""
            nameafd1 = AFDControl.ControladorAFD.returnAfd(name)
            c.drawString(260,h,name+"")
            h = h-30
            positionafd = h
            positiongramar = h
            ##########################################################################GRAMATICA REGULAR##############################################
            
            c.drawString(60,h,"*********GRAMATICA REGULAR*********")
            h = h-20
            

            #No Terminales
            #State
            for inf6 in range(nameafd1.getContadorEstado()):
                cadena6 = cadena6 + nameafd1.getEstados()[inf6]+ ", "
            c.drawString(50,h,"Estados= {"+cadena6+"}")
            h = h-20
            
            #Terminales
            for inf5 in range(nameafd1.getContadorAlfabeto()):
                cadena5 = cadena5 + nameafd1.getAlfabeto()[inf5]+ ", "
            c.drawString(50,h,"Terminales = {"+cadena5+"}")
            h = h-20

            #Start
            c.drawString(50,h,nameafd1.getEstadoInicial()+" = Inicio")
            h = h-20

            #Productions
            c.drawString(50,h,"Producciones:")
            h = h-20
            elementos = ""
            elementos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            contador = 0
            f = Digraph(format='png', name='salida')
            f.attr(rankdir='LR', size='8,5')
            for i in range(nameafd1.getContadorTransiciones()):

                transitions = nameafd1.getTransiciones()[i]
                state1 = ""
                state2 = ""
                l = ""
                a = True
                b= True
                
                for j in transitions:
                    if a == True:
                        if j == ";":
                            a=False
                        else:
                            state1 = state1 + j
                    elif b == True:
                        if j == ";":
                            b= False
                        else:
                            state2 = state2 + j
                    else:
                        l = l+j
                crear = True
                crear2 = True
                cadena = state1+" → "+l +" "+state2
                for leer in range(contador+1):
                    if elementos[leer] == state1:
                        crear = False
                if crear == True:
                    typestate = AFDControl.ControladorAFD.TryAcceptanceState(name,state1)
                    if state1 != "" and state1 != " " and state1 != "  " and state1 != "epsilon":
                        if typestate == False:
                            f.attr('node', shape='doublecircle')
                            f.node(state1)
                            elementos[contador] = state1
                            contador = contador +1
                        else:
                            f.attr('node', shape='circle')
                            f.node(state1)
                            elementos[contador] = state1
                            contador = contador +1

                for leer1 in range(contador+1):
                    if elementos[leer1] == state2:
                        crear2 = False
                if crear2 == True:
                    typestate = AFDControl.ControladorAFD.TryAcceptanceState(name,state2)
                    if state2 != "" and state2 != " " and state2 != "  " and state2 != "epsilon":
                        if typestate == False:
                            f.attr('node', shape='doublecircle')
                            f.node(state2)
                            elementos[contador] = state2
                            contador = contador +1
                        else:
                            f.attr('node', shape='circle')
                            f.node(state2)
                            elementos[contador] = state2
                            contador = contador +1

                if l != "epsilon" and state1 != "epsilon" and state2 != "epsilon":   
                    f.edge(state1, state2, l)
                
                c.drawString(130,h,cadena)
                h = h-18
            f.attr('node', shape='none')
            f.attr('edge', arrowhead='empty', arrowsize='1.5')
            f.edge('', nameafd1.getEstadoInicial(), None)
            f.render() 
             ##########################################################################AFD##############################################
            positiongramar = h
            h = positionafd
            c.drawString(330,h,"********* AFD *********")
            h = h-20

            #Language
            for inf1 in range(nameafd1.getContadorAlfabeto()):
                cadena1 = cadena1 + nameafd1.getAlfabeto()[inf1]+ ", "
            c.drawString(320,h,"Lenguaje= {"+cadena1+"}")
            h = h-20

            #State
            for inf in range(nameafd1.getContadorEstado()):
                cadena12 = cadena12 + nameafd1.getEstados()[inf]+ ", "
            c.drawString(320,h,"Estados= {"+cadena12+"}")
            h = h-20
            
            #Acceptance States
            for inf3 in range(nameafd1.getContadorEstadoAceptacion()):
                cadena3 = cadena3 + nameafd1.getEstadoAceptacion()[inf3]+ ", "
            c.drawString(320,h,"Estados de Aceptacion= {"+cadena3+"}")
            h = h-20

            #Start
            c.drawString(320,h,"Estado Inicial= "+nameafd1.getEstadoInicial())
            h = h-20
            #Grafo
            c.drawImage('salida.gv.png', 280, h-140, 280, 150)
            h = h-160

            #Valid String
            c.drawString(320,h,"Cadenas Validas:")
            h = h-20
            at = True
            validez = ""
            cade = ""

            ################################################################## Create Chains #########################################################
            #Validas
            for creat in range(3):
                value = "Valida"
                
                stateinitial = nameafd1.getEstadoInicial();
                alphabet_AFD = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
                Contador_Alphabet = 0
                Repeater_Creater = True
                Chain = ""
                while Repeater_Creater == True:
                    
                    for i in range(Pproductions.Produccion.Contador):
                
                        productions = Pproductions.Produccion.Show(ProductionControl.objeto[i])
                        if productions.getNombreGram() == nameafd1.getNombre() and productions.getEstado1() == stateinitial:
                            alphabet_AFD[Contador_Alphabet] = productions
                            Contador_Alphabet = Contador_Alphabet + 1
                    if Contador_Alphabet != 0:
                        pos = random.randint(0, Contador_Alphabet-1)
                    else:
                        pos = 0
                    productions1 = Pproductions.Produccion.Show(alphabet_AFD[pos])
                    if productions1.getTerminal()+"" == "epsilon":
                        Repeater_Creater = False
                    else:
                        Chain = Chain + productions1.getTerminal()
                        stateinitial = productions1.getEstado2()
                        Contador_Alphabet = 0


                                    
                value = Chain +"|"+ value
                       
                AFDControl.ControladorAFD.NewCadena(nameafd1.getNombre(),value)
                value = ""
                #Invalidas
            for creat in range(3):
                Counting = 0
                Inic = ""
                value = "Invalida"
                stateinitial = nameafd1.getEstadoInicial();
                alphabet_AFD = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
                Contador_Alphabet = 0
                Repeater_Creater = True
                Chain = ""
                while Repeater_Creater == True:
                    
                    for i in range(Pproductions.Produccion.Contador):
                
                        productions = Pproductions.Produccion.Show(ProductionControl.objeto[i])
                        if productions.getNombreGram() == nameafd1.getNombre() and productions.getEstado1() == stateinitial:
                            alphabet_AFD[Contador_Alphabet] = productions
                            Contador_Alphabet = Contador_Alphabet + 1
                    if Contador_Alphabet != 0:
                        pos = random.randint(0, Contador_Alphabet-1)
                    else:
                        pos = 0

                    for er in range(nameafd1.getContadorAlfabeto()):
                        for re in range(Contador_Alphabet):
                            productionsp = Pproductions.Produccion.Show(alphabet_AFD[re])
                            if productionsp.getTerminal() != nameafd1.getAlfabeto()[er]:
                                Inic = nameafd1.getAlfabeto()[er]

                    
                    productions1 = Pproductions.Produccion.Show(alphabet_AFD[pos])
                    trystate1 = AFDControl.ControladorAFD.TryAcceptanceState(nameafd1.getNombre(),productions1.getEstado1())
                    if productions1.getTerminal() == "epsilon":
                        
                        
                        stateinitial = nameafd1.getEstadoInicial()
                        Contador_Alphabet = 0
                        if Counting > 1:
                           if trystate1 == True:
                                Repeater_Creater = False
                    else:
                        if trystate1 == True:
                                Repeater_Creater = False
                        if Counting > 3:
                            Repeater_Creater = False

                        Chain = Inic + Chain + productions1.getTerminal()
                        stateinitial = productions1.getEstado2()
                        Contador_Alphabet = 0
                        


                    Counting = Counting + 1                    
                value = Chain +"|"+ value
                       
                AFDControl.ControladorAFD.NewCadena(nameafd1.getNombre(),value)
                value = ""
            
            ################################################################## Print Chains ##########################################################
            
            for ui in range(nameafd1.getContadorCadenasEvaluadas()):
                for iu in nameafd1.getCadenasEvaluadas()[ui]:
                    if at == True:
                        cade = cade + iu
                    if at == False and iu != "|":
                        validez = validez + iu
                    if iu == "|":
                        at = False

                if validez == "Valida":
                    c.drawString(320,h,cade+"")
                    h = h-20
                validez = ""
                at = True
                cade = ""

                #Invalid String
            c.drawString(320,h,"Cadenas Invalidas:")
            h = h-20
            at = True
            validez = ""
            
            for ui in range(nameafd1.getContadorCadenasEvaluadas()):
                for iu in nameafd1.getCadenasEvaluadas()[ui]:
                    if at == False:
                        validez = validez + iu
                    if iu == "|":
                        at = False

                if validez == "Invalida":
                    c.drawString(320,h,nameafd1.getCadenasEvaluadas()[ui]+"")
                    h = h-20
                validez = ""
                at = True
            
            
            if h < 50:
                c.showPage()
                h = positionafd
            c.drawString(260,h,"Cadenas Evaluadas")
            h = h-25

            for ui in range(nameafd1.getContadorCadenasEvaluadas()):
               
                if h < 50:
                    c.showPage()
                    h = positionafd
                c.drawString(230,h,nameafd1.getCadenasEvaluadas()[ui])
                h = h-25
                
            ui = 0
                
                

            c.showPage()
            c.save()
            print("Reporte Creado Correctamente:")
            print("Ubicacion del Reporte:")
            print("C:\\Users\\milto\\Desktop\\Calificacion\\Proyecto1_201807435\\Proyecto1\\"+name+".pdf")
        else:
            print("El Nombre No Existe")
      elif option_Reports == "3":
          #Help
                print("==========================================================")
                print("||           LENGUAJES FORMALES Y DE PROGRAMACIÓN       ||")
                print("||                       SECCION B-                     ||")
                print("||                       Luis Yela                      ||")
                print("||                           5                          ||")
                print("==========================================================")
                print("")
                input("Presione Enter Para Continuar...")
      else:
          repeater_Reports = False
        

        
        
    elif option == 5:
        #LOAD INPUT FILES
        
        Repeater_Carga = True
        while Repeater_Carga == True:
            os.system("cls")
            print("**************************** CARGAR ARCHIVOS *******************************")
            print("1. Archivos AFD (.afd)")
            print("2. Archivos GRAMATICA (.grm)")
            print("0. Salir")
            option_carga = input()
            if option_carga == "1":
                #Files AFD
                inicial = True
                 
                
                ruta = input("Ingrese la ruta del archivo .afd ")
                fichero = open(ruta,"r")
                t,y = os.path.split(ruta)
                g,f = os.path.splitext(y)
                Name_Carga_AFD= g
                AFDControl.ControladorAFD.newAfd(Name_Carga_AFD)
                
                for line in fichero:
                    State1 = ""
                    State2 = ""
                    Alph = ""
                    A_State1 = ""
                    A_State2 = ""
                    b1 = True
                    b2 = True
                    b3 = True
                    b4 = True
                    for C_A in line.rstrip():
                        if b1 == True:
                            if C_A == ",":
                                b1 = False
                            else:
                                State1 = State1 + C_A
                        elif b2 == True:
                            if C_A == ",":
                                b2 = False
                            else:
                                State2 = State2 + C_A
                        elif b3 == True:
                            if C_A == ";":
                                b3 = False
                            else:
                                Alph = Alph + C_A
                        elif b4 == True:
                            if C_A == ",":
                                b4 = False
                            else:
                                A_State1 = A_State1 + C_A
                        else:
                            A_State2 = A_State2 + C_A
            
                    State1 = State1.upper()
                    State2 = State2.upper()
                    Alph = Alph.lower()
                    A_State1 = A_State1.lower()
                    A_State2 = A_State2.lower()
                    
                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State2)
                    AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,Alph)
                    if inicial == True:
                        AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                        inicial = False
                    estadoinicial = AFDControl.ControladorAFD.returnAfd(Name_Carga_AFD)
                    
                    if A_State1 == "true":
                        AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1)
                        preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,"finish","epsilon")
                        if preg != False:
                            afd_transition = State1+"; ;epsilon"
                            AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,afd_transition)
                    if A_State2 == "true":
                        AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State2)
                        preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State2,"finish","epsilon")
                        if preg !=False:
                            afd_transition = State2+"; ;epsilon"
                            AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,afd_transition)
                    preg= ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,State2,Alph)
                    if preg != False:
                        afd_transition = State1+";" + State2 + ";" + Alph
                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,afd_transition)
                    
                   
                
                input("AFD Creado Correctamente...")
            elif option_carga == "2":
                #Cargar Gramatica
                inicial = True
                 
                
                ruta = input("Ingrese la ruta del archivo .grm ")
                fichero = open(ruta,"r")
                t,y = os.path.split(ruta)
                g,f = os.path.splitext(y)
                Name_Carga_AFD= g
                AFDControl.ControladorAFD.newAfd(Name_Carga_AFD)
                
                for line in fichero:
                    State1 = ""
                    State2 = ""
                    Alph = ""
                    
                    b1 = True
                    b2 = True
                    b3 = True
                    b4 = True
                    for C_A in line.rstrip():
                        if b1 == True:
                            if C_A == " ":
                                b1 = False
                            else:
                                State1 = State1 + C_A
                        elif b2 == True:
                            if C_A == " ":
                                b2 = False
                        elif b3 == True:
                            if C_A == " ":
                                b3 = False
                            else:
                                State2 = State2 + C_A
                        elif b4 == True:
                            if C_A == "|":
                                if State2 == "epsilon":
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)

                                    if inicial == True:
                                        AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                        inicial = False
                                    AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1)
                                    
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,"finish",State2)
                                    if preg != False:
                                        trans = State1 + "; ;"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                else:
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")

                                    if inicial == True:
                                        AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                        inicial = False
                                    
                                    AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,State1+"'",State2)
                                    if preg != False:
                                        trans = State1 + ";"+State1+"';"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                        preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'","finish","epsilon")
                                        if preg1 != False:
                                                trans = State1 + "'; ;epsilon"
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                            
                                b4 = False
                            elif C_A == " ":
                                    State1 = State1.upper()
                                    if Alph.isupper() == True:
                                        AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                        AFDControl.ControladorAFD.NewState(Name_Carga_AFD,Alph)

                                        if inicial == True:
                                            AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                            inicial = False
                                        AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)
                                        preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,Alph,State2)
                                        if preg != False:
                                            trans = State1 + ";"+Alph+";"+State2
                                            AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                        b4 = False
                                    elif State2.isupper() == True:
                                        #Gramatica por la izquiera
                                            
                                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                            if inicial == True:
                                                AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                                inicial = False

                                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State2+"'")
                                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State2+"'")
                                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")
                                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1+"'")
                                            AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,Alph)
                                            preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'",State2+"'",Alph)
                                            if preg != False:
                                                trans = State1 + "';"+State2+"';"+Alph
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                            preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State2+"'","finish","epsilon")
                                            if preg1 != False:
                                                trans = State2 + "'; ;epsilon"
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                            b4 = False

                            else:
                                Alph = Alph + C_A
                        else:
                            if C_A == " ":
                                
                                State2 = ""
                                Alph = ""
                                b3 = True
                                b4 = True


                    if State1 != "" and State2 != "" and Alph != "" and State1 != " " and State2 != " " and Alph != " ":
                        State1 = State1.upper()
                        if Alph.isupper() == True:
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,Alph)

                            if inicial == True:
                                AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                inicial = False
                            AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)
                            preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,Alph,State2)
                            if preg != False:
                                trans = State1 + ";"+Alph+";"+State2
                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)                  
                        elif State2.isupper() == True:
                                        #Gramatica por la izquiera
                                            
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                            if inicial == True:
                                AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                inicial = False

                                            
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State2+"'")
                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State2+"'")
                            AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")
                            AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1+"'")
                            AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,Alph)
                            preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'",State2+"'",Alph)
                            if preg != False:
                                trans = State1 + "';"+State2+"';"+Alph
                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                            preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State2+"'","finish","epsilon")
                            if preg1 != False:
                                trans = State2 + "'; ;epsilon"
                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                    elif State1 != "" and State2 != "" and State1 != " " and State2 != " ":
                        if State2 == "epsilon":
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)

                                    if inicial == True:
                                        AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                        inicial = False
                                    AFDControl.ControladorAFD.AcceptanceState(Name_Carga_AFD,State1)
                                    
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,"finish",State2)
                                    if preg != False:
                                        trans = State1 + "; ;"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                        else:
                                    State1 = State1.upper()
                                    State2 = State2.lower()
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1)
                                    AFDControl.ControladorAFD.NewState(Name_Carga_AFD,State1+"'")
                                    AFDControl.ControladorAFD.NewAlphabet(Name_Carga_AFD,State2)

                                    if inicial == True:
                                        AFDControl.ControladorAFD.InitialState(Name_Carga_AFD,State1)
                                        inicial = False
                                    
                                    preg = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1,State1+"'",State2)
                                    if preg != False:
                                        trans = State1 + ";"+State1+"';"+State2
                                        AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                                        preg1 = ProductionControl.ControladorProduccion.newProduction(Name_Carga_AFD,State1+"'","finish","epsilon")
                                        if preg1 != False:
                                                trans = State1 + "'; ;epsilon"
                                                AFDControl.ControladorAFD.InsertTransition(Name_Carga_AFD,trans)
                input("Elementos Cargados Correctamente, Presiones Enter para continuar...")                          
            else:
                Repeater_Carga = False



    elif option == 6:
        #Guardar 
        Repeater_Save = True
        while Repeater_Save == True:
            os.system("cls")
            print("*********** MENU GUARDAR ***********")
            print("1. Guardar Archivo AFD (.afd)")
            print("2. Guardar Archivo Gramatica (.grm)")
            print("0. Salir")
            option_Save = input()
            if option_Save == "1":
                print("Ingrese el Nombre del AFD: ")
                Name_AFD = input()
                print("Con que Nombre Desea Guardar el Archivo")
                Name_Ruta = input()
                afd_action = AFDControl.ControladorAFD.returnAfd(Name_AFD)
                if afd_action != False:
                    verdadero = "true"
                    falso = "false"
                    fichero = open("C:\\Users\\milto\\Desktop\\Lenguajes\\Proyecto 1\\Proyecto1\\"+Name_Ruta+".afd","w")
                    for y in range(Pproductions.Produccion.Contador):
                        ob = ProductionControl.objeto[y]
                        ob1 = Pproductions.Produccion.Show(ob)
                        if ob1.getNombreGram() == Name_AFD:
                            if ob1.getEstado2() == "finish" or ob1.getTerminal() == "epsilon":
                                pass
                            else:
                                v_s1 = ""
                                v_s2 = ""
                                trys1 = AFDControl.ControladorAFD.TryAcceptanceState(Name_AFD,ob1.getEstado1())
                                trys2 = AFDControl.ControladorAFD.TryAcceptanceState(Name_AFD,ob1.getEstado2())
                                if trys1 == False:
                                    v_s1 = verdadero
                                else:
                                    v_s1 = falso
                                if trys2 == False:
                                    v_s2 = verdadero
                                else:
                                    v_s2 = falso
                                
                                imprimir = ob1.getEstado1()+","+ ob1.getEstado2()+","+ob1.getTerminal()+";"+v_s1+","+v_s2
                                fichero.writelines(imprimir+"\n")

                    fichero.close()
                    input("Creado Correctamente: Presione Enter Para Continuar...")
                else:
                    input("EL AFD no existe: Presione Enter Para Continuar...")
                


            elif option_Save == "2":
                print("Ingrese el Nombre del La Gramatica: ")
                Name_AFD = input()
                print("Con que Nombre Desea Guardar el Archivo")
                Name_Ruta = input()
                fichero = open("C:\\Users\\milto\\Desktop\\Lenguajes\\Proyecto 1\\Proyecto1\\"+Name_Ruta+".grm","w")
                for y in range(Pproductions.Produccion.Contador):
                        ob = ProductionControl.objeto[y]
                        ob1 = Pproductions.Produccion.Show(ob)
                        if ob1.getNombreGram() == Name_AFD:
                            if ob1.getEstado2() == "finish" or ob1.getTerminal() == "epsilon":
                                cae = ob1.getEstado1() + " > "+ob1.getTerminal()
                                fichero.writelines(cae+"\n")
                            else:
                                cae = ob1.getEstado1() + " > "+ob1.getTerminal()+" "+ob1.getEstado2()
                                fichero.writelines(cae+"\n")
                fichero.close()
                input("Creado Correctamente: Presione Enter Para Continuar...")
            else:
                Repeater_Save = False


    elif option == 7:
        #Gramáticas tipo2 y AP
        
        newewpeater = True
        while newewpeater == True:
            os.system('cls')
            

            print("****************Menu de Gramatica Tipo 2 y AP***************************")
            print("1. Ingresar / modificar Gramatica")
            print("2. Generar Automata de Pila y visualizarlo")
            
            print("3. Validar Cadena")
            print("0. Regresar")
            leer_OP7 = input()
            if leer_OP7 == "1":
                #Add or update gramar
                os.system('cls')
                print("Ingrese el nombre de la gramatica")
                namegramar = input()
                AFDControl.ControladorAFD.newAfd(namegramar)
                repeater_Gramar = True
                while repeater_Gramar == True: 
                    os.system('cls')
                    print("*************** Bienvenido Al Menu de "+namegramar + " *****************")
                    print("1. Ingresar Terminales")
                    print("2. Ingresar No Terminales")
                    print("3. Ingresar Producciones")
                    print("4. Borrar Producciones")
                    print("5. No Terminal Inicial")
                    print("0. Regresar")
                    leer_gramar = input()
                    if leer_gramar == "1":
                        #add Terminales
                        os.system("cls")
                        repeater_add_T = True
                        while repeater_add_T == True:
                            name_T = input("Ingrese Un Terminal o la palabra (salir) para salir: ")
                           
                            if name_T == "salir":
                                repeater_add_T = False
                            elif name_T.isupper() == True:
                                print("No Puede Ingresar Terminales Con letras mayusculas")
                                print()
                            else:

                                    tryt_T = AFDControl.ControladorAFD.NewAlphabet(namegramar,name_T)
                                    if tryt_T == False:
                                        print("El Terminal ya ha sido creado anteriormente o pertence a un No Terminal: No Creado ")
                                    else:
                            
                                        print("Terminal Creado Correctamente")
                    elif leer_gramar == "2":
                        #Add No Terminales
                        os.system("cls")
                        repeater_add_NT = True
                        while repeater_add_NT == True:
                            name_NT = input("Ingrese Un No Terminal o el signo mas (+) para salir: ")
                            letrainicial = ""
                            contador_letra = 0
                            
                            if name_NT != "":
                                for le in name_NT:
                                    if contador_letra == 0:
                                        letrainicial = le
                                        contador_letra = contador_letra + 1

                            if name_NT == "+":
                                repeater_add_NT = False
                            elif letrainicial.islower() == True:
                                print("El No Terminal debe iniciar con mayuscula: No Terminal No Guardado")
                                print()
                            else:
                                    tryt_NT = AFDControl.ControladorAFD.NewState(namegramar,name_NT)
                                    if tryt_NT == False:
                                        print("El No Terminal ya ha sido creado anteriormente o pertence a un Terminal: No Creado ")
                                    else:
                                        print("No Terminal Creado Correctamente")
                    elif leer_gramar == "3":
                        #add Productions
                        repeater_reader = True
                        while repeater_reader == True:
                            os.system('cls')
                            print("Ingrese La Prpduccion de la siguiente manera o escriba la palabra (salir) para regresar: ")
                            print("A > α b β")
                            print("A es un no terminal")
                            print("α y β son un conjunto de terminales y no terminales")
                            print("b es un terminal.")
                            Cadena = input()
                            if Cadena == "salir":
                                repeater_reader = False
                            else:
                                isBad = True
                                message = ""
                                al = True
                                al1 = True
                                al2 = True
                                Terminal = ""
                                NT = ""
                                inicial = ""
                                produ = ""
                                for lectura in Cadena:
                                    if al == True:
                                        if lectura == " ":
                                            inicial = Terminal
                                            com12 = AFDControl.ControladorAFD.TryState(namegramar, Terminal)
                                            if com12 == False:
                                                isBad = False;
                                                message = message + " El No Terminal "+Terminal +" No Existe"
                                            al = False
                                        else:
                                            Terminal = Terminal + lectura
                                    elif al1 == True:
                                        if lectura == " ":
                                            al1 = False
                                    else:
                                        if lectura == " ":
                                            
                                            thisj = True;
                                            thisk = True

                                            for this in NT:
                                                if thisj == True:
                                                    thisj = False
                                                    if this.isupper() == True:
                                                        thisk = False
                                            if thisk == False:
                                                
                                                trysta = AFDControl.ControladorAFD.TryState(namegramar,NT)
                                                if trysta == False:
                                                    isBad = False
                                                    message = message + ", El No Terminal ' "+NT+" ' no a sido Creado"
                                            else:
                                                trystat = AFDControl.ControladorAFD.SearchAlphabet(namegramar,NT)
                                                if trystat == True:
                                                    isBad = False
                                                    message = message + ", El Terminal ' "+NT+" ' no a sido Creado"
                                            produ = produ + NT + " "
                                            NT = ""
                                                    
                                                        

                                        else:
                                            NT = NT + lectura
                                thisj = True;
                                thisk = True

                                for this in NT:
                                                if thisj == True:
                                                    thisj = False
                                                    if this.isupper() == True:
                                                        thisk = False
                                if thisk == False:
                                                
                                                trysta = AFDControl.ControladorAFD.TryState(namegramar,NT)
                                                if trysta == False:
                                                    isBad = False
                                                    message = message + ", El No Terminal ' "+NT+" ' no a sido Creado"
                                else:
                                                trystat = AFDControl.ControladorAFD.SearchAlphabet(namegramar,NT)
                                                ProductionC.ControladorProduccion.Insertar_Aceptacion(namegramar,Cadena,NT)
                                                
                                                if trystat == True:
                                                    isBad = False
                                                    message = message + ", El Terminal ' "+NT+" ' no a sido Creado"
                                produ = produ + NT + " "

                                if isBad == True:
                                    #Lo Guarda
                                    
                                    prob= ProductionC.ControladorProduccion.newProduction(namegramar,Cadena)
                                    if prob == False:
                                        exitnew =input("La Produccion Ya Existe, Presione enter para continuar o el signo mas (+) para salir.... ")
                                        if exitnew == "+":
                                            repeater_reader = False
                                    else:
                                        ProductionC.ControladorProduccion.Insertar_inicial(namegramar,Cadena,inicial,produ)
                                        
                                        print("Cadena: "+Cadena)
                                        print(inicial)
                                        print(produ)
                                        
                                        exitnew =input("Guardado Correctamente, Presione enter para continuar o el signo mas (+) para salir.... ")
                                        if exitnew == "+":
                                             repeater_reader = False

                                else:
                               
                                    exitnew =input(message+", Produccion No Guardada,  Presione enter para continuar o el signo mas (+) para salir....")
                                    if exitnew == "+":
                                        repeater_reader = False

                    elif leer_gramar == "4":
                        #Delete Productions
                        repeater_Delete = True
                        while repeater_Delete == True:
                            os.system('cls')
                            print("Ingrese la Produccion de la siguiente manera para eliminar o la palabra (salir) para regresar")
                            print("A > α β")
                            print("Donde:")
                            print("A es un no terminal")
                            print("α, β son un conjunto de terminales y no terminales")
                            leer_eliminar = input()
                            if leer_eliminar == "salir":
                                repeater_Delete = False
                            else:
                                delete = ProductionC.ControladorProduccion.Eliminar(namegramar,leer_eliminar)
                                if delete == True:
                                    input("Produccion Eliminada Correctamente, Presione enter para continuar")
                                else:
                                    input("La Produccion No existe, Presione enter para Continuar")

                    elif leer_gramar == "5":
                        #Initial State
                        os.system("cls")
                        print("Ingrese un No Terminal inicial: ")
                        initialstate1 = input()
                        initialstate1 = initialstate1.upper()
                        tryinitial1 = AFDControl.ControladorAFD.InitialState(namegramar,initialstate1)
                        if tryinitial1 == True:
                            input("El No Terminal Inicial Creado Correctamente, Presione Enter para continuar: ")
                        else:
                            input("El No Terminal que desea nombrar como inicial no existe, Error: Presione Enter para continuar")
                    else:
                        #Exit
                        repeater_Gramar = False

            elif leer_OP7 == "2":
                #Genera
                os.system("cls")
                Name_evaluate = input("Ingrese El Nombre de la Gramatica")
                check = AFDControl.ControladorAFD.SearchAfd(Name_evaluate)
                if check == True:
                    fx = Digraph(format='png', name= Name_evaluate)
                    fx.attr(rankdir='LR', size='8,5')
                    print("Automata de Pila de: "+Name_evaluate)
                    print("S: {i, P, q, F}")
                    fx.attr('node', shape='circle')
                    fx.node("i")
                    fx.attr('node', shape='circle')
                    fx.node("p")
                    fx.attr('node', shape='circle')
                    fx.node("q")
                    fx.attr('node', shape='doublecircle')
                    fx.node("f")
                    print("Σ: {"+AFDControl.ControladorAFD.NoTerminales(Name_evaluate)+"}")
                    print("Γ: {"+AFDControl.ControladorAFD.NoTerminales(Name_evaluate)+","+AFDControl.ControladorAFD.Terminales(Name_evaluate)+",#}")
                    print("L: i")
                    print("F: F")
                    print("T:")
                    print("   i, λ, λ; p, #")
                    fx.edge("i", "p", "λ,λ;#")
                    alome = AFDControl.ControladorAFD.returnAfd(Name_evaluate)
                    de = "   p, λ, λ; q, "+alome.getEstadoInicial()
                    fx.edge("p", "q", "λ,λ;"+alome.getEstadoInicial())
                    for i in range(ProductionO.Production.Contador):
                        
                        productions = ProductionO.Production.Show(ProductionC.objeto[i])
                        
                        if productions.getNombreGram() == Name_evaluate:
                            
                            print("   q, λ, "+productions.getEstadoInicial()+"; q, "+productions.getPrducciones())
                            
                            fx.edge("q", "q", "λ,"+productions.getEstadoInicial()+";"+productions.getPrducciones())
                        po = ""
                        pol = True
                    for k in AFDControl.ControladorAFD.NoTerminales(Name_evaluate):
                            if pol == True:
                                if k == ",":
                                    pol = False
                            else:
                                if k == ",":
                                    print("   q, "+po+", "+po+"; q, λ")
                                    fx.edge("q", "q", po+","+po+";λ")
                                    po = ""
                                else:
                                    po = po+k
                    print("   q, λ, #; f, λ")
                    fx.edge("q", "f", "λ,#;λ")
                    fx.attr('node', shape='none')
                    fx.attr('edge', arrowhead='empty', arrowsize='1.5')
                    fx.edge('', 'i', None)
                    fx.render()
                    input("Presione Enter para Regresar....")
                else:
                    input("El Nombre de la Gramatica no existe Presiones Enter Para Regresar....")
            
            elif leer_OP7 == "3":
                #Value Chains
                os.system("cls")
                Name_evaluate = input("Ingrese El Nombre de la Gramatica")
                check = AFDControl.ControladorAFD.SearchAfd(Name_evaluate)
                if check == True:
            
                    repeater_evaluate = True
                    Cadena_En_Curso = ""
                    while repeater_evaluate == True:
                        os.system("cls")
                        
                        print("*********************** Menu VAlidar Cadenas ***********************")
                        print("1. Ingresar Cadena")
                        print("2. Resultado")
                        print("3. Reporte")
                        print("0. Salir")
                        leer_validar = input()
                        if leer_validar == "1":
                            #Add Chain
                            print("Ingrese la Cadena a evaluar:")
                            cha = input()
                            r = AFDControl.ControladorAFD.InsertCadena(Name_evaluate,cha)
                            if r == True:
                                print("Guardado Correctamente")
                            else:
                                print("LA CAdena ya a sido valuada anteriormente")
                            Cadena_En_Curso = cha
                            input()
                        elif leer_validar == "2":
                            #Result
                            

                            retorno = ProductionC.ControladorProduccion.MethodValidar(Name_evaluate,Cadena_En_Curso+"#")
                            if retorno == "":
                                input("Invalida")
                            else:
                                input("La cadena es: "+retorno)
                        elif leer_validar == "3":
                            #Report
                            pass
                        else:
                            repeater_evaluate = False
            
            else:
                newewpeater = False
    elif option == 11:
        art = input("Ingresar: ")
        print(art[0])
        input()
    elif option == 0:
        #EXIT
        Repeater = False

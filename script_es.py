#!/usr/bin/python
# -*- coding: utf-8 -*-
#creditos: BorjaLizbeth,ParedesByron,FalconiLuis,VallePaul
import os
import random

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("¿QUÉ DATOS DESEA GENERAR?")
	print ("\t1 WINDOWS")
	print ("\t2 LINUX  ")
	print ("\t3 SALIR")

while True:
        print ("---------------------------BIENVENIDO!---------------------")
        print ("GENERADOR DATOS PARA INSERTAR EN ELASTICSEARCH")
        print ("1. GENERAR ARCHIVO")
        print ("2. SALIR DEL PROGRAMA")
        print ("")
        opc = input("inserta una opción >> ")

        if opc=="1":
                nomf = input("ingresa un nombre para el documento >> ")
                file = open(nomf+'.txt', "w")
                os.system("cls")
                menu()
                """
                Informacion que se va a utilizar
                """
                opcion = input("inserta una opción >> ")
                names = ['Sam', 'Paul', 'Mark', 'Byron', 'Sean', 'Lizbeth', 'Jhofre', 'Luis', 'David', 'Ivan', 'Daniela', 'Daraliz', 'Cristian', 'Carolina', 'Jose']
                apellidos = ['Valle', 'Paredes', 'Borja', 'Falconi', 'Rodriguez', 'Duran', 'Castellano', 'Navarro', 'Aguilar', 'Barrera', 'Bonilla', 'Cardona', 'Escalona', 'Escobar', 'Monreal']
                ci = 0
                id = 1
                
                cadena = 'curl -XPUT -H "Content-Type: application/json" localhost:9200/datos/datos/'
                cadenaLx = "curl -XPUT -H 'Content-Type: application/json;' 'localhost:9200/datos/datos/"
                cadenaf=''

                if opcion=="1":
                        print ("NÚMERO DE DATOS QUE DESEA GENERAR")
                        opcion=input("ingrese el número a generar: ")
                        os.system("cls")
                        num = int(opcion)
                        file.write('---------DATOS GENERADOS PARA WINDOWS---------\n')
                        while num > 0:
                                ci = random.randint(1111111111, 2499999999)
                                cadenaf = cadena+str(id)+' -d "' +'{\\"type\\":\\"mongodb\\", \\"mongodb\\":{\\"db\\":\\"elastic\\", \\"collection\\":\\"elastic\\"}, \\"index\\":{\\"id\\":\\"'+str(id) + '\\", \\"nombre\\":\\"'+ random.choice(names)+'\\", \\"apellido\\":\\"'+ random.choice(apellidos)+ '\\", \\"ci\\":\\"'+str(ci)+'\\"}}"'
                                file.write(cadenaf+'\n')
                                """print (cadenaf)"""
                                id = id + 1
                                num = num -1
                        file.close()
                        print ("----------DATOS INGRESADOS----------")
                        print ("")
                        print ("Nombre del documento: "+nomf+".txt")
                        print ("Sistema Operativo: Windows")
                        print ("Número de datos: "+opcion)
                        print ("")
                        
                elif opcion=="2":
                        print ("NÚMERO DE DATOS QUE DESEA GENERAR")
                        opcion=input("ingrese el número a generar: ")
                        os.system("clear")
                        num = int(opcion)
                        file.write('----------DATOS GENERADOS PARA LINUX--------\n')
                        while num > 0:
                                ci = random.randint(1111111111, 2499999999)
                                cadenaf = cadenaLx+str(id)+"' -d '" +'{"id":"'+str(id) + '", "nombre":"'+ random.choice(names)+'", "apellido":"'+ random.choice(apellidos)+ '", "ci":"'+str(ci)+'"}'+"'"
                                file.write(cadenaf+'\n')
                                """print (cadenaf)"""
                                id = id + 1
                                num = num -1
                        file.close()
                        print ("----------DATOS INGRESADOS----------")
                        print ("")
                        print ("Nombre del documento: "+nomf+".txt")
                        print ("Sistema Operativo: Linux")
                        print ("Número de datos: "+opcion)
                        print ("")
                        
                elif opcion=="3":
                        break
                else:
                        print ("")
                        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        elif opc=="2":
                break
        else:
                        print ("")
                        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

                

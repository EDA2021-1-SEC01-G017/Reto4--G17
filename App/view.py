﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import time
import config as cf
import sys
import threading
import controller
from DISClib.ADT import list as lt
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import stack
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


airportfile = 'Skylines//airports_full.csv'
routefile = 'Skylines//routes_full.csv'
citiesfile = 'Skylines//worldcities.csv'
initialStation = None


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de VUELOS")
    print("3- REQ1- ")
    print("4- REQ2-")
    print("5- REQ3-")
    print("6- REQ4-")
    print("7- REQ5-")
    print("8- REQ6BONO-Visualizar avistamientos en una zona geográfica /--Long(Limite máx y min) Lat(Límite máx y min)--/")
    print("0- Salir")
    print("*******************************************")

analyzer = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        
        analyzer = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos....")
        controller.loadData(analyzer, airportfile, routefile, citiesfile) 
        print("En el primer grafo hay un total de " + str(gr.numVertices[analyzer["vuelos"]]) + "aeropuertos.")
        print("En el segundo grafo hay un total de " + str(gr.numVertices[analyzer["doubleRoutes"]]) + " aeropuertos.")
        print("Existen " + str(m.size(analyzer["cityInfo"])) + " ciudades en el archivo.")
        lista_iatas = m.keySet(analyzer["iataInfo"])
        primer_iata = lt.firstElement(lista_iatas)
        pareja_ini = m.get(analyzer["iataInfo"], primer_iata)
        info_list = me.getValue(pareja_ini)
        first_ap_str = ""
        for elemento in lt.iterator(info_list):
            first_ap_str += elemento
            first_ap_str += ", "
        
        print("La información del primer aeropuerto cargado es: " + first_ap_str)

        lista_ciudades = m.keySet(analyzer["cityInfo"])
        ultima_ciudad = lt.lastElement(lista_ciudades)
        pareja_ini2 = m.get(analyzer["cityInfo"], ultima_ciudad)
        info_list2 = me.getValue(pareja_ini2)
        final_city_str = ""
        for elemento2 in lt.iterator(info_list2):
            final_city_str += elemento2
            final_city_str += ", "

        print("La información de la última ciudad cargada primer aeropuerto cargado es: " + final_city_str)

        
    

    
    #EJEMPLO PARA ACOMODAR CADA REQ
    #elif int(inputs[0]) == 3:
        #TITULO DEL REQ
        #print("\nREQ1-Buscando OVNIS en una ciudad: ")
        #INPUTS REQUERIDOS
        #City = input("Ingrese la ciudad: ")
        #USO DE FUNCIÓN
        #total = getOvnisInCity(archive, City)
        #IMPRESIÓN DE RESULTADOS
        #print(total)
        #print("Altura del arbol: " + str(om.height(archive['DateIndex'])))
        #print('Elementos en el arbol: ' + str(om.size(archive['DateIndex'])))

    elif int(inputs[0]) == 4:
        pass

    else:
        sys.exit(0)
sys.exit(0)

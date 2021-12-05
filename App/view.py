"""
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
from tabulate import tabulate
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


airportfile = 'Skylines//airports-utf8-small.csv'
routefile = 'Skylines//routes-utf8-small.csv'
citiesfile = 'Skylines//worldcities-utf8.csv'
initialStation = None

# ___________________________________________________
#  Funciones
# ___________________________________________________

def graph_info(analyzer):
    #First Table
    num1 = gr.numVertices(analyzer["vuelos"])
    num2 = gr.numEdges(analyzer["vuelos"])

    print("=== Airports-Routes DiGraph ===")
    print("Nodes: " + str(num1))
    print("Edges: " + str(num2))
    print("First & Last Airport loaded in the Digraph." + "\n")
    
    lista_iatas = m.keySet(analyzer["iataInfo"])
    primer_iata = lt.firstElement(lista_iatas)
    pareja_inicial1 = m.get(analyzer["iataInfo"], primer_iata)

    a = gr.vertices(analyzer["vuelos"])
    tList = []
    for i in lt.iterator(a):
        tList.append(i)
    info_list1 = me.getValue(pareja_inicial1)

    first_ap_list = []
    for elemento in lt.iterator(info_list1):
        first_ap_list.append(str(elemento))

    ultimo_iata = lt.lastElement(lista_iatas)
    pareja_final1 = m.get(analyzer["iataInfo"], ultimo_iata)
    info_list2 = me.getValue(pareja_final1)
    last_ap_list = []
    for elemento in lt.iterator(info_list2):
        last_ap_list.append(str(elemento))
    
    table1 =[first_ap_list, last_ap_list]
    headliners1 = ["Name", "City", "Country", "Longitude", "Latitude"]
    print(tabulate(table1, headers=headliners1, tablefmt="grid") + "\n")
    
    #Second Table
    num3 = gr.numVertices(analyzer["doubleRoutes"])
    num4 = gr.numEdges(analyzer["doubleRoutes"])

    print("=== Airports-Routes Graph ===")
    print("Nodes: " + str(num3))
    print("Edges: " + str(num4))
    print("First & Last Airport loaded in the Graph." + "\n")

    
    #Third Table
    num5 = m.size(analyzer["cityInfo"])

    print("=== City Network ===")
    print("The number of cities are: " + str(num5))
    print("First & Last City loaded in data structure.")

    lista_ciudades = m.keySet(analyzer["cityInfo"])
    primera_ciudad = lt.firstElement(lista_ciudades)
    pareja_ini2 = m.get(analyzer["cityInfo"], primera_ciudad)
    info_list3 = me.getValue(pareja_ini2)
    chainList1 = primera_ciudad.split('-')
    first_city_list = [chainList1[0]]
    for elemento2 in lt.iterator(info_list3):
        first_city_list.append(elemento2)

    ultima_ciudad = lt.lastElement(lista_ciudades)
    pareja_final2 = m.get(analyzer["cityInfo"], ultima_ciudad)
    info_list4 = me.getValue(pareja_final2)
    chainList2 = ultima_ciudad.split('-')
    final_city_list = [chainList2[0]]
    for elemento2 in lt.iterator(info_list4):
        final_city_list.append(elemento2)

    table3 = [first_city_list, final_city_list]
    headliners3 = ["city", "country", "population", "latitude", "longitude", "id"]
    print(tabulate(table3, headers=headliners3, tablefmt="grid") + "\n")

def interconection(analyzer):
    answer = controller.interconection(analyzer)
    org = sorted(answer, key=lambda x:x[4], reverse=True)
    table5 = org[:5]
    headliners = ["Name", "City", "Country", "IATA", "connections", "inbound", "outbound"]
    print("Connected airports inside network: " + str(len(org)) + "\n")
    print("TOP 5 most connected airports..." + "\n")
    print(tabulate(table5, headers=headliners, tablefmt="grid") + "\n")
     
def clusteres (analyzer, iataAp1, iataAp2):
    answer = controller.clusteres(analyzer, iataAp1, iataAp2)
    number = answer[0]
    chain = answer[1]
    if chain == False:
        cond = " not "
    else:
        cond = ""
    print("The total number of clusters present in the network is: " + number)
    print("The two airports identified with the IATAS: " + iataAp1 + " & " + iataAp2 + " are " + cond + " located on the same cluster." + "\n")

def shortestRoute (analyzer, origin, destiny):
    answer = controller.shortestRoute(analyzer, origin, destiny)



def travelerMiles (analyzer, origin, miles):
    answer = controller.travelerMiles(analyzer, origin, miles)

def closedEffect (analyzer, closedIata):
    answer = controller.closedEffect(analyzer, closedIata)

def compareWeb (analyzer, origin, destiny):
    answer = controller.compareWeb(analyzer, origin, destiny)

def graphVis ():
    answer = controller.graphVis()

def chooseCity (analyzer, city):
    answer = controller.chooseCity(analyzer, city)
    correctLine = 0
    headliners = ["Option Number", "city", "country", "population", "lat", "lng", "id"] 
    if len(answer) > 1:
        print(tabulate(answer, headers=headliners, tablefmt="pretty") + "\n")
        correctLine = int(input("Type the option number of the city you would like to choose: "))-1
    chosenCity = answer[correctLine][1] + "-" + str(answer[correctLine][-1])
    return chosenCity

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
        print("\nLoading flies routes....\n\n")
        controller.loadData(analyzer, airportfile, routefile, citiesfile) 
        graph_info(analyzer)
        
    elif int(inputs[0]) == 3:
        print(interconection(analyzer))
           
    elif int(inputs[0]) == 4:
        iataAp1 = input("Enter the IATA code of the first airport: ").upper()
        iataAp2 = input("Enter the IATA code of the second airport: ").upper()
        print(clusteres(analyzer, iataAp1, iataAp2))
        
    elif int(inputs[0]) == 5:
        origin = input("Enter the name of the departure city: ").upper()
        c_origin = chooseCity(analyzer, origin)
        destiny = input("Enter the name of the destination city: ").upper()
        c_destiny = chooseCity(analyzer, destiny)
        print(shortestRoute(analyzer, c_origin, c_destiny))        

    elif int(inputs[0]) == 6:
        origin = input("Enter the name of the departure city: ").upper()
        miles = int(input("Enter the number of miles that the passenger has: "))
        c_origin = chooseCity(analyzer, origin)
        print(travelerMiles(analyzer, c_origin, miles))

    elif int(inputs[0]) == 7:
        closedIata = input("Enter the IATA code of the airport that isn't available: ")
        print(closedEffect(analyzer, closedIata))

    elif int(inputs[0]) == 8:
        origin = input("Enter the name of the departure city: ").upper()
        c_origin = chooseCity(analyzer, origin)
        destiny = input("Enter the name of the destination city: ").upper()
        c_destiny = chooseCity(analyzer, destiny)
        print(compareWeb(analyzer, c_origin, c_destiny))

    elif int(inputs[0]) == 9:
        print(graphVis())

    else:
        sys.exit(0)
sys.exit(0)

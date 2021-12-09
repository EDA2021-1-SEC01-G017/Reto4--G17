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

from timeit import default_timer
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


airportfile = 'Skylines//airports-utf8-large.csv'
routefile = 'Skylines//routes-utf8-large.csv'
citiesfile = 'Skylines//worldcities-utf8.csv'

sys.setrecursionlimit(1048576)
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
    for elemento2 in lt.iterator(info_list2):
        last_ap_list.append(str(elemento2))
    
    table1 =[first_ap_list, last_ap_list]
    headliners1 = ["Name", "City", "Country", "Longitude", "Latitude"]
    print(tabulate(table1, headers=headliners1, tablefmt="grid") + "\n")
    
    #Second Table
    num3 = gr.numVertices(analyzer["doubleRoutes"])
    num4 = int(gr.numEdges(analyzer["doubleRoutes"])/2)

    print("=== Airports-Routes Graph ===")
    print("Nodes: " + str(num1))
    print("Edges: " + str(num4))
    print("First & Last Airport loaded in the Graph." + "\n")

    first_iata = lt.firstElement(analyzer["doubleList"])
    first_pair = m.get(analyzer["iataInfo"], first_iata)
    first_value = me.getValue(first_pair)

    f_i_l = []
    for elemento3 in lt.iterator(first_value):
        f_i_l.append(elemento3)

    last_iata = lt.lastElement(analyzer["doubleList"])
    last_pair = m.get(analyzer["iataInfo"], last_iata)
    last_value = me.getValue(last_pair)

    l_i_l = []
    for elemento4 in lt.iterator(last_value):
        l_i_l.append(elemento4)

    table2 = [f_i_l, l_i_l]
    headliners2 = ["Name", "City", "Country", "Longitude", "Latitude"]
    print(tabulate(table2, headers=headliners2, tablefmt="grid") + "\n")
    
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
    org = sorted(answer, key=lambda ans:ans[4], reverse=True)
    table5 = org[:5]
    headliners = ["Name", "City", "Country", "IATA", "connections", "inbound", "outbound"]
    print("\n=== Req No. 1 Answer ===")
    print("Connected airports inside network: " + str(len(org)))
    print("TOP 5 most connected airports..." + "\n")
    print(tabulate(table5, headers=headliners, tablefmt="grid") + "\n")
  
def clusteres (analyzer, iataAp1, iataAp2):
    
    answer = controller.clusteres(analyzer, iataAp1, iataAp2)
    components = answer[0]
    connection = answer[1]
    ap1 = m.get(analyzer["iataInfo"], iataAp1)
    val1 = me.getValue(ap1)
    a_1_L = [iataAp1]
    i = 0
    for el1 in lt.iterator(val1):
        if i < 3:
            a_1_L.append(el1)
        i += 1
    ap2 = m.get(analyzer["iataInfo"], iataAp2)
    val2 = me.getValue(ap2)
    a_2_L = [iataAp2]
    j = 0
    for el2 in lt.iterator(val2):
        if j < 3:
            a_2_L.append(el2)
        j += 1
    table = [a_1_L, a_2_L]

    headliners = ["IATA", "Name", "City", "Country"]

    print("=== Req No. 2 Answer ===")
    print(tabulate(table, headers=headliners, tablefmt="grid") + "\n")
    print("- Number of SCC in Airport-Route network: " + str(components))
    print("- Does the " + a_1_L[1] + " and the " + a_2_L[1] + " belong together?")
    print("- ANS:" + str(connection) + "\n")

def shortestRoute (analyzer, origin, destiny):
    
    answer = controller.shortestRoute(analyzer, origin, destiny)
    table1 = answer[0]
    table2 = answer[1]
    tDistance = 0
    for flight in table1:
        tDistance += float(flight[2])

    headliners1 = ["Departure", "Destination", "distance_km"]
    headliners2 = ["IATA", "Latitude", "Longitude"]
    print("=== Req No. 3 ===")
    print("- Total distance: " + str(round(tDistance, 2)) + " (km)")
    print("- Trip Path:")
    print(tabulate(table1, headers=headliners1, tablefmt="grid"))
    print("- Trip Stops:")
    print(tabulate(table2, headers=headliners2, tablefmt="grid") + "\n")

def travelerMiles (analyzer, miles):
    
    answer = controller.travelerMiles(analyzer, miles)
    table1 = answer[0]
    table1f = [table1[0], table1[1], table1[2], table1[-3], table1[-2], table1[-1]]
    table2 = answer[1]
    table2f = [table2[0], table2[1], table2[2], table2[-3], table2[-2], table2[-1]]
    
    avKilo = float(miles) * 1.6
    numAp = len(table1)
    print("=== Req No. 4 Answer ===\n")
    headliners1 = ["IATA", "Name", "City", "Country"]
    print("These are the first and last 3 airports available: ")
    print(tabulate(table1f, headers=headliners1, tablefmt="grid") + "\n")

    print("- Possible airports information: ")
    print("- Number of possible airports: " + str(numAp) + ".")
    print("- Passenger available travelling miles: " + str(avKilo) + " (km).\n")

    headliners2 = ["Departure", "Destination", "distance_km"]
    print("- These are the first and last 3 of the possible path details:")
    print(tabulate(table2f, headers=headliners2, tablefmt="grid") + "\n")
    print("\n")

def closedEffect (analyzer, closedIata):
    
    answer = controller.closedEffect(analyzer, closedIata)
    todos = answer[0]
    table = [todos[0], todos[1], todos[2], todos[-3], todos[-2], todos[-1]]

    num1 = answer[1][0]
    num2 = answer[1][1]
    num3 = answer[1][2]
    num4 = (answer[1][3])/2

    num5 = answer[2][0]
    num6 = answer[2][1]
    num7 = answer[2][2]
    num8 = answer[2][3]
    
    numAffected = answer[3]
    
    headliners = ["IATA", "Name", "City", "Country"]

    print("--- Airports-Routes Digraph ---")
    print("Original number of Airports: " + str(num1) + " and Routes: " + str(num2))
    print("--- Airports-Routes Graph ---")
    print("Original number of Airports: " + str(num3) + " and Routes: " + str(int(num4)) + "\n")
    
    print("+++ Removing Airport with IATA: " + closedIata + " +++\n")

    print("--- Airports-Routes Digraph ---")
    print("Resulting number of Airports: " + str(num1-num5) + " and Routes: " + str(int(num2-num6)))
    print("--- Airports-Routes Graph ---")
    print("Resulting number of Airports: " + str(num1-num7) + " and Routes: " + str(int(num4-num8)) + "\n")

    print("There are " + str(numAffected) + " Airports affected by the removal of " + closedIata)
    print("The first & last 3 Airports affected are:")
    print(tabulate(table, headers=headliners, tablefmt="grid"))

def compareWeb ():
    answer = controller.compareWeb()
    print("This option is not available at this moment...")

def graphVis ():
    answer = controller.graphVis()
    print("This option is not available at this moment...")

def chooseCity (analyzer, city):
    answer = controller.chooseCity(analyzer, city)
    correctLine = 0
    headliners = ["Option Number", "city", "country", "population", "lat", "lng", "id"] 
    if len(answer) > 1:
        print(tabulate(answer, headers=headliners, tablefmt="grid") + "\n")
        correctLine = int(input("Type the option number of the city you would like to choose: "))-1
    chosenCity = answer[correctLine][1] + "-" + str(answer[correctLine][-1])
    return chosenCity

def shortestAirport (analyzer, city):
    answer = controller.shortestAirport(analyzer, city)
    return answer
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Initialize and Load Analyzer")
    print("2- REQ1 - Interconnection")
    print("3- REQ2 - Clusters")
    print("4- REQ3 - Shortest Route")
    print("5- REQ4 - Miles")
    print("6- REQ5 - Closed Airport")
    print("7- REQ6 - Compare Web")
    print("8- REQ7 - Visualize")
    print("0- Exit")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('To continue, please select an option: \n')
    if int(inputs[0]) == 1:
        inicio1 = default_timer()
        print("\nInicializando....")
        analyzer = controller.init()
        controller.loadData(analyzer, airportfile, routefile, citiesfile) 
        graph_info(analyzer)
        fin1 = default_timer()
        tiempo1 = fin1-inicio1
        print("TIEMPO: " + str(tiempo1))

    elif int(inputs[0]) == 2:
        inicio2 = default_timer()
        print("\nLoading flies routes....\n\n")
        print(interconection(analyzer))
        fin2 = default_timer()
        tiempo2 = fin2-inicio2
        print("TIME: " + str(tiempo2))
        
    elif int(inputs[0]) == 3:
        
        iataAp1 = input("Enter the IATA code of the first airport: ").upper()
        iataAp2 = input("Enter the IATA code of the second airport: ").upper()
        inicio3 = default_timer()
        print(clusteres(analyzer, iataAp1, iataAp2))
        fin3 = default_timer()
        tiempo3 = fin3-inicio3
        print("TIME: " + str(tiempo3))
           
    elif int(inputs[0]) == 4:
        origin = input("Enter the name of the departure city: ").upper()
        c_origin = chooseCity(analyzer, origin)
        destiny = input("Enter the name of the destination city: ").upper()
        c_destiny = chooseCity(analyzer, destiny)
        inicio4 = default_timer()
        ap1 = shortestAirport(analyzer, c_origin)
        source = ap1[0]
        ap2 = shortestAirport(analyzer, c_destiny)
        vertex = ap2[0]
        print(shortestRoute(analyzer, source, vertex)) 
        fin4 = default_timer()
        tiempo4 = fin4-inicio4
        print("TIME: " + str(tiempo4))

    elif int(inputs[0]) == 5:
        miles = int(input("Enter the number of miles that the passenger has: "))
        inicio6 = default_timer()
        print(travelerMiles(analyzer, miles))
        fin6 = default_timer()
        tiempo6 = fin6-inicio6
        print("TIME: " + str(tiempo6))

    elif int(inputs[0]) == 6:
        closedIata = input("Closing the airport with IATA code: ").upper()
        inicio5 = default_timer()
        print(closedEffect(analyzer, closedIata))
        fin5 = default_timer()
        tiempo5 = fin5-inicio5
        print("TIME: " + str(tiempo5))

    elif int(inputs[0]) == 7:
        print(compareWeb())

    elif int(inputs[0]) == 8:
        print(graphVis())

    else:
        sys.exit(0)
sys.exit(0)

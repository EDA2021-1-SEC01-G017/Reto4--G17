"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """



import config 

from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error

assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------


def newAnalyzer():
    """ 
    Inicializa el analizador

   stops: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
                    'iataInfo': None,
                    'distances': None,
                    'routeMap': None,
                    'cityInfo': None,
                    'vuelos': None,
                    'doubleRoutes': None,
                    'existCheck': None
                    }
        
        
        analyzer['iataInfo'] = m.newMap(numelements=20000,
                                     maptype='PROBING',
                                     loadfactor=0.5
                                     )

        analyzer['distances'] = m.newMap(numelements=20000,
                                     maptype='PROBING',
                                     loadfactor=0.5
                                     )
        
        analyzer['routeMap'] = m.newMap(numelements=20000,
                                     maptype = 'PROBING',
                                     loadfactor = 0.5
                                     )

        analyzer["cityInfo"] = m.newMap(numelements=20000,
                                     maptype = 'PROBING',
                                     loadfactor = 0.5
                                     )

        analyzer['vuelos'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=2075,
                                              comparefunction=compareroutes
                                              )
                                     
        analyzer["doubleRoutes"] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=20000,
                                              comparefunction=compareroutes
                                              )
        
        analyzer["existCheck"] = lt.newList(datastructure="SINGLE_LINKED")
        
        

        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# Funciones para agregar informacion al grafo

def add_info (analyzer, airport):

    intlist0 = lt.newList()

    lt.addLast(intlist0, airport["Name"].upper())
    lt.addLast(intlist0, airport["City"].upper())
    lt.addLast(intlist0, airport["Country"].upper())
    lt.addLast(intlist0, float(airport["Longitude"]))
    lt.addLast(intlist0, float(airport["Latitude"]))

    m.put(analyzer["iataInfo"], airport["IATA"], intlist0)

    intlist1 = lt.newList()
    m.put(analyzer["routeMap"], airport["IATA"], intlist1)

    gr.insertVertex(analyzer["vuelos"], airport["IATA"])

def add_edge (analyzer, route):
    NoneType = type(None)

    b1= route["Departure"].upper()
    b2= route["Destination"].upper()
    b3= float(route["distance_km"])


    c = True
    if  type(b1) == NoneType or  type(b2) == NoneType or type(b3) == NoneType:
        c = False
    
    lt.addLast(analyzer["existCheck"], c)

    gr.addEdge(analyzer["vuelos"], b1, b2, b3)

    #pair = m.get(analyzer["routeMap"], route["Departure"])
    #value = me.getValue(pair)

    #if lt.isPresent(value, route["Destination"]) == 0:
    #    lt.addLast(value, route["Destination"])

    #joinKey = route["Departure"] + "-" + route["Destination"]
    #m.put(analyzer["distances"], joinKey, route["distance_km"])
    

def add_city (analyzer, city):
    joinKey = city["city_ascii"] + "-" + city["capital"]
    infoList = lt.newList()
    lt.addLast(infoList, int(city["population"]))
    lt.addLast(infoList, float(city["lat"]))
    lt.addLast(infoList, float(city["lng"]))
    m.put(analyzer["cityInfo"], joinKey, infoList)
    
def double_check(analyzer):
    iataList = m.keySet(analyzer["iataInfo"])

    for dep in lt.iterator(iataList):

        pair1 = m.get(analyzer["routeMap"], dep)

        value1 = me.getValue(pair1)

        for des in lt.iterator(value1): 

            pair2 = m.get(analyzer["routeMap"], des)

            value2 = me.getValue(pair2)

            if lt.isPresent(value2, dep) != 0:
                if gr.containsVertex(analyzer["doubleRoutes"], dep) == False:
                    gr.insertVertex(analyzer["doubleRoutes"], dep)
                if gr.containsVertex(analyzer["doubleRoutes"], des) == False:
                    gr.insertVertex(analyzer["doubleRoutes"], des)

                join_key = dep + "-" + des
                distance_pair = m.get(analyzer["distances"], join_key)
                distance_val = me.getValue(distance_pair)

                gr.addEdge(analyzer["doubleRoutes"], dep, des, distance_val)

                pos_del1 = lt.isPresent(value1, des)
                pos_del2 = lt.isPresent(value2, dep)

                lt.deleteElement(value1, pos_del1)
                lt.deleteElement(value2, pos_del2)
    
def interconection (analyzer):
    iataList = m.keySet(analyzer["iataInfo"])
    table = []
    for iata in lt.iterator(iataList):
        numVertex = gr.adjacents(analyzer["vuelos"], iata)
        line = []
        path = m.get(analyzer["iataInfo"], iata)
        values = me.getValue(path)
        nombre = lt.getElement(values, 1)
        ciudad = lt.getElement(values, 2)
        pais = lt.getElement(values, 3)
        line.append(iata) 
        line.append(nombre) 
        line.append(ciudad) 
        line.append(pais)
        line.append(str(numVertex))
        table.append(line)
    return table

def clusteres (analyzer, iataAp1, iataAp2):
    
    pass

def shortestRoute (analyzer, origin, destiny):
    pass

def travelerMiles (analyzer, origin, miles):
    pass

def closedEffect (analyzer, closedIata):
    pass

def compareWeb (analyzer, origin, destiny):
    pass

def graphVis ():
    pass

        





    




    


    


# Funciones para creacion de datos PROBABLEMENTE NO SE USE

# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion

def compareroutes(route1, route2):
    """
    Compara dos rutas
    """
    if (route1 == route2):
        return 0
    else:
        return 1

# ==============================


# Funciones de ordenamiento PROBABLEMENTE NO SE USE


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
                    'names': None,
                    'iatas': None,
                    'vuelos': None,
                    }

        analyzer['names'] = m.newMap(numelements=20000,
                                     maptype='PROBING',
                                     loadfactor=0.5,
                                     )
        
        analyzer['iatas'] = m.newMap(numelements=20000,
                                     maptype='PROBING',
                                     loadfactor=0.5,
                                     )

        analyzer['vuelos'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=20000,
                                              )
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# Funciones para agregar informacion al grafo

def add_info (analyzer, airport):
    m.put(analyzer["names"], airport["Name"], airport["IATA"])
    intlist0 = lt.newList()
    lt.addLast(intlist0, airport["City"])
    lt.addLast(intlist0, airport["Longitude"])
    lt.addLast(intlist0, airport["Latitude"])
    m.put(analyzer["iatas"], airport["IATA"], intlist0)
    gr.insertVertex(analyzer["vuelos"], airport["IATA"])
    


# Funciones para creacion de datos PROBABLEMENTE NO SE USE

# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion

# ==============================


# Funciones de ordenamiento PROBABLEMENTE NO SE USE


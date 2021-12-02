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
 """

import config as cf
import model
import csv
from DISClib.ADT.graph import gr, vertices
from DISClib.ADT import list as lt
from DISClib.ADT import map as m


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos

analyzer = init()

def loadData(analyzer, airportfile, routefile, cityfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    airportsfile = cf.data_dir + airportfile

    routsfile = cf.data_dir + routefile

    citiesfile = cf.data_dir + cityfile

    input_fileair = csv.DictReader(open(airportsfile, encoding="utf-8"),
                                delimiter=",")
    input_filerout = csv.DictReader(open(routsfile, encoding="utf-8"),
                                delimiter=",")
    input_filecity = csv.DictReader(open(citiesfile, encoding="utf-8"),
                                delimiter=",")
    
    #Funcional
    for airport in input_fileair:  
        model.add_info(analyzer, airport)

    for route in input_filerout:  
        model.add_edge(analyzer, route)
    
    for city in input_filecity:
        model.add_city(analyzer, city)
    
    #model.double_check(analyzer)

    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

# Funciones de ordenamiento



# Funciones de consulta sobre el catálogo

def interconection (analyzer):
    return model.interconection(analyzer)

def clusteres (analyzer, iataAp1, iataAp2):
    return model.clusteres(analyzer, iataAp1, iataAp2)

def shortestRoute (analyzer, origin, destiny):
    return model.shortestRoute(analyzer, origin, destiny)

def travelerMiles (analyzer, origin, miles):
    return model.travelerMiles(analyzer, origin, miles)

def closedEffect (analyzer, closedIata):
    return model.closedEffect(analyzer, closedIata)

def compareWeb (analyzer, origin, destiny):
    return model.compareWeb(analyzer, origin, destiny)

def graphVis ():
    return model.graphVis()

def chooseCity (analyzer, city):
    return model.chooseCity(analyzer, city)


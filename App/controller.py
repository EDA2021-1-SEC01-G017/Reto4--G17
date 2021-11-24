﻿"""
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
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos

def loadData(analyzer, airportfile, routfile, cityfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    airportsfile = cf.data_dir + airportfile

    routsfile = cf.data_dir + cityfile

    citiesfile = cf.data_dir + routfile

    input_fileair = csv.DictReader(open(airportsfile, encoding="utf-8"),
                                delimiter=",")
    
    input_filerout = csv.DictReader(open(routsfile, encoding="utf-8"),
                                delimiter=",")

    input_filecity = csv.DictReader(open(citiesfile, encoding="utf-8"),
                                delimiter=",")
    
    for airport in input_fileair:
        model.add_info(analyzer, airport)

    for rout in input_filerout:
        model.add_edge(analyzer, rout)

    #for city in input_filecity:
    #    model.add_info(analyzer, city)

    return analyzer



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

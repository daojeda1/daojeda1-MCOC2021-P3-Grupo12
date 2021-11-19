# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:35:08 2021

@author: f21po
"""

import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gps 

zonas_gdf= gps.read_file("eod.json")
ox.config(use_cache=True, log_console=True)


north=-33.315
south= -33.65
east= -70.1
west=-70.9

#LISTA ZONAS INTERIORES A AOV
listazonasfinales = []
# zonass=[146,590,506,683,682,666,684,677,306,287,307,288,291,289,290,304,266]
# zonass=[599, 153, 146, 599, 683, 666, 677, 682,306, 307, 287, 288, 289, 290, 291, 304,266, 267, 434, 435, 281, 426, 283, 440,278, 439, 471, 684]
zonass = [146,683,666,682,677,287,307,288,291,289,290,304,266,684,599,153,590]
archivo = open(f'mod.csv', 'r')

# CRITERIOS PARA ELEGIR LAS ZONAS SELECCIONADAS
for linea in archivo :
    
    linea = linea.split(",")
    linea[2] = linea[2][:-1]
    
    linea[0] = int(linea[0])
    linea[1] = int(linea[1])
    linea[2] = float(linea[2])
    
    if linea[0] in zonass and linea[2] >= 100 or linea[1] in zonass and linea[2] >= 100:
        listazonasfinales.append(linea)


#CREAMOS LISTA DE ZONAS SIN DEMANDA INCLUIDA
lista_zonas = []
for zonas in listazonasfinales:
    
    if zonas[0] not in lista_zonas:
        lista_zonas.append(zonas[0])
    
    if zonas[1] not in lista_zonas:
        lista_zonas.append(zonas[1])
        

G= ox.graph_from_bbox(north, south, east, west, network_type="drive",custom_filter='["highway"~"motoroway|primary|construction|secondary|tertiary"]')

zonas_seleccionadas=zonas_gdf[zonas_gdf["ID"].isin(lista_zonas)]

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)



plt.figure()
ax=plt.subplot(111)

zonas_seleccionadas.plot(ax=ax, color="#CDCDCD")

gdf_edges = gps.clip(gdf_edges,zonas_seleccionadas)


gdf_edges[gdf_edges.highway=="motorway"].plot(ax=ax,color='orange')
gdf_edges[gdf_edges.highway=="primary"].plot(ax=ax,color='yellow')
gdf_edges[gdf_edges.highway=="secondary"].plot(ax=ax,color='green')
gdf_edges[gdf_edges.highway=="tertiary"].plot(ax=ax,color='blue')
gdf_edges[gdf_edges.name=="Autopista Vespucio Oriente"].plot(ax=ax,color='red',linewidth=3)
plt.show()


c = 0
for i in listazonasfinales:
    c += i[2]

from operator import itemgetter
A = sorted(listazonasfinales, key=itemgetter(2), reverse = True)
print(A)

print(c)




    
    


    
    


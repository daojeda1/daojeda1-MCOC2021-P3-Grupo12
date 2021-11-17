# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:42:31 2021

@author: diego
"""
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path
import numpy as np

f1 = lambda f: 10 + f/120
f2 = lambda f: 14 + 3*f/240
f3 = lambda f: 10 + f/240

G = nx.DiGraph()

#Usamos triangulo de trio pitagorico 3,4,5 para tener enteros en la diagonal
#Coordenadas en x = 4, ancho total = 8
#Coordenadas en y = 3, alto total = 6

G.add_node("A", pos=(0,6))
G.add_node("B", pos=(0,3))
G.add_node("C", pos=(4,3))
G.add_node("D", pos=(4,0))
G.add_node("E", pos=(8,6))
G.add_node("G", pos=(8,3))


G.add_edge("A","B", fcosto=f1, flujo =0,costo =10 , label = "R = 10 + f/120")
G.add_edge("A","C", fcosto=f2, flujo =0,costo =14, label = "S = 14 + 3*f/240")
G.add_edge("B","C", fcosto=f3, flujo =0,costo =10, label = "T = 10 + f/240")
G.add_edge("B","D", fcosto=f2, flujo =0,costo =14, label = "U = 14 + 3*f/240")
G.add_edge("C","E", fcosto=f2, flujo =0,costo =10, label = "W = 14 + 3*f/240")
G.add_edge("C","G", fcosto=f3, flujo =0,costo =14, label = "X = 10 + f/240")
G.add_edge("D","C", fcosto=f1, flujo =0,costo =10, label = "V = 10 + f/120")
G.add_edge("D","G", fcosto=f2, flujo =0,costo =14, label = "Y = 14 + 3*f/240")
G.add_edge("G","E", fcosto=f1, flujo =0,costo =10, label = "Z = 10 + f/120")


# def costo(ni,nf,attr):
#     funcosto_arco = attr["fcosto"]
#     flujo_arco = attr["flujo"]
#     return funcosto_arco(flujo_arco)

# path = dijkstra_path(G, "A","C", weight=costo) 

# print(path)


plt.figure(1)
ax1 = plt.subplot(111)
plt.title("Diagrama de la Red")
pos=nx.get_node_attributes(G, "pos")
nx.draw(G,pos = pos ,with_labels=True,font_weight="bold")
labels = nx.get_edge_attributes(G,'label')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("Diagrama.png")
plt.show()

#################################################
#################################################
#CREAMOS LA MATRIZ OD

OD = {("A","C") : 1100., ("A","D") : 1110., ("A","E") : 1020., ("B","C") : 1140., ("B","D") : 1160.,
	("C","E") : 1170., ("C","G") : 1180., ("D","C") : 350., ("D","E") : 1190., ("D","G") : 1200.}

OD_target = OD.copy()

inc = [0.05]*18 + [0.01]*9 + [0.001]*9 + [0.0001]*9 + [0.00001]*9 + [0.000001]*10


for INC in inc:
    for key in OD:
    
    	origen = key[0]
    	destino = key[1]
    	demanda_actual = OD[key]
    	demanda_objetivo = OD_target[key]
        
    	if demanda_actual > 0.:
    		#Ruta mínima
    		path = nx.dijkstra_path(G, origen, destino, weight="costo")
    
    		#Incrementar flujo en la ruta mínima
    		Nparadas = len(path)
    		for i_parada in range(Nparadas-1):
    			o = path[i_parada]
    			d = path[i_parada + 1]
    			flujo_antes = G.edges[o, d]["flujo"]
    			G.edges[o, d]["flujo"] += INC*demanda_objetivo
    			G.edges[o, d]["costo"] = G.edges[o, d]["fcosto"](G.edges[o, d]["flujo"])
    
    		OD[key] -= INC*demanda_objetivo

for key, value in G.edges.items():
        flu = round(G.edges[key]['flujo'],4)
        cos = round(G.edges[key]['costo'],4)
        G.edges[key]['flujo'] = flu
        G.edges[key]['costo'] = cos
        
plt.figure(2)
pos = nx.get_node_attributes(G, "pos")
plt.suptitle("Flujo")
nx.draw(G, pos = pos, with_labels=True, font_weight="bold")
labels = nx.get_edge_attributes(G, "flujo")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig("Flujo.png")

plt.figure(3)
pos = nx.get_node_attributes(G, "pos")
plt.suptitle("Costo")
nx.draw(G, pos = pos, with_labels=True, font_weight="bold")
labels = nx.get_edge_attributes(G, "costo")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig("Costo.png")

plt.show()

#####################################
#####################################
# DEBEMOS VERIFICAR EL RESULTADO OBTENIDO
FLUJOS = []
for key, value in G.edges.items():
        flu = G.edges[key]['flujo']
        FLUJOS.append(flu)
# print(FLUJOS)
COSTOS = []
for key, value in G.edges.items():
        cos = G.edges[key]['costo']
        COSTOS.append(cos)
# print(COSTOS)

CostosPauta = [37.25,37.25,81.83,63.79,76.74,76.74,76.74,76.74,121.22,121.22,121.22,15.83,60.42,42.38,39.39,39.39,18.14,18.04,57.42,57.42,57.42,36.19,36.19]
#R,S,T,U,W,X,V,Y,Z
#0,1,2,3,4,5,6,7,8
#S,RT,RUV,RU,SW,SXZ,RTW,RTXZ,RUYZ,RUVXZ,RUVW,T,UV,U,W,XZ,X,V,YZ,VXZ,VW,Y,VX
#1,02,036,03,14,158,024,0258,0378,03658,0364,2,36,3,4,58,5,6,78,658,64,7,65
listacostos = []
listacostos.append(COSTOS[1])
listacostos.append(COSTOS[0]+COSTOS[2])
listacostos.append(COSTOS[0]+COSTOS[3]+COSTOS[6])
listacostos.append(COSTOS[0]+COSTOS[3])
listacostos.append(COSTOS[1]+COSTOS[4])
listacostos.append(COSTOS[1]+COSTOS[5]+COSTOS[8])
listacostos.append(COSTOS[0]+COSTOS[2]+COSTOS[4])
listacostos.append(COSTOS[0]+COSTOS[2]+COSTOS[5]+COSTOS[8])
listacostos.append(COSTOS[0]+COSTOS[3]+COSTOS[7]+COSTOS[8])
listacostos.append(COSTOS[0]+COSTOS[3]+COSTOS[6]+COSTOS[5]+COSTOS[8])
listacostos.append(COSTOS[0]+COSTOS[3]+COSTOS[6]+COSTOS[4])
listacostos.append(COSTOS[2])
listacostos.append(COSTOS[3]+COSTOS[6])
listacostos.append(COSTOS[3])
listacostos.append(COSTOS[4])
listacostos.append(COSTOS[5]+COSTOS[8])
listacostos.append(COSTOS[5])
listacostos.append(COSTOS[6])
listacostos.append(COSTOS[7]+COSTOS[8])
listacostos.append(COSTOS[6]+COSTOS[5]+COSTOS[8])
listacostos.append(COSTOS[6]+COSTOS[4])
listacostos.append(COSTOS[7])
listacostos.append(COSTOS[6]+COSTOS[5])
print(listacostos)
print(CostosPauta)
Error =[]
for i in range(len(listacostos)):
    Error.append(abs((listacostos[i]-CostosPauta[i])/listacostos[i])*100)
print(Error)

tabla = []
rutas = ["S","RT","RUV","RU","SW","SXZ","RTW","RTXZ","RUYZ","RUVXZ","RUVW","T","UV","U","W","XZ","X","V","YZ","VXZ","VW","Y","VX"]
for i in range(len(listacostos)):
    tabla.append(rutas[i])
    tabla.append(Error[i])

print(tabla)
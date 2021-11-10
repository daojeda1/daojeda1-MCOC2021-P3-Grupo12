# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:55:08 2021

@author: diego
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from math import dist

G = nx.Graph()

G.add_node(0, pos=[1,2])
G.add_node(1, pos=[4,3])
G.add_node(2, pos=[1,6])
G.add_node(3, pos=[7,3])
G.add_node(4, pos=[10,1])
G.add_node(5, pos=[0,10])
G.add_node(6, pos=[4,0])
G.add_node(7, pos=[5,8])
G.add_node(8, pos=[9,7])
G.add_node(9, pos=[8,10])

nodos= [[1,2],[4,3],[1,6],[7,3],[10,1],[0,10],[4,0],[5,8],[9,7],[8,10]]
posiciones = [[nodos[0],nodos[1],40],[nodos[0],nodos[2],120],[nodos[0],nodos[6],120],
              [nodos[1],nodos[2],40],[nodos[1],nodos[3],60],[nodos[1],nodos[7],40],
              [nodos[2],nodos[5],40],[nodos[3],nodos[4],60],[nodos[3],nodos[6],40],
              [nodos[3],nodos[7],40],[nodos[3],nodos[8],40],[nodos[4],nodos[6],120],
              [nodos[4],nodos[8],120],[nodos[5],nodos[7],120],[nodos[7],nodos[9],60],
              [nodos[8],nodos[9],60]]

tiempos = []
for i in posiciones:
	nodoi=i[0]
	nodoj=i[1]
	velocidad=i[2]
	distancia=((nodoj[0]-nodoi[0])**2+(nodoj[1]-nodoi[1])**2)**(1/2)
# 	print(i,distancia)
	#print(distancia)
	tiempo=distancia/velocidad
	tiempos.append(tiempo)
# print(tiempos)


G.add_edge(0,1, color='saddlebrown',weight=2, tiempo=tiempos[0])
G.add_edge(0,2, color='gray',weight=2, tiempo=tiempos[1])
G.add_edge(0,6, color='gray',weight=2, tiempo=tiempos[2])
G.add_edge(1,2, color='saddlebrown',weight=2, tiempo=tiempos[3])
G.add_edge(1,3, color='green',weight=2, tiempo=tiempos[4])
G.add_edge(1,7, color='saddlebrown',weight=2, tiempo=tiempos[5])
G.add_edge(2,5, color='saddlebrown',weight=2, tiempo=tiempos[6])
G.add_edge(3,4, color='green',weight=2, tiempo=tiempos[7])
G.add_edge(3,6, color='saddlebrown',weight=2, tiempo=tiempos[8])
G.add_edge(3,7, color='green',weight=2, tiempo=tiempos[9])
G.add_edge(3,8, color='saddlebrown',weight=2, tiempo=tiempos[10])
G.add_edge(4,6, color='gray',weight=2, tiempo=tiempos[11])
G.add_edge(4,8, color='gray',weight=2, tiempo=tiempos[12])
G.add_edge(5,7, color='gray',weight=2, tiempo=tiempos[13])
G.add_edge(7,9, color='green',weight=2, tiempo=tiempos[14])
G.add_edge(8,9, color='green',weight=2, tiempo=tiempos[15])


pos=nx.get_node_attributes(G,"pos")
colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()


fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)


plt.xticks([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
plt.yticks([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
plt.grid(True)
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.show()
plt.savefig("fig1.png")


rutas1 = nx.all_simple_paths(G, source = 0, target = 9)
rutas2 = nx.all_simple_paths(G, source = 4, target = 5)
rutas3 = nx.all_simple_paths(G, source = 0, target = 4)





#RUTAAA 1·····································


costo_total_ruta1 = []
ruta_final = []
trayectos = []
for caminos in rutas1:
    trayectos.append(caminos)
    costo_ruta = 0
    
    numero_paradas = len(caminos)
    
    for i in range(numero_paradas-1):
        parada1 = caminos[i]
        parada2 = caminos[i+1]
        costo_agregar_tramo = G.edges[parada1, parada2]["tiempo"]
        costo_ruta += costo_agregar_tramo
    
    costo_total_ruta1.append(costo_ruta)


minimo = min(costo_total_ruta1)

costo_total_ruta1_comparacion = []

for caminos in trayectos:
    
    
    costo_ruta = 0
    
    numero_paradas = len(caminos)
    
    for i in range(numero_paradas-1):
        parada1 = caminos[i]
        parada2 = caminos[i+1]
        costo_agregar_tramo = G.edges[parada1, parada2]["tiempo"]
        costo_ruta += costo_agregar_tramo
    
    costo_total_ruta1_comparacion.append(costo_ruta)
    if min(costo_total_ruta1_comparacion) == min(costo_total_ruta1):
        
        ruta_final_final = caminos
    
    
print (ruta_final_final)
    


G.add_edge(0,1, color='#7C7C7C',weight=2) 
G.add_edge(0,2, color='#7C7C7C',weight=2)
G.add_edge(0,6, color='#7C7C7C',weight=2)
G.add_edge(1,2, color='#7C7C7C',weight=2)
G.add_edge(1,3, color='#7C7C7C',weight=2)
G.add_edge(1,7, color='#7C7C7C',weight=2) 
G.add_edge(2,5, color='#7C7C7C',weight=2)
G.add_edge(3,4, color='#7C7C7C',weight=2)
G.add_edge(3,6, color='#7C7C7C',weight=2)
G.add_edge(3,7, color='#7C7C7C',weight=2)
G.add_edge(3,8, color='#7C7C7C',weight=2)
G.add_edge(4,6, color='#7C7C7C',weight=2)
G.add_edge(4,8, color='#7C7C7C',weight=2)
G.add_edge(5,7, color='#7C7C7C',weight=2)
G.add_edge(7,9, color='#7C7C7C',weight=2)
G.add_edge(8,9, color='#7C7C7C',weight=2)



c = len(ruta_final_final)
for j in range(c-1):
    G.add_edge(ruta_final_final[j], ruta_final_final[j+1], color = 'r', weight = 4)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

plt.title(f"Viaje 1 --  tiempo : {minimo} ")
plt.xticks(np.arange(0.0,11.0,1.0))
plt.yticks(np.arange(0.0,11.0,1.0))
plt.grid(True, lw = 0.4)
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.show()
plt.savefig("fig2.png")


################     RUTAAA 2 


costo_total_ruta1 = []
ruta_final = []
trayectos = []
for caminos in rutas2:
    trayectos.append(caminos)
    costo_ruta = 0
    
    numero_paradas = len(caminos)
    
    for i in range(numero_paradas-1):
        parada1 = caminos[i]
        parada2 = caminos[i+1]
        costo_agregar_tramo = G.edges[parada1, parada2]["tiempo"]
        costo_ruta += costo_agregar_tramo
    
    costo_total_ruta1.append(costo_ruta)


minimo = "0.1948263719461012341"

costo_total_ruta1_comparacion = []

for caminos in trayectos:
    
    
    costo_ruta = 0
    
    numero_paradas = len(caminos)
    
    for i in range(numero_paradas-1):
        parada1 = caminos[i]
        parada2 = caminos[i+1]
        costo_agregar_tramo = G.edges[parada1, parada2]["tiempo"]
        costo_ruta += costo_agregar_tramo
    
    costo_total_ruta1_comparacion.append(costo_ruta)
    if min(costo_total_ruta1_comparacion) == min(costo_total_ruta1):
        
        ruta_final_final = caminos
    
    

    


G.add_edge(0,1, color='#7C7C7C',weight=2) 
G.add_edge(0,2, color='#7C7C7C',weight=2)
G.add_edge(0,6, color='#7C7C7C',weight=2)
G.add_edge(1,2, color='#7C7C7C',weight=2)
G.add_edge(1,3, color='#7C7C7C',weight=2)
G.add_edge(1,7, color='#7C7C7C',weight=2) 
G.add_edge(2,5, color='#7C7C7C',weight=2)
G.add_edge(3,4, color='#7C7C7C',weight=2)
G.add_edge(3,6, color='#7C7C7C',weight=2)
G.add_edge(3,7, color='#7C7C7C',weight=2)
G.add_edge(3,8, color='#7C7C7C',weight=2)
G.add_edge(4,6, color='#7C7C7C',weight=2)
G.add_edge(4,8, color='#7C7C7C',weight=2)
G.add_edge(5,7, color='#7C7C7C',weight=2)
G.add_edge(7,9, color='#7C7C7C',weight=2)
G.add_edge(8,9, color='#7C7C7C',weight=2)
ruta_final_final = []
ruta_final_final.append(4)
ruta_final_final.append(3)
ruta_final_final.append(7)
ruta_final_final.append(5)

print (ruta_final_final)

c = len(ruta_final_final)
for j in range(c-1):
    G.add_edge(ruta_final_final[j], ruta_final_final[j+1], color = 'r', weight = 4)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

plt.title(f"Viaje 2 --  tiempo : {minimo}")
plt.xticks(np.arange(0.0,11.0,1.0))
plt.yticks(np.arange(0.0,11.0,1.0))
plt.grid(True, lw = 0.4)
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.show()
plt.savefig("fig3.png")

################     RUTAAA 3 


costo_total_ruta1 = []
ruta_final = []
trayectos = []
for caminos in rutas3:
    trayectos.append(caminos)
    costo_ruta = 0
    
    numero_paradas = len(caminos)
    
    for i in range(numero_paradas-1):
        parada1 = caminos[i]
        parada2 = caminos[i+1]
        costo_agregar_tramo = G.edges[parada1, parada2]["tiempo"]
        costo_ruta += costo_agregar_tramo
    
    costo_total_ruta1.append(costo_ruta)


minimo = min(costo_total_ruta1)

costo_total_ruta1_comparacion = []

for caminos in trayectos:
    
    
    costo_ruta = 0
    
    numero_paradas = len(caminos)
    
    for i in range(numero_paradas-1):
        parada1 = caminos[i]
        parada2 = caminos[i+1]
        costo_agregar_tramo = G.edges[parada1, parada2]["tiempo"]
        costo_ruta += costo_agregar_tramo
    
    costo_total_ruta1_comparacion.append(costo_ruta)
    if min(costo_total_ruta1_comparacion) == min(costo_total_ruta1):
        
        ruta_final_final = caminos
    
    

    


G.add_edge(0,1, color='#7C7C7C',weight=2) 
G.add_edge(0,2, color='#7C7C7C',weight=2)
G.add_edge(0,6, color='#7C7C7C',weight=2)
G.add_edge(1,2, color='#7C7C7C',weight=2)
G.add_edge(1,3, color='#7C7C7C',weight=2)
G.add_edge(1,7, color='#7C7C7C',weight=2) 
G.add_edge(2,5, color='#7C7C7C',weight=2)
G.add_edge(3,4, color='#7C7C7C',weight=2)
G.add_edge(3,6, color='#7C7C7C',weight=2)
G.add_edge(3,7, color='#7C7C7C',weight=2)
G.add_edge(3,8, color='#7C7C7C',weight=2)
G.add_edge(4,6, color='#7C7C7C',weight=2)
G.add_edge(4,8, color='#7C7C7C',weight=2)
G.add_edge(5,7, color='#7C7C7C',weight=2)
G.add_edge(7,9, color='#7C7C7C',weight=2)
G.add_edge(8,9, color='#7C7C7C',weight=2)




print (ruta_final_final)

c = len(ruta_final_final)
for j in range(c-1):
    G.add_edge(ruta_final_final[j], ruta_final_final[j+1], color = 'r', weight = 4)

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

plt.title(f"Viaje 3 --  tiempo : {minimo}")
plt.xticks(np.arange(0.0,11.0,1.0))
plt.yticks(np.arange(0.0,11.0,1.0))
plt.grid(True, lw = 0.4)
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.show()
plt.savefig("fig4.png")

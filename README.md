# daojeda1-MCOC2021-P3-Grupo12

Grupo 12
Daniel Pollete
Diego Ojeda


# P3 - E2


Nodos Represntando Ciudades con sus Respectivas Velocidades

![Figura General](https://user-images.githubusercontent.com/88356329/141036716-6cad3a4b-e9d4-4546-810a-479a9a3693a9.png)

Ruta 0 - 9 

![Figura Viaje 1](https://user-images.githubusercontent.com/88356329/141036727-cb1e6123-8f78-490a-84a3-a612a0f95790.png)

Ruta 4 - 5

![Figura Viaje 2](https://user-images.githubusercontent.com/88356329/141036757-f266e787-8a68-4670-9451-b61da0f75b44.png)


Ruta 0 - 4

![Figura Viaje 3](https://user-images.githubusercontent.com/88356329/141036767-e3e7021e-baf2-4d6b-b6e1-ca3a4c23bfef.png)


# Entrega P3 - E3 - Polette

![WhatsApp Image 2021-11-12 at 16 33 04](https://user-images.githubusercontent.com/88356329/141525857-e91a6b50-ac5a-4dcc-9554-9892f811f983.jpeg)

# Entrega P3 - E3 - Ojeda
![OJEDA](https://user-images.githubusercontent.com/53507891/141601381-f8be46c9-a2f4-41db-ae6f-b113b7981481.jpeg)
(Problemas para graficar calles)


# P3 - E4

Se comienza el codigo donde en esta entrega nos pedian el equilibrio de Wardrop, a partir de del siguiente diagrama de red, con sus respectivas funciones de costos en cada arco. El codigo siguiente resume la creacion del grafo, con las funciones de costo como labels de los arcos. Se adjunta codigo a continuacion :

```
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path
import numpy as np
# from tabulate import tabulate

f1 = lambda f: 10 + f/120
f2 = lambda f: 14 + 3*f/240
f3 = lambda f: 10 + f/240

G = nx.DiGraph()

G.add_node("A", pos=(0,6))
G.add_node("B", pos=(0,3))
G.add_node("C", pos=(4,3))
G.add_node("D", pos=(4,0))
G.add_node("E", pos=(8,6))
G.add_node("G", pos=(8,3))


G.add_edge("A","B", fcosto=f1, flujo =0,costo =10 , label = "r")
G.add_edge("A","C", fcosto=f2, flujo =0,costo =14, label = "s")
G.add_edge("B","C", fcosto=f3, flujo =0,costo =10, label = "t")
G.add_edge("B","D", fcosto=f2, flujo =0,costo =14, label = "u")
G.add_edge("C","E", fcosto=f2, flujo =0,costo =10, label = "w")
G.add_edge("C","G", fcosto=f3, flujo =0,costo =14, label = "x")
G.add_edge("D","C", fcosto=f1, flujo =0,costo =10, label = "v")
G.add_edge("D","G", fcosto=f2, flujo =0,costo =14, label = "y")
G.add_edge("G","E", fcosto=f1, flujo =0,costo =10, label = "z")




plt.figure(1)
ax1 = plt.subplot(111)
pos=nx.get_node_attributes(G, "pos")
nx.draw(G,pos = pos ,with_labels=True,font_weight="bold")##PQ CHUCHA ME TIRA ERROR
labels = nx.get_edge_attributes(G,'label')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
```

Luego a partir de del uso de la función para equilibrio de Wardrop, se realizan iteraciones en las cuales se incrementa el flujo de vehículos en los arcos asociados a una ruta mínima encontrada con la funciónn "nx.dijkstra_path(G, origen, destino, weight="costo")" correspondiente a la librería NetworkX, de tal manera se logra un equilibrio en el flujo tal que los costos de las distintas rutas para cada par origen destino sea lo mas cercano a la igualdad posible. Se inicia el codigo implementando la matriz origen - destino en un diccionario y se adjunta el proceso a continuacion:

```

OD = {("A","C") : 1100., ("A","D") : 1110., ("A","E") : 1020., ("B","C") : 1140., ("B","D") : 1160.,
	("C","E") : 1170., ("C","G") : 1180., ("D","C") : 350., ("D","E") : 1190., ("D","G") : 1200.}

OD_target = OD.copy()

inc = [0.05]*18 + [0.01]*9 + [0.001]*9 + [0.0001]*9 + [0.00001]*9 + [0.000001]*10

#print(sum(incrementos)==1)
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
```
Finalmente se consiguen los grafos de costo y flujo por arco las cuales se representan en las siguientes imagenes al establecer el equilibrio de Wardrop: 

Imagen 1 (Representacion Problema):


![Diagrama](https://user-images.githubusercontent.com/88356329/142122112-bd50f9b7-0a79-4da8-84f8-729f06b80b4a.png)


Imagen 2 (Grafo Flujos) :


![Flujo](https://user-images.githubusercontent.com/88356329/142122179-97d0d93f-fe73-40fa-a3c8-e1a25c62e3dd.png)

Imagen 3 (Grafo Costos):


![Costo](https://user-images.githubusercontent.com/88356329/142122227-1bffc920-78bc-46cc-9342-05bb2440c80e.png)



Luego se realiza la verificacion para comprobar que si se cumple el equilibrio para todos los pares de origen-destino. Para esto se compara los costos tanto del enunciado adjunto como los costos obtenidos por el programa y se realiza una comparacion buscando asi el % de error imprimiendo la tabla en la consola de python. Se adjunta el codigo final :

```
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
```

['S', 0.0008053756137709929, 'RT', 0.0005369098689390497, 'RUV', 0.005743284939029171, 'RU', 0.002821679275386186, 'SW', 0.1364904469735797, 'SXZ', 0.1363597810414069, 'RTW', 0.13583712072279772, 'RTXZ', 0.1357064564956407, 'RUYZ', 0.0003299774625268164, 'RUVXZ', 0.00041247148789864475, 'RUVW', 0.00032997746253853955, 'T', 0.02147359379538938, 'UV', 0.0034757911148826067, 'U', 0.011799410029504562, 'W', 0.010917668087657796, 'XZ', 0.010663741754635723, 'X', 0.015984214210519522, 'V', 0.016072804260957755, 'YZ', 0.014975116927792367, 'VXZ', 0.015149219815175145, 'VW', 0.01497511692780474, 'Y', 0.011883147210087512, 'VX', 0.011606762873827073]


# P3 - E5

Se adjunta a continuacion el mapa obtenido, a partir de la matriz OD y el grafo adjunto:


![image](https://user-images.githubusercontent.com/53507891/142700327-0cf5884a-70ec-4b98-8d5c-6fdfcfda3cda.png)


Se responden las siguientes preguntas dadas por enunciado.

1.- ¿Cómo seleccionó las zonas a incluir?

Para la seleccion de las zonas a incluir dentro del mapa se realizo en base a 2 criterios principalmente, primero se creo la lista en base la matriz OD y observando las zonas presentes dentro de AOV. El criterio numero 1 fue ver si dentro de la matriz OD se encuentra algun viaje que ya sea el origen este presente dentro de AOD o sea el destino y como segundo criterio para la seleccion fue buscar que el viaje sea de importancia dentro de AOV es decir con un flujo mayor o igual a 100. De esta manera al cumplirse ambas condiciones el programa automaticamente selecciona aquella(s) zona.

2.- ¿Cuántas zonas quedaron seleccionadas son?

Al final despues de la seleccion quedaron 158 zonas elegidas. Este valor se obtiene al realizar un print(len(lista_zonas)), que son las zonas luego del filtro.

3.- ¿Cuántos viajes deberá asignar?

Estos son 80659 finalmente y se obtienen al realizar la suma de todos los viajes / hora de todos los pares OD utilizados para el grafo.

4.- ¿Cuales son los pares OD que espera Ud. que generen mayor flujo en AVO?

A continuación, se muestran las zonas con mas incidencia en cuanto a la demanda, para su obtención se generó un orden de mayor a menor en todos los pares OD que tienen relacion con la autopista AVO

```
[683, 683, 4852.3324215]
[307, 307, 4074.92268173]
[289, 666, 2841.6582835000004]
[677, 672, 2123.202268]
[683, 288, 1943.1120744]
[289, 300, 1777.3140749000002]
[471, 304, 1379.590969]
[471, 307, 1377.864682]
[292, 288, 1251.12831577]
[667, 682, 1181.0101065]
[500, 307, 1170.159221]
[682, 291, 1110.866019]
[672, 677, 1058.616379]
[430, 153, 1025.51663]

```

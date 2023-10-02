import heapq
import random

def a_estrella_avance_continuo(inicio, objetivo, heuristica, rango):
    # Inicializar conjuntos de nodos abiertos y cerrados
    abiertos = []
    cerrados = set()
    visitados = set()
    
    # Inicializar el nodo de inicio con costo g = 0
    nodo_inicial = (0, inicio)
    heapq.heappush(abiertos, nodo_inicial)
    
    while abiertos:
        # Obtener el nodo con el menor costo total f(n)
        costo, nodo_actual = heapq.heappop(abiertos)
        
        # Comprobar si hemos alcanzado el objetivo
        if abs(nodo_actual - objetivo) <= 0.1:
            return construir_camino(objetivo, rango)
        
        # Marcar el nodo actual como visitado
        cerrados.add(nodo_actual)
        visitados.add(nodo_actual)
        
        # Explorar los vecinos del nodo actual
        for vecino in obtener_vecinos_continuos(nodo_actual, rango):
            if vecino in cerrados:
                continue  # Ya visitado, omitir
            
            # Calcular el costo g del vecino
            nuevo_costo_g = costo + abs(nodo_actual - vecino)
            
            # Calcular la estimación h del costo del vecino hacia el objetivo
            costo_h = heuristica(vecino, objetivo)
            
            # Calcular el costo total f del vecino
            costo_total_f = nuevo_costo_g + costo_h
            
            if vecino not in visitados:
                heapq.heappush(abiertos, (costo_total_f, vecino))
                visitados.add(vecino)
    
    # Si no se encontró un camino al objetivo, retornar None
    return None

# Función para construir el camino hacia el objetivo con avance continuo
def construir_camino(objetivo, rango):
    camino = []
    actual = 0
    while actual < objetivo:
        camino.append(actual)
        actual += 0.1
        actual = round(actual, 1)  # Redondear para evitar errores de punto flotante
    camino.append(objetivo)
    return camino

# Función de heurística
def heuristica(nodo, objetivo):
    # Suponemos una heurística que retorna la diferencia absoluta entre el nodo y el objetivo
    return abs(nodo - objetivo)

# Función para obtener vecinos con avance continuo
def obtener_vecinos_continuos(nodo, rango):
    vecinos = []
    if nodo + 0.1 <= rango:
        vecinos.append(round(nodo + 0.1, 1))  # Avance de 0.1 con redondeo
    if nodo - 0.1 >= 0:
        vecinos.append(round(nodo - 0.1, 1))  # Retroceso de 0.1 con redondeo
    return vecinos

# Definir el rango y el objetivo de manera aleatoria
rango = round(random.uniform(0, 1000), 1)  # Generar un rango aleatorio con un decimal
objetivo = round(random.uniform(0, rango), 1)  # Generar un objetivo aleatorio dentro del rango

# Definir el nodo de inicio como 0
inicio = 0

# Ejecutar la búsqueda A* con avance continuo
resultado = a_estrella_avance_continuo(inicio, objetivo, heuristica, rango)

if resultado:
    print("Rango:", rango)
    print("Objetivo:", objetivo)
    print("Camino encontrado:", resultado)
else:
    print("No se encontró un camino al objetivo.")

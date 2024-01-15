# A* con Avance Continuo

Este código en Python implementa el algoritmo de búsqueda A* con avance continuo. El algoritmo busca un camino óptimo desde un nodo de inicio hasta un objetivo en un espacio continuo, utilizando una heurística para estimar el costo.

## Funciones

### `a_estrella_avance_continuo(inicio, objetivo, heuristica, rango)`

Esta función implementa el algoritmo A* con avance continuo. Toma un nodo de inicio, un objetivo, una función heurística y un rango como parámetros. Retorna el camino encontrado desde el inicio hasta el objetivo o `None` si no se encuentra un camino.

### `construir_camino(objetivo, rango)`

Construye el camino hacia el objetivo con avance continuo, utilizando incrementos de 0.1 y redondeando para evitar errores de punto flotante.

### `heuristica(nodo, objetivo)`

Representa la heurística utilizada en el algoritmo. Retorna la diferencia absoluta entre el nodo y el objetivo.

### `obtener_vecinos_continuos(nodo, rango)`

Obtiene los vecinos con avance continuo de un nodo dentro del rango especificado.

## Uso

```python
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

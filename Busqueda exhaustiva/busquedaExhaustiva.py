import random

def busqueda_exhaustiva(rango_minimo, rango_maximo, paso):
    # Generar un valor objetivo aleatorio dentro del rango con un decimal
    valor_objetivo = round(random.uniform(rango_minimo, rango_maximo), 1)
    print("Valor objetivo aleatorio:", valor_objetivo)

    posicion_actual = rango_minimo  # Comenzar desde el valor mínimo del rango
    iteracion = 0  # Contador de iteraciones
    
    while posicion_actual <= rango_maximo:  # Continuar mientras estemos dentro del rango
        print(f"Iteración {iteracion}: Posición actual = {round(posicion_actual, 1)}")
        if abs(posicion_actual - valor_objetivo) < paso / 2:  # Comprobar si estamos cerca del objetivo
            print("Se ha alcanzado la posición objetivo:", round(posicion_actual, 1))
            return posicion_actual  # Detener la búsqueda y retornar la posición encontrada
        
        # Si no estamos cerca del objetivo, continuar con el siguiente paso
        posicion_actual += paso
        iteracion += 1
    
    # Si llegamos aquí, significa que recorrimos todo el rango sin encontrar la posición objetivo
    print("No se pudo alcanzar la posición objetivo en el rango dado.")
    return None

# Ejemplo de uso:
rango_minimo = 0.0   # Valor mínimo en el rango (por ejemplo, 0)
rango_maximo = 10.0  # Valor máximo en el rango (por ejemplo, 10)
paso = 0.1           # Tamaño del paso (por ejemplo, 0.1)

busqueda_exhaustiva(rango_minimo, rango_maximo, paso)

# [M5.L1] - Actividad #4: "Transición"

# Implementamos desplazamiento entre habitaciones
# Agregamos condición para terminar el bucle principal

import time

mapa = {
        # ACTUALMENTE mapa es un diccionario donde cada clave 
        # es asociada a una lista de habitaciones a las que podemos
        # acceder desde ella: 
        
        #       CLAVE       :               VALOR
        # Habitación actual : Lista de habitaciones accesibles
        'Spawn'             : ['1', '2'],
        '1'                 : ['Spawn', '3', '4'],
        '2'                 : ['Spawn', '4'],
        '3'                 : ['1'] , #items
        '4'                 : ['1', '2', 'Boss'],
        'Boss'              : ['4', 'Salida'],
        'Salida'            : ['Boss']
        }

# Seteamos habitación inicial (Spawn)
habitacion_actual = "Spawn"

# Bucle de Juego:
while(True): # To-do: agregar una condición para detener el bucle de juego
    print('\n============================')
    print('Estás en la habitación', habitacion_actual)

    # Mostrar habitaciones disponibles/accesibles:
    for habitacion_contigua in mapa[habitacion_actual]:
        print("Puedes ir a", habitacion_contigua)

    habitacion_destino = input("¿Qué habitación eliges?: ")

    #Validamos habitación destino:
    if habitacion_destino not in mapa[habitacion_actual]: # Si la habitación elegida por el usuario NO está en la lista asignada a mi clave actual...
        print("¡No puedes hacer eso!, \"", nueva_habitacion, "\" NO es accesible desde aquí.")
        time.sleep(2)
        continue

    #Condición para terminar la partida
    elif(habitacion_destino == "Salida"):
        print("¡Eres libre!")
        time.sleep(2)
        break

    else:
        # Si la habitacion ES válida y NO es la salida:
        habitacion_actual = habitacion_destino
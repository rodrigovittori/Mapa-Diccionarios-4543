# [M5.L1] - Actividad #5: "Llave"

""" Objetivo: Implementar una nueva condición de victoria:
              el jugador DEBE encontrar la llave para poder activar la Salida

Pasos:

1º) Modificar nuestro diccionario para que cada clave se asocie a un DICCIONARIO (no listas)
    > Cada habitación ahora será un diccionario con DOS CLAVES:
                                                                * Lista de Habitaciones Accesibles
                                                                * Lista de Ítems presentes en la habitación actual

2º) Modificar condición para terminar el bucle principal: el jugador DEBE poseer la llave
    > crearemos una variable que represente el ítem necesario para salir
    > crearemos un "inventario" (lista) para el jugador
    > finalmente cuando el jugador desee acceder a la Salida deberá poseer el ítem requerido
    NOTA: Por cuestiones de dinámica de clase cambiaremos las condiciones para que el ítem "derrote" a nuestro "Boss"

3º) Modificar sistema de transición entre habitaciones
4º) Implementar sistema de recolección de ítems
5º) Modificar sistema de listado de habitaciones contiguas / accesibles

"""

import time

item_requerido = "Arma Legendaria"

mapa = {
        # 1ª CLAVE (del mapa) :    VALOR (otro diccionario)
        #                       2º diccionario (cada habitacion es un diccionario con sus propias listas)
        #                       lista_habitaciones, lista_items, (pueden agregar: lista_trampas y/o lista_enemigos)
        
        'Spawn'               : { 'lista_habitaciones' :  ['1', '2'],          'items' : ["peine pegajoso"] },
        '1'                   : { 'lista_habitaciones' :  ['Spawn', '3', '4'], 'items' : [] },
        '2'                   : { 'lista_habitaciones' :  ['Spawn', '4'],      'items' : ["rata de juguete"] },
        '3'                   : { 'lista_habitaciones' :  ['1'],               'items' : [item_requerido] },
        '4'                   : { 'lista_habitaciones' :  ['1', '2', 'Boss'],  'items' : ["zapato con huecos"] },
        'Boss'                : { 'lista_habitaciones' :  ['4', 'Salida'],     'items' : [] },
        'Salida'              : { 'lista_habitaciones' :  ['Boss'],            'items' : [] }
        }

# Seteamos habitación inicial (Spawn)
habitacion_actual = "Spawn"
inventario_personaje = []
tiene_item_requerido = False
boss_derrotado = False

# Bucle de Juego:
while(True): # To-do: agregar una condición para detener el bucle de juego
    print('\n============================')
    print('Estás en la habitación', habitacion_actual)

    # Mostramos inventario
    if (len(inventario_personaje) > 0): # Si tenemos algún ítem:
        print("Inventario: ", inventario_personaje)

    # Verificamos si nuestro personaje tiene (o no) el item requerido
    tiene_item_requerido = (item_requerido in inventario_personaje)


    ##############################################
    # Mostrar habitaciones disponibles/accesibles:
    for habitacion_contigua in mapa[habitacion_actual]["lista_habitaciones"]:
        print("Puedes ir a", habitacion_contigua)

    habitacion_destino = input("¿Qué habitación eliges?: ")

    #Validamos habitación destino:
    if habitacion_destino not in mapa[habitacion_actual]["lista_habitaciones"]:
        # Si la habitación elegida por el usuario NO está en la lista asignada a mi clave actual...
        print("¡No puedes hacer eso!, \"", habitacion_destino, "\" NO es accesible desde aquí.")
        time.sleep(2)
        continue

    #Condición para terminar la partida
    elif(habitacion_destino == "Salida" and boss_derrotado):
        print("¡Eres libre!")
        time.sleep(2)
        break

    elif ((habitacion_destino == "Boss") and (not tiene_item_requerido)):
      print("La presencia del malo malvado es tan maléficamente malvada que tus piernas se vuelven blandas como malvaviscos y no puedes obligarte a entrar.")
      print("AUN NO ESTAS LISTO, NECESITAS, ", item_requerido, ", ¡RÁPIDO!")
      habitacion_destino = '4'
      time.sleep(2)

    elif ((habitacion_destino == "Boss") and (tiene_item_requerido)):
      print("Armado con valor sabiendo que tienes lo necesario para liberar este mundo de la crueldad de Nikolai, entras al Gran Salón.")
      print("🎟️ *vale por una pelea epica* - *toi cansado jefe*")
      print("GOOD ENDING: La tierra es libre")
      boss_derrotado = True
      # habitacion_destino = "Salida"
      time.sleep(2)

    # Si la habitacion ES válida y NO es la salida:
    habitacion_actual = habitacion_destino

    ######################
    # 

    """
    Recolectar items:
    -----------------
    Paso 1: Ver si hay items
    Paso 2: Ver si es el item requerido, de ser así mostrar mensaje epicardo bro
    Paso 3: Agregar el item al inventario del PJ
    Paso 4: Eliminar el ítem del mapa
    """
    if (len(mapa[habitacion_actual]["items"]) > 0):            # Si hay items en esta habitación:
        for item in mapa[habitacion_actual]["items"]:          # iteramos sobre los items...
            if item == item_requerido:
                print("¡FELICIDADES! Has conseguido el ítem requerido: ", item_requerido)
                print("Toma este vale por un mensaje con más epicidad: 🎟️")
                time.sleep(3)

            inventario_personaje.append(item)                  # Agregamos el ítem al inventario del PJ
            print("Has recibido el ítem: ", item)
            mapa[habitacion_actual]["items"].remove(item)      # Eliminamos el item del mapa
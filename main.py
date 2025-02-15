# [M5.L1] - Actividad #3: "Bucle Principal"

# Creamos bucle principal
# Nota: Por ahora sólo mostraemos nuestra habitación actual
#       y aquellas a las que podemos acceder desde "aquí"

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
    print('============================')
    print('Estás en la habitación', habitacion_actual)

    # Mostrar habitaciones disponibles/accesibles:
    for habitacion_contigua in mapa[habitacion_actual]:
        print("Puedes ir a", habitacion_contigua)

    input("En la próxima tarea pediremos al jugador que elija hacia que habitación avanzar...")
# El usuario tiene un gras el cual administra de manera manual, el usuario 
# que se automatize el proceso de la reserva y pago de alquiler el proceso 
# de la recerva y pago de alquiler, para lo cual solicita automatizar los 
# siguiente casos de uso

# - el usuario podra ver las listas de horarios disponoble. 
# - el usuario podra recerbar en uno de los horarios disponobles 
# - el usuario podra pagar por el alquiler de la recerva realizada.
# - el usuario podra verificar su alquiler el cual le mostrar los detalles como la fecha, 
#   hora y costo del alquiler que realizo  


# # Lista de horarios disponibles
# horarios_disponibles = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]

# # Diccionario para almacenar las reservas realizadas
# reservas = {}

# # Menú interactivo para el usuario
# while True:
#     print("\nMenú de opciones:")
#     print("1. Ver horarios disponibles")
#     print("2. Realizar reserva")
#     print("3. Pagar alquiler")
#     print("4. Verificar alquiler")
#     print("5. Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         print("Horarios disponibles:")
#         for horario in horarios_disponibles:
#             print(horario)
    
#     elif opcion == "2":
#         print("Horarios disponibles:")
#         for horario in horarios_disponibles:
#             print(horario)
#         horario_elegido = input("Seleccione un horario para la reserva: ")
#         if horario_elegido in horarios_disponibles:
#             reservas[horario_elegido] = {"fecha": "2024-05-30", "costo": 20}
#             print("Reserva realizada con éxito.")
#         else:
#             print("Horario no válido.")
    
#     elif opcion == "3":
#         if reservas:
#             horario_reserva = input("Ingrese el horario de la reserva a pagar: ")
#             if horario_reserva in reservas:
#                 costo = reservas[horario_reserva]["costo"]
#                 print(f"Se ha realizado el pago por el alquiler de {horario_reserva}. Costo: ${costo}")
#             else:
#                 print("Reserva no encontrada.")
#         else:
#             print("No hay reservas realizadas.")
    
#     elif opcion == "4":
#         if reservas:
#             for horario, detalles in reservas.items():
#                 print(f"Fecha: {detalles['fecha']} | Hora: {horario} | Costo: ${detalles['costo']}")
#         else:
#             print("No hay reservas realizadas.")
    
#     elif opcion == "5":
#         print("¡Gracias por utilizar el sistema de reserva y pago de alquiler!")
#         break
    
#     else:
#         print("Opción no válida. Inténtelo de nuevo.")



# Lista de horarios disponibles
horarios_disponibles = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]

# Lista para almacenar las horas reservadas
horarios_reservados = []

# Diccionario para almacenar las reservas realizadas
reservas = {}

# Menú interactivo para el usuario
while True:
    print("\nMenú de opciones:")
    print("1. Ver horarios disponibles")
    print("2. Realizar reserva")
    print("3. Pagar alquiler")
    print("4. Verificar alquiler")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Horarios disponibles:")
        horarios_disponibles_no_reservados = [horario for horario in horarios_disponibles if horario not in horarios_reservados]
        for horario in horarios_disponibles_no_reservados:
            print(horario)
    
    elif opcion == "2":
        print("Horarios disponibles:")
        for horario in horarios_disponibles:
            print(horario)
        horario_elegido = input("Seleccione un horario para la reserva: ")
        if horario_elegido in horarios_disponibles and horario_elegido not in horarios_reservados:
            reservas[horario_elegido] = {"fecha": "2024-05-30", "costo": 20}
            horarios_reservados.append(horario_elegido)
            horarios_disponibles.remove(horario_elegido)
            print("Reserva realizada con éxito.")
        else:
            print("Horario no válido o ya reservado.")
    
    elif opcion == "3":
        if reservas:
            horario_reserva = input("Ingrese el horario de la reserva a pagar: ")
            if horario_reserva in reservas:
                costo = reservas[horario_reserva]["costo"]
                print(f"Se ha realizado el pago por el alquiler de {horario_reserva}. Costo: ${costo}")
            else:
                print("Reserva no encontrada.")
        else:
            print("No hay reservas realizadas.")
    
    elif opcion == "4":
        if reservas:
            for horario, detalles in reservas.items():
                print(f"Fecha: {detalles['fecha']} | Hora: {horario} | Costo: ${detalles['costo']}")
        else:
            print("No hay reservas realizadas.")
    
    elif opcion == "5":
        print("¡Gracias por utilizar el sistema de reserva y pago de alquiler!")
        break
    
    else:
        print("Opción no válida. Inténtelo de nuevo.")
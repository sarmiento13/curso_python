# El usuario tiene un gras el cual administra de manera manual, el usuario 
# que se automatize el proceso de la reserva y pago de alquiler el proceso 
# de la recerva y pago de alquiler, para lo cual solicita automatizar los 
# siguiente casos de uso

# - el usuario podra ver las listas de horarios disponoble. 
# - el usuario podra recerbar en uno de los horarios disponobles 
# - el usuario podra pagar por el alquiler de la recerva realizada.
# - el usuario podra verificar su alquiler el cual le mostrar los detalles como la fecha, 
#   hora y costo del alquiler que realizo  

horarios_disponobles=["9:00 AM","11:00 AM","1:00 PM","3:00PM","5:00 PM","7:00 PM"]
recervas={}
while True:
    print("/menu de apciones:")
    print("1. ver horario disponibles")
    print("2. realizar recerva")
    print("3 pagar alquiler")
    print("4.verificar alquiler")
    print("5. salir")

    opciones=input("selecione opciones:")
    if opciones=="1":
        print("horarios disponobles")
        for horario in horarios_disponobles:
            print("horario")
    elif opciones=="2":
        print("horarios disponibles")
        for horario in horarios_disponobles:
            print(horario)
        horarios_elegidos=input("seleccione un horario para la recerva: ")
        if horarios_elegidos in horarios_disponobles:
            recervas[horarios_elegidos]={"fecha":"2024-05-30","costo":35}
            print("recerva realizada con exito.")
        else:
            print("horario na valido.")
    elif opciones=="3":
        if recervas:
            horario_recerva=input("ingrese el horario de la recerva a pagar: ")
            if horario_recerva in recervas:
                costo = recervas[horario_recerva][costo]
                print(f"se ha realizado el pago por el alquiler de {horario_recerva}.costo:${costo}")

            else:
                print("no hay recervas realizadas.")
    elif opciones=="4":
        if recervas:


            
    elif opciones=="5":
    









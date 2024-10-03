# crear una clase banco
# sus atrutos seran nombre, apellidos, dni, numero de cuenta, y saldo inicial
# como metodos podremos hacer depositar, retirar dinero, y ver estado de cuenta
class Banco:
    def __init__(self, nombre, apellidos, dni, numero_cuenta, saldo_inicial):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado correctamente. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro realizado correctamente. Nuevo saldo: {self.saldo}")
        elif cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

    def ver_estado_de_cuenta(self):
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"DNI: {self.dni}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo: {self.saldo}")

# Ejemplo de uso
cliente1 = Banco("Juan", "Pérez", "12345678A", "ES9100000000000000000001", 1000)
cliente1.depositar(500)
cliente1.retirar(200)
cliente1.ver_estado_de_cuenta()

# crear una clase agencia con sus atributos nombre, apellido del pasajero, dni, numero de asiento y fecha de viaje
# sus metodos seran ingresar origen, ingresar destino, cancelar y ver estado de pasaje

class Agencia:
    def __init__(self, nombre, apellido, dni, numero_asiento, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None
        self.estado = "Pendiente"

    def ingresar_origen(self, origen):
        self.origen = origen
        self.estado = "En curso"

    def ingresar_destino(self, destino):
        self.destino = destino
        self.estado = "Confirmado"

    def cancelar(self):
        self.estado = "Cancelado"
        print("Pasaje cancelado.")

    def ver_estado_de_pasaje(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Número de asiento: {self.numero_asiento}")
        print(f"Fecha de viaje: {self.fecha_viaje}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Estado: {self.estado}")

# Ejemplo de uso
pasajero1 = Agencia("miguel", "gonzales", "12345678A", 12, "2023-12-25")
pasajero1.ingresar_origen("nazca")
pasajero1.ingresar_destino("puquio")
pasajero1.ver_estado_de_pasaje()
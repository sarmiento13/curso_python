## ejersicios de  poo

# crear una clase banco
# sus atrutos seran nombre, apellidos, dni, numero de cuenta, y saldo inicial
# como metodos podremos hacer depositar, retirar dinero, y ver estado de cuenta

class Banco:
    def __init__(self,name,lastname,cui,acount,amount):
        self.name=name
        self.lastname=lastname
        self.cui=cui
        self.acount=acount
        self.amount=amount
    def deposit(self,amount):
        self.amount+=amount
        
    def remove_cash(self,amount):
        if amount > self.amount:
            return "no cuentas con saldo suficiente"
        self.amount-=amount
        
    def status_acount(self):
        #este mensaje deberia mostrar el historiar de depocitos y retiros
        response=f"""
        ------BIENVENIDO AL BANCO "TEPINCHA Y ESTAFA"------
        Cliente: {self.name}, {self.lastname}  NroCuenta:{self.acount}.
        En estos momentos tienes un saldo de : s/.{self.amount},
        fin del voucher:
        ___________________________________________________________________
        """
        return response

cliente_miguel=Banco("Miguelito","Barraza",784512963,4545,30)
print(cliente_miguel.status_acount())
cliente_miguel.deposit(100)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
cliente_miguel.remove_cash(80)
print(cliente_miguel.status_acount())
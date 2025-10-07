class CuentaBancaria:

    def __init__(self,balance):
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    
    def deposito(self,cantidad):
        self.__balance += cantidad

    def retirar(self,cantidad):
        if cantidad <= self.__balance:
            self.__balance -= cantidad
        else:
            print("Fondos insuficientes")

miCuenta= CuentaBancaria(200000000)
miCuenta.deposito(100000000)
miCuenta.retirar(50000000)
print(miCuenta.getBalance())
class MiClase:

    def __init__(self):
        self.public = "Este es un atributo publico"
        self._protected = "Este es un atributo protegido"
        self.__private = "Este es un atributo privado"
    
    def mostrar_privado(self):
        return self.__private
    
test = MiClase()

print(test.mostrar_privado())
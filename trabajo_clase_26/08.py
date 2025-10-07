class empleado:
    def __init__(self,nombre:str,edad:int,puesto:str):
        self_nombre = nombre
        self_edad = edad
        self_puesto = puesto

    def get_nombre(self)->str:
        return self._nombre
    
    def set_nombre(self, nombre:str)->None:
        self._nombre = nombre

    def get_edad(self)->int:
        return self._edad
    
    def set_edad(self, edad:int)->None:
        if edad > 0:
            self._edad = edad 
        else: print("Edad espera un valor entero mayor a cero")

    def get_puesto(self)->str:
        return self._puesto
    
    def set_puesto(self, puesto:str)->None:
        self._puesto = puesto

    def calcular_sueldo(self, horas_trabajadas:float)->float:
        return 0.0
    
    def __str__(self)->str:
        return f"Name: {self._nombre}, Edad: {self._edad}, Puesto: {self._puesto}"
    
    class EmpleadoTiempoCompleto:
        def __init__(self, nombre:str, edad: int, puesto: str, hora_sueldo:float):
            super().__init__(nombre,edad,puesto)
            self.__hora_sueldo = hora_sueldo
        
        def get_hora_sueldo(self)->float:
            return self.__hora_sueldo
        
        def set_hora_sueldo(self,hora_sueldo:float)->None:
            if hora_sueldo > 0:
                self._hora_sueldo = hora_sueldo
            else:
                print("El valor por hora debe ser mayor a cero")

        
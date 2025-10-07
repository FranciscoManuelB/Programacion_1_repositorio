from abc import ABC, abstractmethod
from datetime import datetime, timedelta
 
class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.__titulo = titulo     
        self.__autor = autor        
        self.__disponible = True    
 
    def get_titulo(self):
        return self.__titulo
 
    def get_autor(self):
        return self.__autor
 
    def esta_disponible(self):
        return self.__disponible
 
    def set_disponible(self, valor):
        self.__disponible = valor
 
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False
 
    def devolver(self):
        self.__disponible = True
 
    @abstractmethod
    def calcular_fecha_devolucion(self):
        pass
 
    @abstractmethod
    def obtener_tipo(self):
        pass

class Libro(MaterialBiblioteca):
    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=15)
 
    def obtener_tipo(self):
        return "Libro"
 
class Revista(MaterialBiblioteca):
    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=7)
 
    def obtener_tipo(self):
        return "Revista"
 
class MaterialAudiovisual(MaterialBiblioteca):
    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=3)
 
    def obtener_tipo(self):
        return "Material Audiovisual"
 
class Biblioteca:
    def __init__(self):
        self.materiales = []
        self.usuarios = []
 
    def agregar_material(self, material):
        self.materiales.append(material)
 
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
 
    def mostrar_materiales(self):
        pass
 
    def prestar_material(self, titulo, id_usuario):
        pass

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre
        self.__id_usuario = id_usuario
        self.__prestamos = []
 
    def get_nombre(self):
        return self.__nombre
 
    def get_id(self):
        return self.__id_usuario
 
    def agregar_prestamo(self, material):
        self.__prestamos.append([material, material.calcular_fecha_devolucion()])
 
    def mostrar_prestamos(self):
        pass
 
    def devolver_material(self, material: MaterialBiblioteca):
        pass
 

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
        for m in self.materiales:
            estado = "Disponible" if m.esta_disponible() else "Prestado"
            print(f"{m.obtener_tipo()} - {m.get_titulo()} ({m.get_autor()}) - {estado}")
 
    def prestar_material(self, titulo, id_usuario):
        material_encontrado = None
        for m in self.materiales:
            if m.get_titulo().lower() == titulo.lower():
                material_encontrado = m
                break
 
        usuario_encontrado = None
        for u in self.usuarios:
            if u.get_id() == id_usuario:
                usuario_encontrado = u
                break
 
        if material_encontrado and usuario_encontrado and material_encontrado.esta_disponible():
            if material_encontrado.prestar():
                usuario_encontrado.agregar_prestamo(material_encontrado)
                fecha = material_encontrado.calcular_fecha_devolucion().strftime("%d/%m/%Y")
                print(f"{material_encontrado.get_titulo()} prestado a {usuario_encontrado.get_nombre()} hasta {fecha}")
                return
 
        print("No se pudo realizar el préstamo.")
 
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
        if not self.__prestamos:
            return "No tiene préstamos."
        return [p[0].get_titulo() for p in self.__prestamos]
 
    def devolver_material(self, material: MaterialBiblioteca):
        for prestamo in self.__prestamos:
            if prestamo[0] == material:
                material.set_disponible(True)
                self.__prestamos.remove(prestamo)
                print(f"{material.get_titulo()} ha sido devuelto por {self.__nombre}.")
                return
        print(f"{self.__nombre} no tenía prestado {material.get_titulo()}.")
 
if __name__ == "__main__":
    biblioteca = Biblioteca()
 
    libro1 = Libro("El principito","Antonie")
    revista1 = Revista("Vogue", "Varias personas")
    video1 = MaterialAudiovisual("Documental Cosmos", "Carl Sagan")
 
    biblioteca.agregar_material(libro1)
    biblioteca.agregar_material(revista1)
    biblioteca.agregar_material(video1)
 
    usuario1 = Usuario("Brandon", 1)
    biblioteca.registrar_usuario(usuario1)
 
    print("\nMateriales en la Biblioteca:")
    biblioteca.mostrar_materiales()
 
    print("\nRealizando préstamo:")
    biblioteca.prestar_material("El principito",1)
 
    print("\nMateriales después del préstamo:")
    biblioteca.mostrar_materiales()
 
    print("\nPréstamos de Usuario:")
    print(usuario1.mostrar_prestamos())
 
    print("\nDevolviedo material:")
    usuario1.devolver_material(libro1)
 
    print("\nMateriales después de la devolución:")
    biblioteca.mostrar_materiales()
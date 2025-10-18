"""
EJERCICIOS PARA ESTUDIANTES - MANEJO DE EXCEPCIONES
Completa estos ejercicios mientras exploras los conceptos confusos de manejo de excepciones.
"""

# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")
print("Esta función tiene un except desnudo. Arréglalo para capturar excepciones específicas.")
print()

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    ARREGLA: Usa manejo de excepciones específico en lugar de except desnudo.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError:
        print("Error: No hay lista para calcular el promedio")
        return None
    except TypeError:
        print("Error: En la lista no hay elementos numericos.")
        return None

# El error estaba en que al usar except no se estaba expecificando de que tipo era. Entonces lo que se hizo fue agregarle
# la excepcion de una lista vacia junto con la de dar error si no hay elementos numericos.

# Prueba tu arreglo:
print(calcular_promedio([1, 2, 3, 4, 5]))  # Debería funcionar
print(calcular_promedio([]))  # Debería manejar lista vacía
print(calcular_promedio([1, 2, 'a']))  # Debería manejar error de tipo

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")
print("Este código falla silenciosamente. Añade mensajes apropiados.")
print()


def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo.
    ARREGLA: Añade manejo de excepciones Y feedback al usuario.
    """
    try:
        with open(archivo, 'w') as f:
            f.write(str(datos))
        print(f"Datos guardados correctamente en {archivo}")
        return True
    except FileNotFoundError:
        print("Error: la ruta especificada no existe.")
        return False
    except PermissionError:
        print("Error: no tienes permiso para escribir en ese archivo.")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return False

# El error aqui era que al escribir el archivo no habian excepciones por lo que se probo usando try/except para
# resolver el problema.

# Prueba tu arreglo:
guardar_datos({"usuario": "Ana"}, "datos.txt")  # Debería funcionar
guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")  # Debería informar error

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")
print("Implementa un manejo completo de archivos con else y finally.")
print()

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo.
    TODO: Implementa try-except-else-finally:
    - try: abrir y leer archivo
    - except: manejar FileNotFoundError
    - else: procesar los datos (solo si lectura exitosa)
    - finally: asegurar que el archivo se cierre
    """
    try:
        f = open(nombre_archivo, 'r')
        datos = f.read()
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    else:
        print("Archivo leído exitosamente:")
        print(datos)
    finally:
        try:
            f.close()
            print("Archivo cerrado.")
        except:
            pass

# Aqui simplemente se agrego lo que se proponia: El try-except-finally.

# Prueba tu implementación:
procesar_archivo("existente.txt")
procesar_archivo("faltante.txt")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")
print("Implementa validación con excepciones específicas.")
print()

def crear_usuario(nombre_usuario, edad, email):
    """
    Crea un nuevo usuario con validación.
    TODO: Lanza excepciones apropiadas si:
    - nombre_usuario tiene menos de 3 caracteres (ValueError)
    - edad no es un entero (TypeError)
    - edad es negativa o mayor a 150 (ValueError)
    - email no contiene '@' (ValueError)
    """
    if len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años.")
    if '@' not in email:
        raise ValueError("El email debe contener '@'.")
    print(f"Usuario {nombre_usuario} creado correctamente.")
    pass

# Lo mismo que el anterior punto, se agrego lo que se proponia, ValueError y TypeError.

# Prueba tu implementación:
crear_usuario("Ana", 25, "ana@example.com")  # Debería funcionar
crear_usuario("Ab", 25, "ana@example.com")  # Debería lanzar ValueError
crear_usuario("Ana", "25", "ana@example.com")  # Debería lanzar TypeError
crear_usuario("Ana", -5, "ana@example.com")  # Debería lanzar ValueError
crear_usuario("Ana", 25, "anaexample.com")  # Debería lanzar ValueError

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")
print("Crea excepciones personalizadas para un sistema bancario.")
print()

# TODO: Crea estas clases de excepción:
# class SaldoInsuficienteError(Exception):
#     def __init__(self, saldo, monto):
#         self.saldo = saldo
#         self.monto = monto
#         super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")

# class MontoInvalidoError(Exception):
#     pass

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente: tienes {saldo}, necesitas {monto}.")

class MontoInvalidoError(Exception):
    def __init__(self, monto):
        super().__init__(f"Monto invalido: {monto} no es un valor permitido.")

def retirar(saldo, monto):
    """
    Retira dinero de una cuenta.
    TODO: 
    - Lanza MontoInvalidoError si monto <= 0
    - Lanza SaldoInsuficienteError si monto > saldo
    - Retorna nuevo saldo si exitoso
    """
    if monto <= 0:
        raise MontoInvalidoError(monto)
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto
    pass

# Se usa init para crear el mensaje directo y se activa cuando el valor no tiene logica y ya en la funcion retirar
# se realizo lo que se pedia con los <,> y =.

# Prueba tu implementación:
print(retirar(100, 50))  # Debería funcionar
retirar(100, 150)  # Debería lanzar SaldoInsuficienteError
retirar(100, -10)  # Debería lanzar MontoInvalidoError

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")
print("Procesa una lista con manejo de errores.")
print()

def procesar_lista_numeros(lista_strings):
    """
    Convierte strings a números y los duplica.
    TODO: 
    - Intenta convertir cada elemento a int
    - Si falla, registra el error pero continúa con los demás
    - Retorna tupla (resultados_exitosos, lista_errores)
    """
    resultados = []
    errores = []
    for item in lista_strings:
        try:
            num = int(item)
            resultados.append(num * 2)
        except ValueError as e:
            errores.append((item, str(e)))
    return resultados, errores
    pass

# Los resultados guarda los numero validos para la funcion y en errores guarda los que no, luego en el try convierte
# item a entero como bien se pedia y ya si llegara a fallar se guarda el error y no se daña el ciclo.

# Prueba tu implementación:
resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])
print(f"Exitosos: {resultados}")  # [2, 4, 8]
print(f"Errores: {errores}")  # [('abc', error), ('xyz', error)]

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")
print("Registra errores pero permite que el llamador los maneje.")
print()

def operacion_critica(valor):
    """
    Realiza operación crítica con logging.
    TODO:
    - Intenta procesar valor
    - Si falla, registra el error (print)
    - Re-lanza la excepción para que el llamador pueda manejarla
    """
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error en operacion_critica: {e}")
        raise
        pass

# Basicamente se agrego lo que pedia, mostrar el error con el print y relanzarlo con raise.

# Prueba tu implementación:
print(operacion_critica("10"))  # Debería funcionar
try:
    operacion_critica("0")  # Debería registrar y re-lanzar
except ZeroDivisionError:
    print("Llamador: Manejo el error")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")
print("Maneja diferentes tipos de errores de manera diferente.")
print()

def calculadora_segura(operacion, a, b):
    """
    Realiza operaciones matemáticas con manejo de errores.
    TODO: Implementa try con múltiples except:
    - ZeroDivisionError: retorna mensaje específico
    - TypeError: retorna mensaje específico
    - ValueError: retorna mensaje específico
    """
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError("Operación no valida.")
    except ZeroDivisionError:
        return "Error: division entre cero."
    except TypeError:
        return "Error: tipos de datos invalidos."
    except ValueError as e:
        return f"Error: {e}"
    pass

# Se dio uso de todo lo aprendido y usado anteriormente para cada operacion, suma, resta ,multiplicacion y
# division. Aparte de haber agregado de nuevo el raise y los except necesario.

# Prueba tu implementación:
print(calculadora_segura("suma", 10, 5))  # 15
print(calculadora_segura("division", 10, 0))  # Maneja división por cero
print(calculadora_segura("suma", 10, "5"))  # Maneja error de tipo
print(calculadora_segura("invalida", 10, 5))  # Maneja operación inválida

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")
print("Preserva el contexto al lanzar nuevas excepciones.")
print()

def parsear_configuracion(json_string):
    """
    Parsea configuración JSON.
    TODO: 
    - Intenta parsear JSON
    - Si falla, lanza ValueError con 'from' para preservar el error original
    """
import json

def parsear_configuracion(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("Error al parsear configuracion json.") from e
    pass

# Si json.loads no puede convertir el texto da error, se vuelve a lanzar otro ValueError para preservar el error original.

# Prueba tu implementación:
print(parsear_configuracion('{"nombre": "Ana"}'))  # Debería funcionar
try:
     parsear_configuracion('json invalido')
except ValueError as e:
     print(f"Error: {e}")
     print(f"Causado por: {e.__cause__}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 10: Proyecto completo
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")
print("Crea un sistema de gestión de inventario con manejo completo de excepciones.")
print()

# TODO: Crea excepciones personalizadas
class ErrorInventario(Exception):
     pass
 
class ProductoNoEncontrado(ErrorInventario):
     pass

class StockInsuficiente(ErrorInventario):
     pass

class Inventario:
    """Sistema de inventario con manejo completo de excepciones."""
    
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, codigo, nombre, cantidad):
        """
        Añade producto al inventario.
        TODO: 
        - Validar que cantidad sea positiva (ValueError)
        - Validar que codigo no exista ya (KeyError o custom)
        """
        if cantidad <= 0:
            raise ValueError("La cantidad tiene que ser positiva.")
        if codigo in self.productos:
            raise KeyError(f"El producto con codigo {codigo} ya existe.")
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"Producto '{nombre}' agregado correctamente.")
        pass
    
    def retirar_stock(self, codigo, cantidad):
        """
        Retira cantidad de un producto.
        TODO:
        - Verificar que producto existe (ProductoNoEncontrado)
        - Verificar que hay suficiente stock (StockInsuficiente)
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"El producto {codigo} no existe.")
        if self.productos[codigo]["cantidad"] < cantidad:
            raise StockInsuficiente("No hay suficiente stock disponible.")
        self.productos[codigo]["cantidad"] -= cantidad
        print(f"Se retiraron {cantidad} unidades del producto {codigo}.")
        pass
    
    def obtener_producto(self, codigo):
        """
        Obtiene información de un producto.
        TODO:
        - Lanzar ProductoNoEncontrado si no existe
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"El producto {codigo} no existe.")
        return self.productos[codigo]
        pass

# Primero se valida la cantidad, verifica los duplicados y agrega al diccionario, luego se verifica si esta la cantidad
# disponible y lanza las excepciones depende del error que se tenga y ya por ultimo da la informacion si todo lo que se
# pidio existe o si da error.

# Prueba tu implementación:
inventario = Inventario()
inventario.agregar_producto("001", "Laptop", 10)
print(inventario.obtener_producto("001"))
inventario.retirar_stock("001", 5)
# Prueba casos de error...

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Reflexión Final
# ===========================================================================
print("\n" + "=" * 70)
print(" REFLEXIÓN")
print("=" * 70 + "\n")

print("Después de completar estos ejercicios, reflexiona:")
print()
print("1. ¿Qué tipos de excepciones usaste más frecuentemente?")
print("Respuesta1: Los mas frecuentes fueron ValueError y TypeError")
print("2. ¿Cuándo decidiste crear excepciones personalizadas?")
print("Respuesta2: Cuando en los errores se podian como modificar segun la logica de lo que se pedia")
print("3. ¿Qué patrón de manejo de excepciones te pareció más útil?")
print("Respuesta3: El de try y except")
print("4. ¿Cómo ayuda el manejo de excepciones a la experiencia del usuario?")
print("Respuesta4: Para dar un mensaje de lo que paso mal en vez de que te de un error muy grande.")
print("5. ¿Qué errores comunes evitaste con el manejo apropiado?")
print("Respuesta5: Cuando no se agrega nada al except, osea el desnudo y pues operaciones invalidas.")
print()
print("Discute tus respuestas con un compañero o con el profesor.")
print()

print("=" * 70)
print(" ¡EJERCICIOS COMPLETADOS!")
print("=" * 70)

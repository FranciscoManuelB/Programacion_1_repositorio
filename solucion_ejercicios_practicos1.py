#Ejercicios Prácticos: Operadores Lógicos
#📝 Instrucciones
#Resuelve los ejercicios en orden
#Intenta predecir el resultado antes de ejecutar el código
#Verifica tus respuestas con Python
#Si te equivocas, analiza por qué

#🟢 NIVEL 1: Básico (Operadores Fundamentales)

#Ejercicio 1.1: Predice los Resultados
# Evalúa sin ejecutar:
print(True and False)
print(True or False)
print(not True)
print(not False)
#Tu predicción: False, True, False, True
#Resultado real: False, True, False, True
#Explicación: Cuando es True and False, da False, luego cuando es True or False, devuelve True porque cuando al menos una de las 
#expresiones es verdadera devuelve True y las ultimas dos serian lo contrario a lo que piden, Not True, da False y Not False, da True.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 1.2: Operadores Combinados
a, b, c = True, False, True

print(a and b)  # ?
print(a or b)   # ?
print(b or c)   # ?
print(a and c)  # ?
#Tu predicción: False, True, True, True
#Resultado real: False, True, True, True
#Explicación: Con el (and), cuando uno es negativo sin importar el otro dara False,pero si los dos son True, dara True, al contrario 
#de (or), sí uno es positivo dara True.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 1.3: Precedencia
a, b, c = True, False, True

print(a and b or c)      # ?
print(a or b and c)      # ?
print(not a or b)        # ?
print(not (a or b))      # ?
#Tu predicción: True, True, False, False
#Resultado real: True, True, False, False
#Explicación: El and se opera antes que el or por lo que si en la ultima operacion con el or llega a haber un True, el resultado dara
#True, tambien hay que tener en cuenta que se debe realizar primero lo de dentro del parentesis.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 1.4: Comparaciones y Lógica
x = 5
print(x > 3 and x < 10)  # ?
print(x < 3 or x > 10)   # ?
print(not x > 3)         # ?
#Tu predicción: True, False, False
#Resultado real: True, False, False
#Explicación: En el primero se aplican las dos reglas correctamente x=5, 5>3 and 5<10, en el segundo tiene que haber con que sea uno
#correcto pero no lo hay, por eso da False y en el ultimo es correcto que 5>3 pero como luego pone not, se contradice y por eso da
#False.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 1.5: Comparaciones Encadenadas
x = 5
print(3 < x < 10)        # ?
print(1 <= x <= 3)       # ?
print(10 > x > 3)        # ?
#Tu predicción: True, False, True
#Resultado real: True, False, True
#Explicación: Son comparaciones encadenadas normales.

#------------------------------------------------------------------------------------------------------------------------------------

#🟡 NIVEL 2: Intermedio (Valores y Cortocircuito)
#Ejercicio 2.1: Valores Retornados
print("hola" and "mundo")  # ?
print("hola" and "")       # ?
print("" and "mundo")      # ?
print("hola" or "mundo")   # ?
print("" or "mundo")       # ?
#Tu predicción: mundo, "","", hola, mundo
#Resultado real: mundo, "","", hola, mundo
#Explicación: and evalúa el segundo operando, "" es una cadena vacía, osea es False, por lo tanto en el and retorna a False, osea "".
#En el or cuando los dos son True, devuelve el primer valor. Lo mismo que en el and, como "" es False y el otro valor con texto es
#True, devuelve el valor de True.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 2.2: Truthy y Falsy
print(bool(0))          # ?
print(bool(""))         # ?
print(bool([]))         # ?
print(bool([0]))        # ?
print(bool(" "))        # ?
print(bool(None))       # ?
#Tu predicción: False, False, False, True, True, False
#Resultado real: False, False, False, True, True, False
#Explicación: Cuando es 0,""(sin espacio) o [](sin nada) y None, retorna False, en cambio si tiene [0](con un valor dentro 
#independientemente de que sea 0) y " "(con espacio), imprime True.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 2.3: Evaluación de Cortocircuito
#Evalúa qué se imprime:

def f1():
    print("f1 ejecutada")
    return True

def f2():
    print("f2 ejecutada")
    return False

# Caso 1
print("Caso 1:")
resultado = f1() and f2()
print(f"Resultado: {resultado}")

# Caso 2
print("\nCaso 2:")
resultado = f2() and f1()
print(f"Resultado: {resultado}")

# Caso 3
print("\nCaso 3:")
resultado = f1() or f2()
print(f"Resultado: {resultado}")

#Tu predicción: Caso 1=False, Caso 2=False, Caso 3=True
#Resultado real: Caso 1:
#f1 ejecutada
#f2 ejecutada
#Resultado: False

#Caso 2:
#f2 ejecutada
#Resultado: False

#Caso 3:
#f1 ejecutada
#Resultado: True

#Explicación: En el caso 1 se ejecuta f1() y imprime "f1 ejecutada" lo que devuelve True, luego como and necesita que ambos 
#sean verdaderos, Python sí evalúa el segundo porque el primero fue True, entonces se ejecuta f2() y imprime "f2 ejecutada"
#y devuelve False, todo esto da True and False = False.

#En el caso 2 imprime "f2 ejecutada" y devuelve False, luego el operador and detiene la evaluación aquí, porque si el 
#primero es False, el resultado ya no puede ser True, sin importar el segundo valor y esto da False and (lo que sea) = False.

#En el caso 3 imprime "f1 ejecutada" y devuelve True, luego el operador or detiene la evaluación aquí, porque si el 
#primero ya es True, el resultado siempre será True, sin importar el segundo valor y esto da True or (lo que sea) = True.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 2.4: Operadores de Pertenencia
nums = [1, 2, 3, 4, 5]
print(3 in nums)        # ?
print(6 in nums)        # ?
print(6 not in nums)    # ?

word = "Python"
print("P" in word)      # ?
print("p" in word)      # ?
print("th" in word)     # ?
#Tu predicción: True, False, True, True, False, True
#Resultado real: True, False, True, True, False, True
#Explicación: Lo que hace el "in" es verificar si la variable esta dentro de la lista, entonces si esta, dara True y si no dara False.

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 2.5: Identidad vs Igualdad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # ?
print(lista1 is lista2)  # ?
print(lista1 == lista3)  # ?
print(lista1 is lista3)  # ?
#Tu predicción: True, False, True, True
#Resultado real: True, False, True, True
#Explicación: El "==" compara si las listas escogidas tiene igual contenido o si son las mismas, el "is" verifica si las 
#listas estan igualadas con "=".

#------------------------------------------------------------------------------------------------------------------------------------

#🔴 NIVEL 3: Avanzado (Aplicaciones Prácticas)
#Ejercicio 3.1: Validación de Formulario
#Implementa la función validar_datos que verifica si: 
# - El nombre tiene entre 2 y 30 caracteres - El email contiene '@' - La edad es mayor o igual a 18 
# - La contraseña tiene al menos 8 caracteres

def validar_datos(nombre, email, edad, password):
    return (
        nombre and 2 <= len(nombre) <= 30 and
        email and '@' in email and
        edad and edad >= 18 and
        password and len(password) >= 8
    )

print(validar_datos("Ana", "ana@email.com", 25, "secreto123"))
print(validar_datos("", "no-email", 15, "123"))

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 3.2: Sistema de Autorización
#Implementa un sistema que determine si un usuario puede acceder a un recurso basado en: 
# - Debe estar autenticado - Debe ser administrador O tener el permiso específico - No debe estar en la lista negra

def puede_acceder(usuario, permiso_requerido, lista_negra):
    return (
        usuario["autenticado"] and
        (usuario["admin"] or permiso_requerido in usuario["permisos"]) and
        usuario["id"] not in lista_negra
    )

admin = {
    "id": 1, "autenticado": True, "admin": True, "permisos": ["leer", "escribir"]
}
usuario_normal = {
    "id": 2, "autenticado": True, "admin": False, "permisos": ["leer"]
}
usuario_bloqueado = {
    "id": 3, "autenticado": True, "admin": False, "permisos": ["leer", "escribir"]
}
lista_negra = [3, 4]

print(puede_acceder(admin, "borrar", lista_negra))
print(puede_acceder(usuario_normal, "leer", lista_negra)) 
print(puede_acceder(usuario_normal, "escribir", lista_negra))
print(puede_acceder(usuario_bloqueado, "leer", lista_negra))

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 3.3: Acceso Seguro a Diccionario
#Implementa una función obtener_valor_seguro que retorne: 
# - El valor de la clave si existe - Un valor predeterminado si la clave no existe

def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    return diccionario[clave] if clave in diccionario else predeterminado

config = {"timeout": 30, "retries": 3}
print(obtener_valor_seguro(config, "timeout"))   
print(obtener_valor_seguro(config, "cache"))    
print(obtener_valor_seguro(config, "cache", 60))

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 3.4: Filtrar Lista
#Escribe una función para filtrar una lista de productos según criterios: 
# - Precio dentro de un rango (min y max) - Opcionalmente filtrar por categoría - Solo productos disponibles

def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    return [
        p for p in productos
        if precio_min <= p["precio"] <= precio_max and
           p["disponible"] and
           (categoria is None or p["categoria"] == categoria)
    ]

productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica", "disponible": True},
    {"nombre": "Teléfono", "precio": 800, "categoria": "Electrónica", "disponible": False},
    {"nombre": "Libro", "precio": 15, "categoria": "Libros", "disponible": True},
    {"nombre": "Audífonos", "precio": 200, "categoria": "Electrónica", "disponible": True},
]

print(filtrar_productos(productos, 0, 500))
print(filtrar_productos(productos, 100, 1000, "Electrónica"))

#------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 3.5: Evaluación de Riesgo
#Implementa un sistema de evaluación de riesgo crediticio:

def evaluar_riesgo(cliente):
    return (
        cliente["score_crediticio"] > 700 or
        (cliente["ingreso_anual"] > 50000 and cliente["años_historial"] > 2) or
        (cliente["vip"] and not cliente["deudas_pendientes"])
    )

cliente1 = {
    "nombre": "Ana García", "score_crediticio": 720, "ingreso_anual": 45000,
    "años_historial": 3, "vip": False, "deudas_pendientes": False
}
cliente2 = {
    "nombre": "Luis Pérez", "score_crediticio": 680, "ingreso_anual": 60000,
    "años_historial": 4, "vip": False, "deudas_pendientes": False
}
cliente3 = {
    "nombre": "Carmen Ruiz", "score_crediticio": 690, "ingreso_anual": 30000,
    "años_historial": 1, "vip": True, "deudas_pendientes": False
}

print(evaluar_riesgo(cliente1))
print(evaluar_riesgo(cliente2))
print(evaluar_riesgo(cliente3))

#------------------------------------------------------------------------------------------------------------------------------------

#🎯 PROYECTO FINAL: Sistema de Control de Acceso
#Descripción
#Crea un sistema de control de acceso para una plataforma digital que determine qué recursos puede ver un usuario.

#Requisitos Mínimos
#Función que verifica si un usuario puede acceder a un recurso
#Múltiples reglas de acceso
#Manejo de diferentes tipos de usuarios
#Justificación para cada decisión

usuarios = [
    {
        "id": 1,
        "nombre": "Admin",
        "roles": ["admin"],
        "permisos": ["leer", "escribir", "eliminar"],
        "plan": "premium",
        "activo": True,
        "edad": 35
    },
    {
        "id": 2,
        "nombre": "Usuario Regular",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "basico",
        "activo": True,
        "edad": 17
    },
    {
        "id": 3,
        "nombre": "Usuario Inactivo",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "premium",
        "activo": False,
        "edad": 25
    }
]

recursos = [
    {
        "id": 1,
        "nombre": "Panel Admin",
        "requiere_rol": ["admin"],
        "requiere_permiso": "eliminar",
        "solo_adultos": False
    },
    {
        "id": 2,
        "nombre": "Contenido Premium",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": True,
        "solo_adultos": False
    },
    {
        "id": 3,
        "nombre": "Contenido para Adultos",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": False,
        "solo_adultos": True
    }
]

def puede_acceder_recurso(usuario, recurso):
    """Determina si un usuario puede acceder a un recurso."""
    
    if not usuario["activo"]:
        return False
    
    if "requiere_rol" in recurso and not any(rol in recurso["requiere_rol"] for rol in usuario["roles"]):
        return False
    
    if "requiere_permiso" in recurso and recurso["requiere_permiso"] not in usuario["permisos"]:
        return False
    
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False
    
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False
    
    return True

def probar_accesos():
    for usuario in usuarios:
        for recurso in recursos:
            acceso = puede_acceder_recurso(usuario, recurso)
            print(f"Usuario: {usuario['nombre']:17} | Recurso: {recurso['nombre']:22} | Acceso: {acceso}")

probar_accesos()



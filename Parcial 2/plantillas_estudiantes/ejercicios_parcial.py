#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: Francisco Manuel Bermúdez Rodríguez
Fecha: 19/10/2025
"""

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):
    """
    Realiza operaciones matemáticas con validación.
    
    Args:
        operacion: "suma", "resta", "multiplicacion", "division", "potencia", "modulo"
        a: Primer número (int o float)
        b: Segundo número (int o float)
      
    Returns:
        float: Resultado con 2 decimales de precisión
    
    Raises:
        ValueError: Si la operación es inválida o tipos incorrectos
        ZeroDivisionError: Si intenta dividir por cero
    """
    # TODO: Implementar validaciones y operaciones

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los operandos deben ser numeros (int o float).")

    if operacion not in ["suma", "resta", "multiplicacion", "division", "potencia", "modulo"]:
        raise ValueError("operacion invalida")

    if operacion in ["division", "modulo"] and b == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")

    if operacion == "suma":
        resultado = a + b
    elif operacion == "resta":
        resultado = a - b
    elif operacion == "multiplicacion":
        resultado = a * b
    elif operacion == "division":
        resultado = a / b
    elif operacion == "potencia":
        resultado = a ** b
    else:
        resultado = a % b

    return round(resultado, 2)
    pass


# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

class ValidadorPassword:
    """Validador de contraseñas con reglas configurables."""
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        """
        Inicializa el validador con reglas específicas.
        
        Args:
            min_longitud: Longitud mínima requerida
            requiere_mayuscula: Si debe tener al menos una mayúscula
            requiere_minuscula: Si debe tener al menos una minúscula
            requiere_numero: Si debe tener al menos un número
            requiere_especial: Si debe tener al menos un carácter especial
        """
        # TODO: Inicializar atributos

        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        pass
    
    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        
        Args:
            password: Contraseña a validar
        
        Returns:
            tuple: (es_valido, lista_de_errores)
                   (True, []) si es válido
                   (False, ['error1', 'error2', ...]) si no es válido
        """
        # TODO: Implementar validaciones
        errores = []

        if len(password) < self.min_longitud:
            errores.append(f"la contraseña debe de tener {self.min_longitud} caracteres")

        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("debe de tener al menos una letra mayuscula")
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("debe de tener al menos una letra minuscula")
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("debe de tener al menos un numero")
        if self.requiere_especial and not any(not c.isalnum() for c in password):
            errores.append("debe de tener al menos un caracter especial")

        return (len(errores) == 0, errores)
        pass
    
    def es_fuerte(self, password):
        """
        Determina si el password es fuerte.
        Un password fuerte tiene al menos 12 caracteres,
        mayúsculas, minúsculas, números y caracteres especiales.
        
        Returns:
            bool: True si es fuerte, False en caso contrario
        """
        # TODO: Implementar

        return (
            len(password) >= 12
            and any(c.superior() for c in password)
            and any(c.inferior() for c in password)
            and any(c.digito() for c in password)
            and any(not c.alfanum() for c in password)
        )
        pass


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:
    """Sistema de gestión de inventario."""
    
    def __init__(self):
        """
        Inicializa el inventario.
        Estructura: {codigo: {'nombre', 'precio', 'cantidad', 'categoria'}}
        """
        # TODO: Inicializar estructuras de datos
       
        self.inventario = {}
        pass
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """
        Agrega un producto al inventario.
        
        Raises:
            ValueError: Si el código ya existe
        """
        # TODO: Implementar

        if codigo in self.inventario:
            raise ValueError("el producto con este codigo ya existe")
        self.inventario[codigo] = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad,
            'categoria': categoria
        }
        pass
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock de un producto.
        
        Args:
            cantidad_cambio: Positivo para añadir, negativo para reducir
        
        Raises:
            ValueError: Si producto no existe o stock resultante sería negativo
        """
        # TODO: Implementar

        if codigo not in self.inventario:
            raise ValueError("el producto no existe")

        nuevo_stock = self.inventario[codigo]['cantidad'] + cantidad_cambio
        if nuevo_stock < 0:
            raise ValueError("el stock no puede ser negativo")

        self.inventario[codigo]['cantidad'] = nuevo_stock
        pass
    
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Returns:
            list: Lista de tuplas (codigo, nombre, precio)
        """
        # TODO: Implementar

        resultado = []
        for codigo, datos in self.inventario.items():
            if datos['categoria'].lower() == categoria.lower():
                resultado.append((codigo, datos['nombre'], datos['precio']))
        return resultado
        pass
    
    def productos_bajo_stock(self, limite=10):
        """
        Encuentra productos con stock bajo el límite.
        
        Returns:
            dict: {codigo: cantidad} de productos bajo el límite
        """
        # TODO: Implementar

        bajos = {}
        for codigo, datos in self.inventario.items():
            if datos['cantidad'] < limite:
                bajos[codigo] = datos['cantidad']
        return bajos
        pass
    
    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Suma de (precio * cantidad) de todos los productos
        """
        # TODO: Implementar

        total = 0
        for datos in self.inventario.values():
            total += datos['precio'] * datos['cantidad']
        return round(total, 2)
        pass
    
    def top_productos(self, n=5):
        """
        Retorna los N productos con mayor valor en inventario.
        
        Returns:
            list: Lista de tuplas (codigo, valor_total) ordenadas descendentemente
        """
        # TODO: Implementar

        valores = []
        for codigo, datos in self.inventario.items():
            valor = datos['precio'] * datos['cantidad']
            valores.append((codigo, round(valor, 2)))

        valores.sort(key=lambda x: x[1], reverse=True)
        return valores[:n]
        pass


# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si divisible por 100: no bisiesto
    - EXCEPTO si divisible por 400: bisiesto
    
    Returns:
        bool: True si es bisiesto, False en caso contrario
    """
    # TODO: Implementar

    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
    pass


def dias_en_mes(mes, anio):
    """
    Retorna el número de días en un mes específico.
    
    Args:
        mes: Número del mes (1-12)
        anio: Año (considera bisiestos)
    
    Returns:
        int: Número de días en el mes
    
    Raises:
        ValueError: Si mes es inválido (no está entre 1 y 12)
    """
    # TODO: Implementar

    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12.")
    
    dias_por_mes = {
        1: 31,
        2: 29 if es_bisiesto(anio) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return dias_por_mes[mes]
    pass


def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera representación string del calendario de un mes.
    
    Args:
        mes: Mes (1-12)
        anio: Año
        dia_inicio: Día de la semana del primer día (0=Lunes, 6=Domingo)
    
    Returns:
        str: Calendario formateado
        
    Formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    # TODO: Implementar

    dias_semana = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"]
    dias_mes = dias_en_mes(mes, anio)

    calendario = " ".join(dias_semana) + "\n"
    
    calendario += "   " * dia_inicio
    
    dia_actual = 1
    for i in range(dia_inicio, dia_inicio + dias_mes):
        calendario += f"{dia_actual:2d} "
        if (i + 1) % 7 == 0:
            calendario += "\n"
        dia_actual += 1

    return calendario.strip()
    pass


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    """
    Analiza lista de ventas y genera estadísticas.
    
    Args:
        ventas: Lista de dicts con 'producto', 'cantidad', 'precio', 'descuento'
    
    Returns:
        dict: {
            'total_ventas': float,
            'promedio_por_venta': float,
            'producto_mas_vendido': str,
            'venta_mayor': dict,
            'total_descuentos': float
        }
    """
    # TODO: Implementar

    if not ventas:
        return {
            'total_ventas': 0.0,
            'promedio_por_venta': 0.0,
            'producto_mas_vendido': None,
            'venta_mayor': None,
            'total_descuentos': 0.0
        }
    
    total_ventas = 0
    total_descuentos = 0
    productos = {}
    venta_mayor = None
    max_total = 0

    for venta in ventas:
        subtotal = venta['cantidad'] * venta['precio']
        descuento = subtotal * (venta['descuento'] / 100)
        total = subtotal - descuento
        
        total_ventas += total
        total_descuentos += descuento
        
        productos[venta['producto']] = productos.get(venta['producto'], 0) + venta['cantidad']
        
        if total > max_total:
            max_total = total
            venta_mayor = venta

    producto_mas_vendido = max(productos, key=productos.get)
    promedio = total_ventas / len(ventas)

    return {
        'total_ventas': round(total_ventas, 2),
        'promedio_por_venta': round(promedio, 2),
        'producto_mas_vendido': producto_mas_vendido,
        'venta_mayor': venta_mayor,
        'total_descuentos': round(total_descuentos, 2)
    }
    pass


def encontrar_patrones(numeros):
    """
    Encuentra patrones en una secuencia de números.
    
    Returns:
        dict: {
            'secuencias_ascendentes': int,
            'secuencias_descendentes': int,
            'longitud_max_ascendente': int,
            'longitud_max_descendente': int,
            'numeros_repetidos': dict
        }
    """
    # TODO: Implementar

    if not numeros:
        return {
            'secuencias_ascendentes': 0,
            'secuencias_descendentes': 0,
            'longitud_max_ascendente': 0,
            'longitud_max_descendente': 0,
            'numeros_repetidos': {}
        }
    
    asc = desc = 0
    max_asc = max_desc = 1
    actual_asc = actual_desc = 1
    repetidos = {}

    for num in numeros:
        repetidos[num] = repetidos.get(num, 0) + 1

    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i-1]:
            actual_asc += 1
            actual_desc = 1
        elif numeros[i] < numeros[i-1]:
            actual_desc += 1
            actual_asc = 1
        else:
            actual_asc = actual_desc = 1
        
        max_asc = max(max_asc, actual_asc)
        max_desc = max(max_desc, actual_desc)

    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i-1]:
            asc += 1
        elif numeros[i] < numeros[i-1]:
            desc += 1

    numeros_repetidos = {k: v for k, v in repetidos.items() if v > 1}

    return {
        'secuencias_ascendentes': asc,
        'secuencias_descendentes': desc,
        'longitud_max_ascendente': max_asc,
        'longitud_max_descendente': max_desc,
        'numeros_repetidos': numeros_repetidos
    }
    pass


def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    
    Args:
        principal: Monto inicial
        tasa_anual: Tasa de interés (0.05 para 5%)
        anios: Número de años
        aporte_anual: Aporte adicional al inicio de cada año
    
    Returns:
        list: Lista de dicts con 'anio', 'balance', 'interes_ganado'
    """
    # TODO: Implementar

    resultados = []
    balance = principal

    for anio in range(1, anios + 1):
        balance += aporte_anual
        interes = balance * tasa_anual
        balance += interes
        resultados.append({
            'anio': anio,
            'balance': round(balance, 2),
            'interes_ganado': round(interes, 2)
        })

    return resultados
    pass


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)
    
    # Aquí puedes añadir tus propias pruebas
    
    print("\nEjercicio 1: Calculadora")
    # TODO: Pruebas
    print(calculadora_cientifica("suma", 3, 9))
    print(calculadora_cientifica("resta", 15, 4.5))
    print(calculadora_cientifica("multiplicacion", 5, 5))
    print(calculadora_cientifica("division", 20, 10))
    print(calculadora_cientifica("potencia", 2, 5))
    print(calculadora_cientifica("modulo", 10, 3))

    
    print("\nEjercicio 2: Validador de Password")
    # TODO: Pruebas
    v = ValidadorPassword()
    print(v.validar("Abc123!"))       
    print(v.es_fuerte("Abc123!@#$Xyz"))
    
    print("\nEjercicio 3: Gestor de Inventario")
    # TODO: Pruebas
    inventario = GestorInventario()
    inventario.agregar_producto("A1", "Laptop", 3000, 5, "Tecnología")
    inventario.agregar_producto("B2", "Mouse", 50, 20, "Tecnología")
    inventario.agregar_producto("C3", "Camiseta", 25, 8, "Ropa")
    inventario.actualizar_stock("B2", -5)
    print(inventario.buscar_por_categoria("tecnología"))
    print(inventario.productos_bajo_stock(10))
    print(inventario.valor_total_inventario())
    print(inventario.top_productos(2))
    
    print("\nEjercicio 4: Calendario")
    # TODO: Pruebas
    print(es_bisiesto(2024))
    print(es_bisiesto(1900))
    print(dias_en_mes(2, 2024))
    print(generar_calendario(10, 2025, dia_inicio=2))
    
    print("\nEjercicio 5: Análisis de Datos")
    # TODO: Pruebas
    ventas = [
    {'producto': 'Laptop', 'cantidad': 2, 'precio': 3000, 'descuento': 10},
    {'producto': 'Mouse', 'cantidad': 5, 'precio': 50, 'descuento': 0},
    {'producto': 'Laptop', 'cantidad': 1, 'precio': 3000, 'descuento': 5},
    ]
    print("")
    print(analizar_ventas(ventas))
    print("")
    numeros = [1, 2, 3, 2, 1, 1, 3, 4, 5, 2]
    print(encontrar_patrones(numeros))
    print("")
    print(simular_crecimiento(1000, 0.05, 5, 500))
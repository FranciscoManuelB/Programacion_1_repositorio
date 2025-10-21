#!/usr/bin/env python3
"""
PROBLEMA INTEGRADOR DE PRÁCTICA
Sistema de Gestión de Restaurante

Nombre: Francisco Manuel Bermúdez Rodríguez
Fecha: 19/10/2025
"""

from datetime import datetime, time

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================

class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass


class PlatoNoEncontrado(ErrorRestaurante):
    """Se lanza cuando un plato no existe en el menú."""
    def __init__(self, codigo_plato):
        self.codigo_plato = codigo_plato
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")


class MesaNoDisponible(ErrorRestaurante):
    """Se lanza cuando la mesa está ocupada."""
    # TODO: Implementar __init__ con atributos numero_mesa y hora_disponible

    def __init__(self, numero_mesa, hora_disponible):
        self.numero_mesa = numero_mesa
        self.hora_disponible = hora_disponible
        super().__init__(f"la mesa {numero_mesa} esta ocupada y estara disponible a las {hora_disponible}")
    pass


class CapacidadExcedida(ErrorRestaurante):
    """Se lanza cuando hay más comensales que capacidad."""
    # TODO: Implementar __init__ con atributos numero_mesa, capacidad y comensales
    
    def __init__(self, numero_mesa, capacidad, comensales):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.comensales = comensales
        super().__init__(
            f"la mesa {numero_mesa} tiene capacidad para {capacidad} personas, "
            f"pero se intentaron sentar {comensales}."
        )
    pass


class PedidoInvalido(ErrorRestaurante):
    """Se lanza para pedidos con problemas."""
    # TODO: Implementar __init__ con atributo razon

    def __init__(self, razon):
        self.razon = razon
        super().__init__(f"pedido invalido: {razon}")
    pass


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA RESTAURANTE
# ===========================================================================

class SistemaRestaurante:
    """Sistema completo de gestión de restaurante."""
    
    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        """
        Inicializa el sistema.
        
        Args:
            num_mesas: Número total de mesas
            tasa_impuesto: Tasa de impuesto (IVA)
            propina_sugerida: Propina sugerida por defecto
        """
        # TODO: Inicializar estructuras de datos

        # Estructuras principales del sistema
        self.mesas = {i: {"disponible": True, "capacidad": 4, "pedido": None, "hora_disponible": None} for i in range(1, num_mesas + 1)}
        self.menu = {}
        self.tasa_impuesto = tasa_impuesto
        self.propina_sugerida = propina_sugerida
        self.pedidos = {}
        self.contador_pedidos = 1
    
    # ============ GESTIÓN DE MENÚ ============
    
    def agregar_plato(self, codigo, nombre, categoria, precio):
        """
        Agrega un plato al menú.
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si código ya existe
        """
        # TODO: Implementar con validaciones

        if not codigo or not nombre or not categoria:
            raise ValueError("codigo, nombre y categoria son obligatorios")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("el precio debe ser un numero positivo")
        if codigo in self.menu:
            raise KeyError(f"el plato con codigo '{codigo}' ya existe")
        
        self.menu[codigo] = {"nombre": nombre, "categoria": categoria, "precio": precio, "disponible": True}
        pass
    
    def cambiar_disponibilidad(self, codigo, disponible):
        """
        Cambia disponibilidad de un plato.
        
        Raises:
            PlatoNoEncontrado: Si código no existe
        """
        # TODO: Implementar

        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        self.menu[codigo]["disponible"] = bool(disponible)
        pass
    
    def buscar_platos(self, categoria=None, precio_max=None):
        """
        Busca platos por criterios.
        
        Returns:
            Lista de diccionarios con info de platos disponibles
        """
        # TODO: Implementar búsqueda con filtros

        resultados = []
        for codigo, plato in self.menu.items():
            if not plato["disponible"]:
                continue
            if categoria and plato["categoria"].lower() != categoria.lower():
                continue
            if precio_max and plato["precio"] > precio_max:
                continue
            resultados.append({"codigo": codigo, **plato})
        return resultados
        pass
    
    # ============ GESTIÓN DE MESAS ============
    
    def configurar_mesa(self, numero, capacidad):
        """
        Configura capacidad de una mesa.
        
        Raises:
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar con validaciones

        if numero not in self.mesas:
            raise ValueError("numero de mesa invalido")
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("la capacidad debe ser un numero entero positivo")
        self.mesas[numero]["capacidad"] = capacidad
        pass
    
    def reservar_mesa(self, numero, comensales, hora):
        """
        Reserva una mesa.
        
        Raises:
            MesaNoDisponible: Si mesa ocupada
            CapacidadExcedida: Si comensales > capacidad
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar con validaciones

        if numero not in self.mesas:
            raise ValueError("la mesa no existe")
        mesa = self.mesas[numero]
        if not mesa["disponible"]:
            raise MesaNoDisponible(numero, mesa["hora_disponible"])
        if comensales > mesa["capacidad"]:
            raise CapacidadExcedida(numero, mesa["capacidad"], comensales)
        
        mesa["disponible"] = False
        mesa["hora_disponible"] = hora
        pass
    
    def liberar_mesa(self, numero):
        """
        Libera una mesa (termina servicio).
        
        Raises:
            ValueError: Si mesa no existe o no está ocupada
        """
        # TODO: Implementar

        if numero not in self.mesas:
            raise ValueError("la mesa no existe")
        mesa = self.mesas[numero]
        if mesa["disponible"]:
            raise ValueError("la mesa ya esta libre")
        
        mesa["disponible"] = True
        mesa["pedido"] = None
        mesa["hora_disponible"] = None
        pass
    
    def mesas_disponibles(self, comensales):
        """
        Lista mesas disponibles para N comensales.
        
        Returns:
            Lista de números de mesa
        """
        # TODO: Implementar filtrado

        disponibles = []
        for numero, mesa in self.mesas.items():
            if mesa["disponible"] and mesa["capacidad"] >= comensales:
                disponibles.append(numero)
        return disponibles
        pass
    
    # ============ GESTIÓN DE PEDIDOS ============
    
    def crear_pedido(self, numero_mesa):
        """
        Crea un nuevo pedido para una mesa.
        
        Returns:
            id_pedido: ID único del pedido
        
        Raises:
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar creación de pedido

        if numero_mesa not in self.mesas:
            raise ValueError("la mesa no existe")
        mesa = self.mesas[numero_mesa]
        if mesa["disponible"]:
            raise ValueError("la mesa debe estar reservada para crear un pedido")
        
        id_pedido = self.contador_pedidos
        self.pedidos[id_pedido] = {"mesa": numero_mesa, "items": [], "pagado": False}
        self.contador_pedidos += 1
        mesa["pedido"] = id_pedido
        return id_pedido
        pass
    
    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        """
        Agrega items al pedido.
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
            PlatoNoEncontrado: Si plato no existe
            ValueError: Si plato no disponible
        """
        # TODO: Implementar con validaciones
        
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("el pedido no existe")
        pedido = self.pedidos[id_pedido]
        if pedido["pagado"]:
            raise PedidoInvalido("el pedido ya fue pagado")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        plato = self.menu[codigo_plato]
        if not plato["disponible"]:
            raise ValueError(f"el plato '{plato['nombre']}' no esta disponible")
        
        pedido["items"].append({"codigo": codigo_plato, "nombre": plato["nombre"], "precio": plato["precio"], "cantidad": cantidad})
        pass
    
    def calcular_total(self, id_pedido, propina_porcentaje=None):
        """
        Calcula total del pedido.
        
        Returns:
            dict con subtotal, impuesto, propina, total
        """
        # TODO: Implementar cálculos

        if id_pedido not in self.pedidos:
            raise PedidoInvalido("el pedido no existe")
        
        pedido = self.pedidos[id_pedido]
        subtotal = sum(item["precio"] * item["cantidad"] for item in pedido["items"])
        impuesto = subtotal * self.tasa_impuesto
        if propina_porcentaje is None:
            propina_porcentaje = self.propina_sugerida
        propina = subtotal * propina_porcentaje
        total = subtotal + impuesto + propina
        return {
            "subtotal": subtotal,
            "impuesto": impuesto,
            "propina": propina,
            "total": total
        }

        pass
    
    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        """
        Procesa pago del pedido.
        
        Returns:
            dict con totales
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
        """
        # TODO: Implementar procesamiento de pago

        if id_pedido not in self.pedidos:
            raise PedidoInvalido("el pedido no existe")
        
        pedido = self.pedidos[id_pedido]
        if pedido["pagado"]:
            raise PedidoInvalido("el pedido ya fue pagado")
        
        totales = self.calcular_total(id_pedido, propina_porcentaje)
        pedido["pagado"] = True
        
        numero_mesa = pedido["mesa"]
        self.liberar_mesa(numero_mesa)
        
        return totales
        pass
    
    # ============ REPORTES Y ESTADÍSTICAS ============
    
    def platos_mas_vendidos(self, n=5):
        """
        Retorna los N platos más vendidos del día.
        
        Returns:
            Lista de tuplas (codigo, nombre, cantidad_vendida)
        """
        # TODO: Implementar conteo y ordenamiento

        ventas = {}
        for pedido in self.pedidos.values():
            for item in pedido["items"]:
                codigo = item["codigo"]
                ventas[codigo] = ventas.get(codigo, 0) + item["cantidad"]
        
        ranking = sorted(ventas.items(), key=lambda x: x[1], reverse=True)[:n]
        
        resultado = []
        for codigo, cantidad in ranking:
            nombre = self.menu[codigo]["nombre"]
            resultado.append((codigo, nombre, cantidad))
        
        return resultado
        pass
    
    def ventas_por_categoria(self):
        """
        Calcula ventas totales por categoría.
        
        Returns:
            dict con ventas por categoría
        """
        # TODO: Implementar agrupación

        ventas_cat = {}
        for pedido in self.pedidos.values():
            for item in pedido["items"]:
                codigo = item["codigo"]
                categoria = self.menu[codigo]["categoria"]
                subtotal = item["precio"] * item["cantidad"]
                ventas_cat[categoria] = ventas_cat.get(categoria, 0) + subtotal
        return ventas_cat
        pass
    
    def reporte_ventas_dia(self):
        """
        Genera reporte completo de ventas del día.
        
        Returns:
            dict con estadísticas completas
        """
        # TODO: Implementar reporte completo

        total_ventas = 0
        total_propinas = 0
        total_impuestos = 0
        total_pedidos = 0
        
        for pedido in self.pedidos.values():
            if pedido["pagado"]:
                total_pedidos += 1
                totales = self.calcular_total(pedido["id"], pedido["propina"])
                total_ventas += totales["subtotal"]
                total_impuestos += totales["impuesto"]
                total_propinas += totales["propina"]
        
        return {
            "pedidos_pagados": total_pedidos,
            "ventas_totales": total_ventas,
            "impuestos_totales": total_impuestos,
            "propinas_totales": total_propinas,
            "platos_mas_vendidos": self.platos_mas_vendidos(),
            "ventas_por_categoria": self.ventas_por_categoria()
        }
        pass
    
    def estado_restaurante(self):
        """
        Estado actual del restaurante.
        
        Returns:
            dict con estado de mesas y pedidos
        """
        # TODO: Implementar resumen de estado

        mesas_libres = [n for n, m in self.mesas.items() if not m["ocupada"]]
        mesas_ocupadas = [n for n, m in self.mesas.items() if m["ocupada"]]
        pedidos_activos = [p["id"] for p in self.pedidos.values() if not p["pagado"]]
        
        return {
            "mesas_libres": mesas_libres,
            "mesas_ocupadas": mesas_ocupadas,
            "pedidos_activos": pedidos_activos,
            "total_mesas": len(self.mesas)
        }
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_menu(self, archivo='menu.txt'):
        """
        Exporta menú a archivo de texto.
        Formato: Codigo|Nombre|Categoria|Precio|Disponible
        """
        # TODO: Implementar exportación

        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for codigo, plato in self.menu.items():
                    linea = f"{codigo}|{plato['nombre']}|{plato['categoria']}|{plato['precio']}|{plato['disponible']}\n"
                    f.write(linea)
            return f"menu exportado correctamente a {archivo}"
        except Exception as e:
            return f"error: {e}"
        pass
    
    def importar_menu(self, archivo='menu.txt'):
        """
        Importa menú desde archivo de texto.
        
        Returns:
            dict con exitosos y errores
        """
        # TODO: Implementar importación con manejo de errores

        exitosos = 0
        errores = []

        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f, start=1):
                    try:
                        codigo, nombre, categoria, precio, disponible = linea.strip().split('|')
                        if codigo in self.menu:
                            raise ValueError("codigo duplicado")
                        self.menu[codigo] = {
                            "nombre": nombre,
                            "categoria": categoria,
                            "precio": float(precio),
                            "disponible": disponible == "True"
                        }
                        exitosos += 1
                    except Exception as e:
                        errores.append((i, str(e)))
        except FileNotFoundError:
            return {"exitosos": 0, "errores": [(0, "archivo no encontrado")]}
        
        return {"exitosos": exitosos, "errores": errores}
        pass


# ===========================================================================
# EJEMPLO DE USO
# ===========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("=" * 70)
    
    # Crear sistema
    restaurante = SistemaRestaurante(num_mesas=5)

    # Agregar platos
    restaurante.agregar_plato("P01", "hamburguesa Clasica", "comida rapida", 18000)
    restaurante.agregar_plato("P02", "pizza margarita", "italiana", 22000)
    restaurante.agregar_plato("P03", "limonada natural", "bebidas", 7000)

    # Configurar mesas
    restaurante.configurar_mesa(1, 4)
    restaurante.configurar_mesa(2, 2)
    restaurante.configurar_mesa(3, 6)

    # Reservar mesa y crear pedido
    restaurante.reservar_mesa(1, 3, "12:30")
    id_pedido = restaurante.crear_pedido(1)
    restaurante.agregar_item(id_pedido, "P01", 2)
    restaurante.agregar_item(id_pedido, "P03", 3)

    # Calcular total
    totales = restaurante.calcular_total(id_pedido)
    print("\nresumen del pedido:", totales)

    # Pagar pedido
    resultado_pago = restaurante.pagar_pedido(id_pedido)
    print("pago realizado:", resultado_pago)

    # Estado actual
    print("\nestado del restaurante:")
    print(restaurante.estado_restaurante())

    # Exportar e importar menú
    print("\nexportando menu:")
    print(restaurante.exportar_menu())
    print("\nimportando menu:")
    print(restaurante.importar_menu())
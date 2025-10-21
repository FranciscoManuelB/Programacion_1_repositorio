"""
PARCIAL 2 - CASOS DE PRUEBA
Sistema de Gestión de Restaurante

Estudiante: Francisco Manuel Bermúdez Rodríguez
Fecha: 20/10/2025
"""

from sistema_restaurante import *

def prueba_agregar_platos():
    """Prueba agregar platos al menu."""
    print("\n" + "="*60)
    print(" TEST: Agregar Platos al Menu")
    print("="*60)
    
    restaurante = SistemaRestaurante()

    # Agregar plato valido
    restaurante.agregar_plato("P01", "Hamburguesa", "Comida Rapida", 25000)
    assert "P01" in restaurante.menu
    
    # Intentar agregar plato duplicado
    try:
        restaurante.agregar_plato("P01", "Hamburguesa Doble", "Comida Rapida", 30000)
    except KeyError:
        print("Excepcion por duplicado detectada correctamente")

    # Agregar plato con precio invalido
    try:
        restaurante.agregar_plato("P02", "Agua", "Bebida", -1000)
    except ValueError:
        print("Excepcion por precio invalido detectada")

    print("Prueba completada")


def prueba_cambiar_disponibilidad():
    """Prueba cambiar disponibilidad de platos."""
    print("\n" + "="*60)
    print(" TEST: Cambiar Disponibilidad de Platos")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.agregar_plato("P01", "Pizza", "Italiana", 32000)

    # Cambiar disponibilidad correctamente
    restaurante.cambiar_disponibilidad("P01", False)
    assert not restaurante.menu["P01"]["disponible"]

    # Intentar cambiar disponibilidad de plato inexistente
    try:
        restaurante.cambiar_disponibilidad("P99", True)
    except PlatoNoEncontrado:
        print("Plato inexistente detectado correctamente")

    print("Prueba completada")


def prueba_buscar_platos():
    """Prueba busqueda de platos."""
    print("\n" + "="*60)
    print(" TEST: Buscar Platos")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.agregar_plato("P01", "Hamburguesa", "Rapida", 25000)
    restaurante.agregar_plato("P02", "Jugo", "Bebida", 8000)
    restaurante.agregar_plato("P03", "Pasta", "Italiana", 28000)

    # Busqueda por categoria
    resultados = restaurante.buscar_platos(categoria="Bebida")
    assert len(resultados) == 1

    # Busqueda por precio maximo
    baratos = restaurante.buscar_platos(precio_max=10000)
    assert len(baratos) == 1

    print("Prueba completada")


def prueba_configurar_y_reservar_mesas():
    """Prueba configuracion y reserva de mesas."""
    print("\n" + "="*60)
    print(" TEST: Configurar y Reservar Mesas")
    print("="*60)
    
    restaurante = SistemaRestaurante()

    # Configurar mesa valida
    restaurante.configurar_mesa(1, 4)

    # Reservar mesa disponible
    restaurante.reservar_mesa(1, 2, "19:00")

    # Intentar reservar mesa ocupada
    try:
        restaurante.reservar_mesa(1, 2, "20:00")
    except MesaNoDisponible:
        print("Mesa ocupada detectada correctamente")

    # Intentar reservar con comensales mayores a la capacidad
    restaurante.configurar_mesa(2, 2)
    try:
        restaurante.reservar_mesa(2, 5, "18:00")
    except CapacidadExcedida:
        print("Capacidad excedida detectada correctamente")

    print("Prueba completada")


def prueba_liberar_y_listar_mesas():
    """Prueba liberacion y listado de mesas disponibles."""
    print("\n" + "="*60)
    print(" TEST: Liberar y Listar Mesas")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.configurar_mesa(1, 4)
    restaurante.reservar_mesa(1, 2, "19:00")

    # Liberar una mesa ocupada
    restaurante.liberar_mesa(1)
    assert not restaurante.mesas[1]["ocupada"]

    # Intentar liberar una mesa inexistente
    try:
        restaurante.liberar_mesa(99)
    except ValueError:
        print("Mesa inexistente detectada correctamente")

    # Listar mesas disponibles
    disponibles = restaurante.mesas_disponibles(2)
    assert isinstance(disponibles, list)

    print("Prueba completada")


def prueba_crear_y_agregar_pedidos():
    """Prueba creacion y agregado de pedidos."""
    print("\n" + "="*60)
    print(" TEST: Crear y Agregar Pedidos")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.configurar_mesa(1, 4)
    restaurante.reservar_mesa(1, 3, "18:00")
    restaurante.agregar_plato("P01", "Hamburguesa", "Comida Rapida", 25000)

    id_pedido = restaurante.crear_pedido(1)
    restaurante.agregar_item(id_pedido, "P01", 2)

    # Intentar agregar plato inexistente
    try:
        restaurante.agregar_item(id_pedido, "P99", 1)
    except PlatoNoEncontrado:
        print("Plato inexistente detectado correctamente")

    print("Prueba completada")


def prueba_calcular_y_pagar():
    """Prueba calculo de totales y pago."""
    print("\n" + "="*60)
    print(" TEST: Calcular Total y Procesar Pago")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.configurar_mesa(1, 4)
    restaurante.reservar_mesa(1, 3, "19:00")
    restaurante.agregar_plato("P01", "Pizza", "Italiana", 30000)

    pedido = restaurante.crear_pedido(1)
    restaurante.agregar_item(pedido, "P01", 2)

    totales = restaurante.calcular_total(pedido)
    assert "total" in totales

    pagado = restaurante.pagar_pedido(pedido)
    assert pagado["total"] >= 0

    print("Prueba completada")


def prueba_reportes_y_estadisticas():
    """Prueba reportes y estadisticas del restaurante."""
    print("\n" + "="*60)
    print(" TEST: Reportes y Estadisticas")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.agregar_plato("P01", "Sopa", "Entrada", 12000)
    restaurante.agregar_plato("P02", "Carne", "Fuerte", 30000)
    restaurante.configurar_mesa(1, 4)
    restaurante.reservar_mesa(1, 2, "13:00")

    pedido = restaurante.crear_pedido(1)
    restaurante.agregar_item(pedido, "P01", 1)
    restaurante.agregar_item(pedido, "P02", 1)
    restaurante.pagar_pedido(pedido)

    # Platos mas vendidos
    top = restaurante.platos_mas_vendidos()
    assert isinstance(top, list)

    # Ventas por categoria
    ventas = restaurante.ventas_por_categoria()
    assert isinstance(ventas, dict)

    # Reporte diario
    reporte = restaurante.reporte_ventas_dia()
    assert isinstance(reporte, dict)

    print("Prueba completada")


def prueba_excepciones_personalizadas():
    """Prueba manejo de excepciones personalizadas."""
    print("\n" + "="*60)
    print(" TEST: Excepciones Personalizadas")
    print("="*60)
    
    restaurante = SistemaRestaurante()

    try:
        raise PlatoNoEncontrado("P99")
    except PlatoNoEncontrado:
        print("Excepcion PlatoNoEncontrado detectada")

    try:
        raise MesaNoDisponible(5, "20:00")
    except MesaNoDisponible:
        print("Excepcion MesaNoDisponible detectada")

    try:
        raise CapacidadExcedida(1, 4, 6)
    except CapacidadExcedida:
        print("Excepcion CapacidadExcedida detectada")

    try:
        raise PedidoInvalido("Pedido no existe")
    except PedidoInvalido:
        print("Excepcion PedidoInvalido detectada")

    print("Prueba completada")


def prueba_importar_y_exportar_menu():
    """Prueba importar/exportar menu."""
    print("\n" + "="*60)
    print(" TEST: Importar y Exportar Menu")
    print("="*60)
    
    restaurante = SistemaRestaurante()
    restaurante.agregar_plato("P01", "Limonada", "Bebida", 6000)
    restaurante.exportar_menu("menu_test.txt")

    nuevo_restaurante = SistemaRestaurante()
    resultado = nuevo_restaurante.importar_menu("menu_test.txt")
    assert "exitosos" in resultado

    print("Prueba completada")


# ===================================================================
# EJECUTAR TODAS LAS PRUEBAS
# ===================================================================

def ejecutar_todas_las_pruebas():
    """Ejecuta toda la suite de pruebas."""
    print("\n" + "="*70)
    print(" EJECUTANDO SUITE COMPLETA DE PRUEBAS DEL RESTAURANTE")
    print("="*70)
    
    pruebas = [
        prueba_agregar_platos,
        prueba_cambiar_disponibilidad,
        prueba_buscar_platos,
        prueba_configurar_y_reservar_mesas,
        prueba_liberar_y_listar_mesas,
        prueba_crear_y_agregar_pedidos,
        prueba_calcular_y_pagar,
        prueba_reportes_y_estadisticas,
        prueba_excepciones_personalizadas,
        prueba_importar_y_exportar_menu
    ]
    
    exitosas = 0
    fallidas = 0
    
    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except Exception as e:
            print(f"Error en {prueba.__name__}: {e}")
            fallidas += 1
    
    print("\n" + "="*70)
    print(" RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"✓ Exitosas: {exitosas}/{len(pruebas)}")
    print(f"✗ Fallidas: {fallidas}/{len(pruebas)}")
    print("="*70)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()

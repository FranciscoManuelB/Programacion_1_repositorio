#!/usr/bin/env python3
"""
PARCIAL 2 - CASOS DE PRUEBA
Sistema de Biblioteca Digital

Estudiante: Francisco Manuel Bermúdez Rodríguez
Fecha: 20/10/2025
"""

from sistema_biblioteca import *
from datetime import datetime, timedelta

def prueba_agregar_libros():
    """Prueba agregar libros al catálogo."""
    print("\n" + "="*60)
    print(" TEST: Agregar Libros")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Agregar libro válido
    biblioteca.agregar_libro("9781234567890", "El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción", 3)
    assert "9781234567890" in biblioteca.catalogo
    # - Intentar agregar libro duplicado
    try:
        biblioteca.agregar_libro("9781234567890", "Duplicado", "Autor", 2000, "Drama", 1)
    except KeyError:
        print("Capturado duplicado correctamente")
    # - Agregar libro con ISBN inválido
    try:
        biblioteca.agregar_libro("123", "Libro Inválido", "Autor", 2020, "Educativo", 2)
    except ValueError:
        print("ISBN invalido detectado")
    # - Agregar libro con año inválido
    try:
        biblioteca.agregar_libro("9789876543210", "Libro Futuro", "Autor X", 3000, "Ficción", 2)
    except ValueError:
        print("Año invalido detectado")

    print("Prueba completada")

def prueba_registrar_usuarios():
    """Prueba registro de usuarios."""
    print("\n" + "="*60)
    print(" TEST: Registrar Usuarios")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Registrar usuario válido
    biblioteca.registrar_usuario("u001", "Juan Perez", "juan@example.com")
    assert "u001" in biblioteca.usuarios
    # - Intentar registrar usuario duplicado
    try:
        biblioteca.registrar_usuario("u001", "Juan Perez", "juan@example.com")
    except KeyError:
        print("Usuario duplicado detectado")
    # - Registrar con email inválido
    try:
        biblioteca.registrar_usuario("u002", "Ana Lopez", "anaemail")
    except ValueError:
        print("Email invalido detectado")
    
    print("Prueba completada")


def prueba_prestar_libros():
    """Prueba sistema de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Préstamos")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(limite_prestamos=3)
    biblioteca.agregar_libro("9781111111111", "Cien Años de Soledad", "García Márquez", 1967, "Novela", 1)
    biblioteca.registrar_usuario("u001", "Mario Vargas", "mario@example.com")
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Préstamo exitoso
    id_prestamo = biblioteca.prestar_libro("9781111111111", "u001")
    assert id_prestamo in biblioteca.prestamos
    # - Intentar prestar libro no disponible
    try:
        biblioteca.prestar_libro("9781111111111", "u001")
    except LibroNoDisponible:
        print("No hay copias disponibles detectado")
    # - Exceder límite de préstamos
    biblioteca.agregar_libro("9782222222222", "Rayuela", "Cortázar", 1963, "Ficción", 1)
    try:
        biblioteca.prestar_libro("9782222222222", "u001")
    except LimitePrestamosExcedido:
        print("Limite de prestamos detectado")
    # - Préstamo con usuario no registrado
    try:
        biblioteca.prestar_libro("9782222222222", "u999")
    except UsuarioNoRegistrado:
        print("Usuario no registrado detectado")
    
    print("Prueba completada")


def prueba_devolver_libros():
    """Prueba devolución y cálculo de multas."""
    print("\n" + "="*60)
    print(" TEST: Devolución y Multas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(multa_por_dia=2.0)
    biblioteca.agregar_libro("9781111111111", "Fahrenheit 451", "Bradbury", 1953, "Ciencia ficcion", 1)
    biblioteca.registrar_usuario("u001", "Luis", "luis@example.com")

    id_prestamo = biblioteca.prestar_libro("9781111111111", "u001")
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Devolución a tiempo (sin multa)
    resultado = biblioteca.devolver_libro(id_prestamo)
    assert resultado["multa"] == 0
    print("Devolucion a tiempo sin multa OK")
    # - Devolución con retraso (con multa)
    id_prestamo2 = biblioteca.prestar_libro("9781111111111", "u001")
    biblioteca.prestamos[id_prestamo2]["fecha_vencimiento"] = datetime.now() - timedelta(days=3)
    resultado2 = biblioteca.devolver_libro(id_prestamo2)
    assert resultado2["multa"] > 0
    print("Devolucion con retraso y multa OK")
    # - Intentar devolver préstamo inexistente
    try:
        biblioteca.devolver_libro("P9999")
    except KeyError:
        print("Intento de devolucion de prestamo inexistente correctamente detectado")

    
    print("Prueba completada")


def prueba_buscar_libros():
    """Prueba búsqueda de libros."""
    print("\n" + "="*60)
    print(" TEST: Búsqueda de Libros")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780000000001", "Python Básico", "Guido", 2010, "Educativo", 2)
    biblioteca.agregar_libro("9780000000002", "Cálculo Avanzado", "Newton", 1687, "Ciencia", 1)
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Búsqueda por título
    assert len(biblioteca.buscar_libros("titulo", "python")) == 1
    # - Búsqueda por autor
    assert len(biblioteca.buscar_libros("autor", "newton")) == 1
    # - Búsqueda con filtro de categoría
    assert len(biblioteca.buscar_libros(categoria="Ciencia")) == 1
    # - Búsqueda sin resultados
    assert len(biblioteca.buscar_libros("titulo", "no existe")) == 0
    
    print("Prueba completada")


def prueba_estadisticas():
    """Prueba generación de estadísticas."""
    print("\n" + "="*60)
    print(" TEST: Estadísticas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9781111111111", "Libro 1", "Autor 1", 2000, "Historia", 3)
    biblioteca.registrar_usuario("u001", "Carlos", "carlos@example.com")

    for _ in range(2):
        pid = biblioteca.prestar_libro("9781111111111", "u001")
        biblioteca.devolver_libro(pid)
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Libros más prestados
    assert isinstance(biblioteca.libros_mas_prestados(), list)
    # - Usuarios más activos
    assert isinstance(biblioteca.usuarios_mas_activos(), list)
    # - Estadísticas por categoría
    assert isinstance(biblioteca.estadisticas_categoria("Historia"), dict)
    
    print("Prueba completada")


def prueba_excepciones():
    """Prueba manejo de excepciones personalizadas."""
    print("\n" + "="*60)
    print(" TEST: Excepciones Personalizadas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780000000000", "Titulo", "Autor", 2000, "Cat", 1)
    biblioteca.registrar_usuario("u001", "Usuario", "u1@example.com")
    
    # TODO: Implementar pruebas
    # Verificar que se lanzan correctamente:
    # - LibroNoEncontrado
    try:
        biblioteca.actualizar_copias("9999999999999", 1)
    except LibroNoEncontrado:
        print("LibroNoEncontrado capturado correctamente")
    else:
        raise AssertionError("Se esperaba LibroNoEncontrado")
    # - LibroNoDisponible
    pid = biblioteca.prestar_libro("9780000000000", "u001")
    try:
        biblioteca.prestar_libro("9780000000000", "u001")
    except LibroNoDisponible:
        print("LibroNoDisponible capturado correctamente")
    else:
        raise AssertionError("Se esperaba LibroNoDisponible")
    # - UsuarioNoRegistrado
    try:
        biblioteca.prestar_libro("9780000000000", "u999")
    except UsuarioNoRegistrado:
        print("UsuarioNoRegistrado capturado correctamente")
    else:
        raise AssertionError("Se esperaba UsuarioNoRegistrado")
    # - LimitePrestamosExcedido
    biblioteca.registrar_usuario("u002", "Otro", "otro@example.com")

    biblioteca.agregar_libro("9780000000001", "Libro2", "Autor2", 2001, "Cat", 1)

    biblioteca2 = SistemaBiblioteca(limite_prestamos=1)
    biblioteca2.agregar_libro("9781111111111", "L1", "A", 2000, "C", 1)
    biblioteca2.agregar_libro("9782222222222", "L2", "A", 2000, "C", 1)
    biblioteca2.registrar_usuario("x001", "Test", "t@example.com")
    biblioteca2.prestar_libro("9781111111111", "x001")
    try:
        biblioteca2.prestar_libro("9782222222222", "x001")
    except LimitePrestamosExcedido:
        print("LimitePrestamosExcedido capturado correctamente")
    else:
        raise AssertionError("Se esperaba LimitePrestamosExcedido")
    
    print("Prueba completada")


def prueba_importar_exportar():
    """Prueba importar/exportar catálogo."""
    print("\n" + "="*60)
    print(" TEST: Importar/Exportar")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9781234567890", "Prueba", "Autor", 2000, "General", 2)
    nombre_archivo = "catalogo_test.txt"
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Exportar catálogo
    res_export = biblioteca.exportar_catalogo(nombre_archivo)
    # - Importar catálogo
    resultado_import = biblioteca.importar_catalogo(nombre_archivo)
    assert isinstance(resultado_import, dict) and "exitosos" in resultado_import
    print("Exportar e importar correcto (resultado):", resultado_import)
    # - Manejo de errores en importación
    bad_file = "catalogo_malo.txt"
    with open(bad_file, "w", encoding="utf-8") as f:
        f.write("malformato|solo|3|campos\n")  # línea inválida
        f.write("9780000000003|Titulo|Autor|2001|Cat|2\n")  # línea válida

    resultado_bad = biblioteca.importar_catalogo(bad_file)
    assert "errores" in resultado_bad and isinstance(resultado_bad["errores"], list)
    print("Importación detecta errores de formato:", resultado_bad["errores"])
    
    print("Prueba completada")


def prueba_renovar_prestamo():
    """Prueba renovación de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Renovación de Préstamos")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9787777777777", "1984", "Orwell", 1949, "Ficción", 2)
    biblioteca.registrar_usuario("u001", "Pedro", "pedro@example.com")
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Renovar préstamo válido
    id_prestamo = biblioteca.prestar_libro("9787777777777", "u001")
    biblioteca.renovar_prestamo(id_prestamo)
    print("Renovacion valida OK")
    # - Intentar renovar préstamo vencido
    biblioteca.prestamos[id_prestamo]["fecha_vencimiento"] = datetime.now() - timedelta(days=2)
    try:
        biblioteca.renovar_prestamo(id_prestamo)
    except PrestamoVencido:
        print("Renovacion vencida detectada correctamente")
    else:
        raise AssertionError("Se esperaba PrestamoVencido")
    # - Renovar préstamo inexistente
    try:
        biblioteca.renovar_prestamo("P9999")
    except KeyError:
        print("Renovacion de prestamo inexistente levantó KeyError")
    except Exception:
        # aceptar cualquier excepción que indique no-existencia si tu implementación usa otro tipo
        print("Renovacion de prestamo inexistente levanto excepción (esperada)")
    else:
        raise AssertionError("Se esperaba error al renovar préstamo inexistente")

    
    print("Prueba completada")


def prueba_reporte_financiero():
    """Prueba reporte financiero."""
    print("\n" + "="*60)
    print(" TEST: Reporte Financiero")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(multa_por_dia=2.0)
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Reporte sin multas
    r_empty = biblioteca.reporte_financiero()
    assert isinstance(r_empty, dict) and "total_multas" in r_empty
    print("Reporte sin multas OK")
    # - Reporte con multas
    biblioteca.agregar_libro("9785555555555", "Crimen y Castigo", "Dostoievski", 1866, "Clásico", 1)
    biblioteca.registrar_usuario("u001", "Tatiana", "tatiana@example.com")
    id_prestamo = biblioteca.prestar_libro("9785555555555", "u001")
    # forzar vencimiento y devolver para generar multa
    biblioteca.prestamos[id_prestamo]["fecha_vencimiento"] = datetime.now() - timedelta(days=5)
    biblioteca.devolver_libro(id_prestamo)
    reporte = biblioteca.reporte_financiero()
    assert reporte.get("total_multas", 0) > 0
    print("Reporte con multas OK")
    # - Reporte con rango de fechas
    id_p2 = biblioteca.prestar_libro("9785555555555", "u001")
    biblioteca.prestamos[id_p2]["fecha_vencimiento"] = datetime.now() - timedelta(days=10)
    biblioteca.devolver_libro(id_p2)
    
    fechas = [p["fecha_devolucion"] for p in biblioteca.prestamos.values() if p["fecha_devolucion"]]
    if len(fechas) >= 2:
        fecha_primera = min(fechas)
        fecha_inicio = fecha_primera - timedelta(seconds=1)
        fecha_fin = fecha_primera + timedelta(seconds=1)
        reporte_rango = biblioteca.reporte_financiero(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        assert isinstance(reporte_rango, dict)
        print("Reporte con rango de fechas OK")
    else:
        print("No se pudieron generar suficientes devoluciones para probar rango; prueba de rango omitida")

    print("Prueba completada")


# ===========================================================================
# EJECUTAR TODAS LAS PRUEBAS
# ===========================================================================

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del sistema."""
    print("\n" + "="*70)
    print(" EJECUTANDO SUITE COMPLETA DE PRUEBAS")
    print("="*70)
    
    pruebas = [
        prueba_agregar_libros,
        prueba_registrar_usuarios,
        prueba_prestar_libros,
        prueba_devolver_libros,
        prueba_buscar_libros,
        prueba_estadisticas,
        prueba_excepciones,
        prueba_importar_exportar,
        prueba_renovar_prestamo,
        prueba_reporte_financiero
    ]
    
    exitosas = 0
    fallidas = 0
    
    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except Exception as e:
            print(f"✗ Error en {prueba.__name__}: {e}")
            fallidas += 1
    
    print("\n" + "="*70)
    print(" RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"✓ Exitosas: {exitosas}/{len(pruebas)}")
    print(f"✗ Fallidas: {fallidas}/{len(pruebas)}")
    print("="*70)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()

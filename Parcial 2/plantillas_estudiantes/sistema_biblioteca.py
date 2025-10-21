#!/usr/bin/env python3
"""
PARCIAL 2 - PROBLEMA INTEGRADOR (Parte 2)
Sistema de Gestión de Biblioteca Digital

Estudiante: Francisco Manuel Bermúdez Rodríguez
Fecha: 19/10/2025
"""

from datetime import datetime, timedelta

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS (5 puntos)
# ===========================================================================

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    """Se lanza cuando no hay copias disponibles."""
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    """Se lanza cuando el usuario no está registrado."""
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    """Se lanza cuando el usuario excede el límite de préstamos."""
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    """Se lanza para operaciones con préstamos vencidos."""
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA BIBLIOTECA (35 puntos)
# ===========================================================================

class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.
    
    Estructuras de datos:
    - catalogo: {isbn: {'titulo', 'autor', 'anio', 'categoria', 'copias_total', 'copias_disponibles'}}
    - usuarios: {id_usuario: {'nombre', 'email', 'fecha_registro', 'prestamos_activos', 'historial'}}
    - prestamos: {id_prestamo: {'isbn', 'id_usuario', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion', 'multa'}}
    """
    
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        """
        Inicializa el sistema.
        
        Args:
            dias_prestamo: Días permitidos para cada préstamo
            multa_por_dia: Multa diaria por retraso
            limite_prestamos: Máximo de préstamos simultáneos por usuario
        """
        # TODO: Inicializar estructuras de datos y configuración

        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
    
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        pass
    
    # ============ GESTIÓN DE CATÁLOGO ============
    
    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """
        Agrega un libro al catálogo.
        
        Validaciones:
        - ISBN debe ser string de 13 dígitos
        - Título y autor no vacíos
        - Año entre 1000 y año actual
        - Copias >= 1
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si ISBN ya existe
        """
        # TODO: Implementar

        if not (isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()):
            raise ValueError("ISBN debe ser un string de 13 digitos")
        if not titulo or not autor:
            raise ValueError("titulo y autor no pueden estar vacios")
        if not (1000 <= anio <= datetime.now().year):
            raise ValueError("año fuera de rango")
        if copias < 1:
            raise ValueError("debe haber al menos una copia")
        if isbn in self.catalogo:
            raise KeyError("ISBN ya registrado")

        self.catalogo[isbn] = {
            'titulo': titulo,
            'autor': autor,
            'anio': anio,
            'categoria': categoria,
            'copias_total': copias,
            'copias_disponibles': copias,
            'prestamos': 0
        }
        pass
    
    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        
        Raises:
            LibroNoEncontrado: Si ISBN no existe
            ValueError: Si resultado sería negativo
        """
        # TODO: Implementar

        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
    
        nuevo_total = self.catalogo[isbn]['copias_total'] + cantidad_cambio
        if nuevo_total < 0:
            raise ValueError("no puede haber copias negativas")

        self.catalogo[isbn]['copias_total'] = nuevo_total
        self.catalogo[isbn]['copias_disponibles'] += cantidad_cambio
        pass
    
    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        """
        Busca libros por diferentes criterios.
        
        Args:
            criterio: 'titulo', 'autor', 'anio'
            valor: Valor a buscar (búsqueda parcial case-insensitive)
            categoria: Filtro opcional por categoría
        
        Returns:
            Lista de diccionarios con info de libros que coinciden
        """
        # TODO: Implementar

        resultados = []
        valor = valor.lower()
        for isbn, libro in self.catalogo.items():
            if categoria and libro['categoria'].lower() != categoria.lower():
                continue
            if valor in str(libro[criterio]).lower():
                resultados.append({'isbn': isbn, **libro})
        return resultados
        pass
    
    # ============ GESTIÓN DE USUARIOS ============
    
    def registrar_usuario(self, id_usuario, nombre, email):
        """
        Registra un nuevo usuario.
        
        Validaciones:
        - Email debe contener '@' y '.'
        - Nombre no vacío
        - ID único
        
        Raises:
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar
        if not nombre:
            raise ValueError("el nombre no puede estar vacio")
        if '@' not in email or '.' not in email:
            raise ValueError("email invalido")
        if id_usuario in self.usuarios:
            raise KeyError("usuario ya registrado")
    
        self.usuarios[id_usuario] = {
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now(),
            'prestamos_activos': [],
            'historial': [],
            'multas': 0.0
        }
        pass
    
    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        
        Returns:
            dict con: nombre, prestamos_activos, puede_prestar, multas_pendientes
        
        Raises:
            UsuarioNoRegistrado: Si usuario no existe
        """
        # TODO: Implementar

        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
    
        u = self.usuarios[id_usuario]
        puede_prestar = len(u['prestamos_activos']) < self.limite_prestamos and u['multas'] <= 50
        return {
            'nombre': u['nombre'],
            'prestamos_activos': len(u['prestamos_activos']),
            'puede_prestar': puede_prestar,
            'multas_pendientes': u['multas']
        }
        pass
    
    # ============ GESTIÓN DE PRÉSTAMOS ============
    
    def prestar_libro(self, isbn, id_usuario):
        """
        Realiza un préstamo.
        
        Validaciones:
        - Usuario registrado
        - Libro existe y disponible
        - Usuario no excede límite de préstamos
        - Usuario no tiene multas pendientes > 50
        
        Returns:
            id_prestamo: ID único del préstamo
        
        Raises:
            UsuarioNoRegistrado, LibroNoEncontrado, LibroNoDisponible,
            LimitePrestamosExcedido, ValueError (multas pendientes)
        """
        # TODO: Implementar

        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
    
        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]

        if libro['copias_disponibles'] <= 0:
            raise LibroNoDisponible(isbn, libro['titulo'])
        if len(usuario['prestamos_activos']) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)
        if usuario['multas'] > 50:
            raise ValueError("usuario tiene multas pendientes mayores a 50")

        id_prestamo = f"P{len(self.prestamos) + 1}"
        fecha = datetime.now()
        vencimiento = fecha + timedelta(days=self.dias_prestamo)

        self.prestamos[id_prestamo] = {
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha,
            'fecha_vencimiento': vencimiento,
            'fecha_devolucion': None,
            'multa': 0.0
        }

        libro['copias_disponibles'] -= 1
        libro['prestamos'] += 1
        usuario['prestamos_activos'].append(id_prestamo)
        usuario['historial'].append(id_prestamo)

        return id_prestamo
        pass
    
    def devolver_libro(self, id_prestamo):
        """
        Procesa devolución de libro.
        
        Calcula multa si hay retraso.
        Actualiza estado de libro y usuario.
        
        Returns:
            dict: {'dias_retraso': int, 'multa': float, 'mensaje': str}
        
        Raises:
            KeyError: Si préstamo no existe
            ValueError: Si ya fue devuelto
        """
        # TODO: Implementar

        if id_prestamo not in self.prestamos:
            raise KeyError("prestamo no encontrado")
    
        p = self.prestamos[id_prestamo]
        if p['fecha_devolucion'] is not None:
            raise ValueError("el libro ya fue devuelto")

        p['fecha_devolucion'] = datetime.now()
        dias_retraso = (p['fecha_devolucion'] - p['fecha_vencimiento']).days
        multa = 0

        if dias_retraso > 0:
            multa = dias_retraso * self.multa_por_dia
            p['multa'] = multa
            self.usuarios[p['id_usuario']]['multas'] += multa

        self.catalogo[p['isbn']]['copias_disponibles'] += 1
        self.usuarios[p['id_usuario']]['prestamos_activos'].remove(id_prestamo)

        return {'dias_retraso': max(0, dias_retraso), 'multa': multa, 'mensaje': "devolucion procesada"}
        pass
    
    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        
        Raises:
            PrestamoVencido: Si ya está vencido
            KeyError: Si préstamo no existe
        """
        # TODO: Implementar

        if id_prestamo not in self.prestamos:
            raise KeyError("prestamo no existe")
        p = self.prestamos[id_prestamo]
        if datetime.now() > p['fecha_vencimiento']:
            raise PrestamoVencido(id_prestamo, (datetime.now() - p['fecha_vencimiento']).days)
        p['fecha_vencimiento'] += timedelta(days=self.dias_prestamo)
        pass
    
    # ============ ESTADÍSTICAS Y REPORTES ============
    
    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        
        Returns:
            Lista de tuplas: [(isbn, titulo, cantidad_prestamos), ...]
            Ordenada descendentemente por cantidad
        """
        # TODO: Implementar

        ordenados = sorted(self.catalogo.items(), key=lambda x: x[1]['prestamos'], reverse=True)
        return [(isbn, d['titulo'], d['prestamos']) for isbn, d in ordenados[:n]]
        pass
    
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        
        Returns:
            Lista de tuplas: [(id_usuario, nombre, total_prestamos), ...]
        """
        # TODO: Implementar

        ordenados = sorted(self.usuarios.items(), key=lambda x: len(x[1]['historial']), reverse=True)
        return [(u, d['nombre'], len(d['historial'])) for u, d in ordenados[:n]]
        pass
    
    def estadisticas_categoria(self, categoria):
        """
        Genera estadísticas de una categoría.
        
        Returns:
            dict: {
                'total_libros': int,
                'total_copias': int,
                'copias_prestadas': int,
                'tasa_prestamo': float,
                'libro_mas_popular': str
            }
        """
        # TODO: Implementar

        libros_categoria = [
            (isbn, datos) for isbn, datos in self.catalogo.items()
            if datos['categoria'].lower() == categoria.lower()
        ]
    
        if not libros_categoria:
            return {
                'total_libros': 0,
                'total_copias': 0,
                'copias_prestadas': 0,
                'tasa_prestamo': 0.0,
                'libro_mas_popular': None
            }

        total_libros = len(libros_categoria)
        total_copias = sum(d['copias_total'] for _, d in libros_categoria)
        copias_disponibles = sum(d['copias_disponibles'] for _, d in libros_categoria)
        copias_prestadas = total_copias - copias_disponibles
        tasa_prestamo = (copias_prestadas / total_copias) if total_copias > 0 else 0

        libro_mas_popular = max(libros_categoria, key=lambda x: x[1]['prestamos'])[1]['titulo']

        return {
            'total_libros': total_libros,
            'total_copias': total_copias,
            'copias_prestadas': copias_prestadas,
            'tasa_prestamo': round(tasa_prestamo, 2),
            'libro_mas_popular': libro_mas_popular
        }
        pass
    
    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        
        Returns:
            Lista de dicts con: id_prestamo, isbn, titulo, id_usuario,
            dias_retraso, multa_acumulada
        """
        # TODO: Implementar

        hoy = datetime.now()
        vencidos = []

        for id_p, datos in self.prestamos.items():
            if datos['fecha_devolucion'] is None and hoy > datos['fecha_vencimiento']:
                dias_retraso = (hoy - datos['fecha_vencimiento']).days
                multa_acumulada = dias_retraso * self.multa_por_dia
                isbn = datos['isbn']
                titulo = self.catalogo[isbn]['titulo']
                vencidos.append({
                    'id_prestamo': id_p,
                    'isbn': isbn,
                    'titulo': titulo,
                    'id_usuario': datos['id_usuario'],
                    'dias_retraso': dias_retraso,
                    'multa_acumulada': multa_acumulada
                })
        return vencidos
        pass
    
    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """
        Genera reporte financiero de multas.
        
        Args:
            fecha_inicio, fecha_fin: Rango de fechas (datetime)
            Si son None, usa todo el historial
        
        Returns:
            dict: {
                'total_multas': float,
                'multas_pagadas': float,
                'multas_pendientes': float,
                'prestamos_con_multa': int,
                'promedio_multa': float
            }
        """
        # TODO: Implementar

        total_multas = 0
        prestamos_con_multa = 0

        for p in self.prestamos.values():
            if p['multa'] > 0:
                fecha = p['fecha_devolucion'] or datetime.now()
                if (fecha_inicio and fecha < fecha_inicio) or (fecha_fin and fecha > fecha_fin):
                    continue
                total_multas += p['multa']
                prestamos_con_multa += 1

        multas_pagadas = sum(u['multas'] for u in self.usuarios.values() if u['multas'] == 0)
        multas_pendientes = sum(u['multas'] for u in self.usuarios.values() if u['multas'] > 0)
        promedio = total_multas / prestamos_con_multa if prestamos_con_multa > 0 else 0

        return {
            'total_multas': round(total_multas, 2),
            'multas_pagadas': round(multas_pagadas, 2),
            'multas_pendientes': round(multas_pendientes, 2),
            'prestamos_con_multa': prestamos_con_multa,
            'promedio_multa': round(promedio, 2)
        }
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        
        Maneja excepciones de archivo apropiadamente.
        """
        # TODO: Implementar

        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for isbn, d in self.catalogo.items():
                    linea = f"{isbn}|{d['titulo']}|{d['autor']}|{d['anio']}|{d['categoria']}|{d['copias_total']}\n"
                    f.write(linea)
            return True
        except OSError as e:
            print(f"error al escribir el archivo: {e}")
            return False
        pass
    
    def importar_catalogo(self, archivo='catalogo.txt'):
        """
        Importa catálogo desde archivo de texto.
        
        Maneja:
        - Archivo no existe
        - Formato incorrecto
        - Duplicados (no sobrescribir)
        
        Returns:
            dict: {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        # TODO: Implementar

        resultado = {'exitosos': 0, 'errores': []}
    
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                for num_linea, linea in enumerate(f, start=1):
                    partes = linea.strip().split('|')
                    if len(partes) != 6:
                        resultado['errores'].append((num_linea, 'Formato incorrecto'))
                        continue
                    isbn, titulo, autor, anio, categoria, copias = partes
                    try:
                        self.agregar_libro(isbn, titulo, autor, int(anio), categoria, int(copias))
                        resultado['exitosos'] += 1
                    except (ValueError, KeyError) as e:
                        resultado['errores'].append((num_linea, str(e)))
        except FileNotFoundError:
            print(f"Archivo '{archivo}' no encontrado.")
        except OSError as e:
            print(f"Error de lectura: {e}")
        return resultado
        pass


# ===========================================================================
# CASOS DE PRUEBA BÁSICOS
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA")
    print("="*70)
    
    # Crear instancia del sistema
    biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)
    
    # TODO: Añadir casos de prueba aquí
    
    print("\n✓ Sistema inicializado")
    print("  Añade tus pruebas para verificar la funcionalidad")

    if __name__ == "__main__":
        print("="*70)
        print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA")
        print("="*70)

        biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)

        try:
            biblioteca.agregar_libro("9781234567890", "Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela", 5)
            biblioteca.agregar_libro("9789876543210", "El Principito", "Antoine de Saint-Exupéry", 1943, "Infantil", 3)
            print("libros agregados")
        except Exception as e:
            print("error:", e)

        try:
            biblioteca.registrar_usuario("u001", "Juan Perez", "juan@example.com")
            biblioteca.registrar_usuario("u002", "Maria Lopez", "maria@example.com")
            print("usuarios registrados")
        except Exception as e:
            print("error:", e)

        try:
            id_prestamo = biblioteca.prestar_libro("9781234567890", "u001")
            print(f"prestamo realizado con ID: {id_prestamo}")
        except Exception as e:
            print("error:", e)

        try:
            resultado = biblioteca.devolver_libro(id_prestamo)
            print("libro devuelto:", resultado)
        except Exception as e:
            print("error:", e)

        resultados = biblioteca.buscar_libros(criterio="autor", valor="Gabriel")
        print("resultados de busqueda por autor:", resultados)

        reporte = biblioteca.reporte_financiero()
        print("reporte financiero:", reporte)

        if biblioteca.exportar_catalogo():
            print("catalogo exportado")

        resultado_importacion = biblioteca.importar_catalogo()
        print("resultado importacion:", resultado_importacion)

        estadisticas = biblioteca.estadisticas_categoria("Novela")
        print("estadisticas categoria 'Novela':", estadisticas)

        vencidos = biblioteca.prestamos_vencidos()
        print("prestamos vencidos:", vencidos)

        print("\nSistema inicializado")
        print("="*70)


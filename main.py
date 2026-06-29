"""
main.py
-------
Punto de entrada del programa.
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas.

Tecnicatura Universitaria en Programación - UTN
Materia: Programación 1
Trabajo Práctico Integrador (TPI)

Estructura de módulos:
    modulos/modulo_csv.py           → Lectura y escritura del archivo CSV
    modulos/modulo_validaciones.py  → Validación de entradas del usuario
    modulos/modulo_paises.py        → Agregar y actualizar países
    modulos/modulo_busqueda.py      → Búsqueda y filtrado de países
    modulos/modulo_ordenamiento.py  → Ordenamiento de la lista de países
    modulos/modulo_estadisticas.py  → Cálculo y visualización de estadísticas
    modulos/modulo_menu.py          → Menú principal e interacción de navegación
"""

import os
import sys

# Asegura que Python encuentre los módulos cuando se ejecuta desde cualquier directorio
sys.path.insert(0, os.path.dirname(__file__))

from modulos.modulo_csv import cargar_paises, guardar_paises
from modulos.modulo_paises import agregar_pais, actualizar_pais
from modulos.modulo_busqueda import menu_buscar, menu_filtrar
from modulos.modulo_ordenamiento import menu_ordenar
from modulos.modulo_estadisticas import menu_estadisticas
from modulos.modulo_menu import mostrar_menu_principal, leer_opcion

# ── Configuración de rutas ─────────────────────────────────────────────────
RUTA_CSV = os.path.join(os.path.dirname(__file__), "datos", "paises.csv")


def main() -> None:
    """
    Función principal del programa.
    Gestiona el ciclo de vida de la aplicación: carga inicial, menú y persistencia.
    """
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║   GESTIÓN DE DATOS DE PAÍSES - Programación 1 (UTN)  ║")
    print("╚══════════════════════════════════════════════════════╝")

    # Lista principal que almacena todos los países en memoria durante la sesión
    paises: list[dict] = []
    datos_modificados = False  # Indica si hay cambios sin guardar

    # ── Carga inicial automática ──────────────────────────────────────────
    try:
        paises = cargar_paises(RUTA_CSV)
        print(f"\n✅ Dataset cargado correctamente: {len(paises)} países desde '{RUTA_CSV}'.")
    except FileNotFoundError:
        print(f"\n⚠️  No se encontró el archivo '{RUTA_CSV}'.")
        print("   El programa iniciará con la lista vacía. Puede cargar datos desde el menú.")
    except ValueError as e:
        print(f"\n❌ Error al leer el CSV: {e}")
        print("   El programa iniciará con la lista vacía.")

    # ── Bucle principal del menú ──────────────────────────────────────────
    opciones_validas = {"0", "1", "2", "3", "4", "5", "6", "7", "8"}

    while True:
        mostrar_menu_principal()
        opcion = leer_opcion(opciones_validas)

        # ── Opción 1: Cargar CSV ──────────────────────────────────────────
        if opcion == "1":
            ruta = input(f"Ruta del archivo CSV [{RUTA_CSV}]: ").strip()
            if not ruta:
                ruta = RUTA_CSV
            try:
                paises = cargar_paises(ruta)
                datos_modificados = False
                print(f"✅ {len(paises)} países cargados desde '{ruta}'.")
            except (FileNotFoundError, ValueError) as e:
                print(f"❌ {e}")

        # ── Opción 2: Agregar país ────────────────────────────────────────
        elif opcion == "2":
            exito, mensaje = agregar_pais(paises)
            print(f"{'✅' if exito else '❌'} {mensaje}")
            if exito:
                datos_modificados = True

        # ── Opción 3: Actualizar país ─────────────────────────────────────
        elif opcion == "3":
            exito, mensaje = actualizar_pais(paises)
            print(f"{'✅' if exito else '❌'} {mensaje}")
            if exito:
                datos_modificados = True

        # ── Opción 4: Buscar por nombre ───────────────────────────────────
        elif opcion == "4":
            menu_buscar(paises)

        # ── Opción 5: Filtrar ─────────────────────────────────────────────
        elif opcion == "5":
            menu_filtrar(paises)

        # ── Opción 6: Ordenar ─────────────────────────────────────────────
        elif opcion == "6":
            menu_ordenar(paises)

        # ── Opción 7: Estadísticas ────────────────────────────────────────
        elif opcion == "7":
            menu_estadisticas(paises)

        # ── Opción 8: Guardar en CSV ──────────────────────────────────────
        elif opcion == "8":
            if not paises:
                print("⚠️  No hay datos para guardar.")
            else:
                ruta = input(f"Ruta de destino [{RUTA_CSV}]: ").strip()
                if not ruta:
                    ruta = RUTA_CSV
                try:
                    guardar_paises(paises, ruta)
                    datos_modificados = False
                    print(f"✅ {len(paises)} países guardados en '{ruta}'.")
                except Exception as e:
                    print(f"❌ Error al guardar: {e}")

        # ── Opción 0: Salir ───────────────────────────────────────────────
        elif opcion == "0":
            if datos_modificados:
                confirmar = input(
                    "\n⚠️  Hay cambios sin guardar. ¿Desea guardar antes de salir? (s/n): "
                ).strip().lower()
                if confirmar == "s":
                    try:
                        guardar_paises(paises, RUTA_CSV)
                        print(f"✅ Cambios guardados en '{RUTA_CSV}'.")
                    except Exception as e:
                        print(f"❌ Error al guardar: {e}")
            print("\n¡Hasta luego!\n")
            break


# ── Punto de entrada ───────────────────────────────────────────────────────
if __name__ == "__main__":
    main()

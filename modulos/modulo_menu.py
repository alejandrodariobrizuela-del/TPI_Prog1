"""
modulo_menu.py
--------------
Módulo responsable de mostrar el menú principal y leer la opción del usuario.
Delega cada acción al módulo correspondiente.
"""


def mostrar_menu_principal() -> None:
    """Imprime el menú principal en pantalla."""
    print("\n" + "=" * 50)
    print("    GESTIÓN DE DATOS DE PAÍSES - MENÚ PRINCIPAL")
    print("=" * 50)
    print("  1. Cargar países desde CSV")
    print("  2. Agregar un país")
    print("  3. Actualizar población/superficie de un país")
    print("  4. Buscar país por nombre")
    print("  5. Filtrar países")
    print("  6. Ordenar países")
    print("  7. Ver estadísticas")
    print("  8. Guardar cambios en CSV")
    print("  0. Salir")
    print("=" * 50)


def leer_opcion(opciones_validas: set[str]) -> str:
    """
    Solicita al usuario una opción del menú y la valida contra el conjunto de opciones permitidas.

    Args:
        opciones_validas: Conjunto de strings con las opciones aceptadas.

    Returns:
        La opción ingresada por el usuario (validada).
    """
    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion in opciones_validas:
            return opcion
        print(f"❌ Opción inválida. Las opciones válidas son: {', '.join(sorted(opciones_validas))}.")

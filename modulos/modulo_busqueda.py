"""
modulo_busqueda.py
------------------
Módulo responsable de buscar y filtrar países según distintos criterios:
  - Búsqueda por nombre (coincidencia parcial o exacta, case-insensitive)
  - Filtro por continente
  - Filtro por rango de población
  - Filtro por rango de superficie
"""

from modulos.modulo_validaciones import validar_continente, validar_rango


def buscar_por_nombre(paises: list[dict], termino: str) -> list[dict]:
    """
    Busca países cuyo nombre contenga el término dado (búsqueda parcial, sin distinguir mayúsculas).

    Args:
        paises: Lista de diccionarios de países.
        termino: Cadena de texto a buscar.
        
    Returns:
        Lista de países que coinciden con el término.
    """

    termino = termino.strip().lower()
    return [p for p in paises if termino in p["nombre"].lower()]


def filtrar_por_continente(paises: list[dict], continente: str) -> list[dict]:
    """
    Filtra países que pertenecen al continente especificado (case-insensitive).

    Args:
        paises: Lista de diccionarios de países.
        continente: Nombre del continente.

    Returns:
        Lista de países del continente indicado.
    """

    continente = continente.strip().lower()
    return [p for p in paises if p["continente"].lower() == continente]


def filtrar_por_rango_poblacion(paises: list[dict], min_pob: int, max_pob: int) -> list[dict]:
    """
    Filtra países cuya población esté dentro del rango [min_pob, max_pob].

    Args:
        paises: Lista de diccionarios de países.
        min_pob: Población mínima (inclusive).
        max_pob: Población máxima (inclusive).

    Returns:
        Lista de países dentro del rango de población.
    """

    return [p for p in paises if min_pob <= p["poblacion"] <= max_pob]


def filtrar_por_rango_superficie(paises: list[dict], min_sup: int, max_sup: int) -> list[dict]:
    """
    Filtra países cuya superficie esté dentro del rango [min_sup, max_sup].

    Args:
        paises: Lista de diccionarios de países.
        min_sup: Superficie mínima en km² (inclusive).
        max_sup: Superficie máxima en km² (inclusive).

    Returns:
        Lista de países dentro del rango de superficie.
    """
    
    return [p for p in paises if min_sup <= p["superficie"] <= max_sup]


# ── Funciones de menú (interacción con el usuario) ─────────────────────────

def menu_buscar(paises: list[dict]) -> None:
    """
    Solicita al usuario un término y muestra los países que coincidan con la búsqueda.
    """
    if not paises:
        print("⚠️  No hay países cargados.")
        return

    termino = input("\nIngrese el nombre (o parte del nombre) a buscar: ").strip()
    if not termino:
        print("❌ Debe ingresar un término de búsqueda.")
        return

    resultados = buscar_por_nombre(paises, termino)
    if not resultados:
        print(f"⚠️  No se encontraron países que coincidan con '{termino}'.")
    else:
        print(f"\n✅ {len(resultados)} resultado(s) para '{termino}':")
        _imprimir_tabla(resultados)


def menu_filtrar(paises: list[dict]) -> None:
    """
    Presenta al usuario las opciones de filtrado y ejecuta el filtro seleccionado.
    """
    if not paises:
        print("⚠️  No hay países cargados.")
        return

    print("\n--- Filtrar países ---")
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")
    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
        _filtrar_continente_interactivo(paises)
    elif opcion == "2":
        _filtrar_rango_interactivo(paises, campo="poblacion")
    elif opcion == "3":
        _filtrar_rango_interactivo(paises, campo="superficie")
    else:
        print("❌ Opción no válida.")


def _filtrar_continente_interactivo(paises: list[dict]) -> None:
    """Solicita el continente y muestra los países filtrados."""
    continente_raw = input("Ingrese el continente (América / Europa / Asia / África / Oceanía): ")
    valido, resultado = validar_continente(continente_raw)
    if not valido:
        print(f"❌ {resultado}")
        return

    continente_normalizado = resultado
    resultados = filtrar_por_continente(paises, continente_normalizado)

    if not resultados:
        print(f"⚠️  No se encontraron países en el continente '{continente_normalizado}'.")
    else:
        print(f"\n✅ Países en {continente_normalizado} ({len(resultados)}):")
        _imprimir_tabla(resultados)


def _filtrar_rango_interactivo(paises: list[dict], campo: str) -> None:
    """
    Solicita un rango mínimo y máximo para filtrar por población o superficie.

    Args:
        paises: Lista de diccionarios de países.
        campo: "poblacion" o "superficie".
    """
    unidad = "habitantes" if campo == "poblacion" else "km²"
    print(f"\nFiltrar por rango de {campo} ({unidad})")

    min_str = input(f"  Valor mínimo: ")
    max_str = input(f"  Valor máximo: ")

    valido, mensaje, valor_min, valor_max = validar_rango(min_str, max_str, campo)
    if not valido:
        print(f"❌ {mensaje}")
        return

    if campo == "poblacion":
        resultados = filtrar_por_rango_poblacion(paises, valor_min, valor_max)
    else:
        resultados = filtrar_por_rango_superficie(paises, valor_min, valor_max)

    if not resultados:
        print(f"⚠️  No hay países con {campo} entre {valor_min:,} y {valor_max:,} {unidad}.")
    else:
        print(f"\n✅ {len(resultados)} país/es con {campo} entre {valor_min:,} y {valor_max:,} {unidad}:")
        _imprimir_tabla(resultados)


def _imprimir_tabla(paises: list[dict]) -> None:
    """
    Imprime la lista de países en formato de tabla alineada.

    Args:
        paises: Lista de diccionarios a imprimir.
    """
    encabezado = f"{'#':<4} {'Nombre':<35} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<12}"
    separador = "-" * len(encabezado)
    print(separador)
    print(encabezado)
    print(separador)
    for i, p in enumerate(paises, start=1):
        print(
            f"{i:<4} {p['nombre']:<35} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<12}"
        )
    print(separador)

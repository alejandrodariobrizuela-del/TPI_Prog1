"""
modulo_estadisticas.py
-----------------------
Módulo responsable de calcular y mostrar estadísticas sobre el dataset de países:
    - País con mayor y menor población
    - Promedio de población
    - Promedio de superficie
    - Cantidad de países por continente
"""


# ── Funciones de cálculo ───────────────────────────────────────────────────

def pais_mayor_poblacion(paises: list[dict]) -> dict | None:
    """
    Devuelve el país con la mayor población.

    Args:
        paises: Lista de diccionarios de países.

    Returns:
        Diccionario del país con mayor población, o None si la lista está vacía.
    """
    if not paises:
        return None
    return max(paises, key=lambda p: p["poblacion"])


def pais_menor_poblacion(paises: list[dict]) -> dict | None:
    """
    Devuelve el país con la menor población.

    Args:
        paises: Lista de diccionarios de países.

    Returns:
        Diccionario del país con menor población, o None si la lista está vacía.
    """
    if not paises:
        return None
    return min(paises, key=lambda p: p["poblacion"])


def promedio_poblacion(paises: list[dict]) -> float:
    """
    Calcula el promedio de población de todos los países.

    Args:
        paises: Lista de diccionarios de países.

    Returns:
        Promedio como número flotante, o 0.0 si la lista está vacía.
    """
    if not paises:
        return 0.0
    total = sum(p["poblacion"] for p in paises)
    return total / len(paises)


def promedio_superficie(paises: list[dict]) -> float:
    """
    Calcula el promedio de superficie de todos los países.

    Args:
        paises: Lista de diccionarios de países.

    Returns:
        Promedio como número flotante, o 0.0 si la lista está vacía.
    """
    if not paises:
        return 0.0
    total = sum(p["superficie"] for p in paises)
    return total / len(paises)


def cantidad_por_continente(paises: list[dict]) -> dict[str, int]:
    """
    Cuenta la cantidad de países por continente.

    Args:
        paises: Lista de diccionarios de países.

    Returns:
        Diccionario {continente: cantidad}, ordenado alfabéticamente por continente.
    """
    conteo: dict[str, int] = {}
    for pais in paises:
        continente = pais["continente"]
        conteo[continente] = conteo.get(continente, 0) + 1
    return dict(sorted(conteo.items()))


# ── Función de menú ──────────────────────────────────────────────────────

def menu_estadisticas(paises: list[dict]) -> None:
    """
    Calcula y muestra todas las estadísticas del dataset en pantalla.
    """
    if not paises:
        print("⚠️  No hay países cargados. Cargue el CSV primero.")
        return

    print("\n" + "=" * 60)
    print("          ESTADÍSTICAS DEL DATASET DE PAÍSES")
    print("=" * 60)

    # ── Mayor y menor población ────────────────────────────────────────
    mayor = pais_mayor_poblacion(paises)
    menor = pais_menor_poblacion(paises)

    print("\n📊 Población:")
    print(f"   País más poblado    : {mayor['nombre']} ({mayor['poblacion']:,} hab.)")
    print(f"   País menos poblado  : {menor['nombre']} ({menor['poblacion']:,} hab.)")
    print(f"   Promedio de población: {promedio_poblacion(paises):,.0f} hab.")

    # ── Promedio de superficie ─────────────────────────────────────────
    print("\n🌍 Superficie:")
    print(f"   Promedio de superficie: {promedio_superficie(paises):,.0f} km²")

    # ── Cantidad por continente ────────────────────────────────────────
    print("\nℹ️  Cantidad de países por continente:")
    conteo = cantidad_por_continente(paises)
    ancho_max = max(len(c) for c in conteo)
    for continente, cantidad in conteo.items():
        barra = "█" * cantidad
        print(f"   {continente:<{ancho_max}} : {cantidad:>3}  {barra}")

    print(f"\n   Total de países en el dataset: {len(paises)}")
    print("=" * 60)

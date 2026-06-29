"""
modulo_paises.py
----------------
Módulo responsable de las operaciones de creación y actualización de países.
Incluye agregar un nuevo país y actualizar los datos de población y superficie.
"""

from modulos.modulo_validaciones import (validar_nombre, validar_entero_positivo, validar_continente, pais_ya_existe,)


def agregar_pais(paises: list[dict]) -> tuple[bool, str]:
    """
    Solicita al usuario los datos de un nuevo país, los valida e incorpora a la lista.
    No permite campos vacíos ni países duplicados (por nombre).

    Args:
        paises: Lista de diccionarios de países (se modifica in-place).

    Returns:
        Tupla (éxito: bool, mensaje: str).
    """
    print("\n--- Agregar nuevo país ---")

    # ── Nombre ──────────────────────────────────────────────────────────────
    nombre_raw = input("Nombre del país: ")
    valido, mensaje = validar_nombre(nombre_raw)
    if not valido:
        return False, f"Error en nombre: {mensaje}"

    nombre = nombre_raw.strip()
    if pais_ya_existe(nombre, paises):
        return False, f"Ya existe un país con el nombre '{nombre}'."

    # ── Población ────────────────────────────────────────────────────────────
    pob_raw = input("Población (número entero): ")
    valido, mensaje, poblacion = validar_entero_positivo(pob_raw, "población")
    if not valido:
        return False, mensaje

    # ── Superficie ───────────────────────────────────────────────────────────
    sup_raw = input("Superficie en km² (número entero): ")
    valido, mensaje, superficie = validar_entero_positivo(sup_raw, "superficie")
    if not valido:
        return False, mensaje

    # ── Continente ───────────────────────────────────────────────────────────
    continente_raw = input("Continente (América / Europa / Asia / África / Oceanía): ")
    valido, resultado = validar_continente(continente_raw)
    if not valido:
        return False, resultado
    continente = resultado  # resultado contiene el nombre normalizado

    # ── Incorporar a la lista ─────────────────────────────────────────────
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(nuevo_pais)
    return True, f"✅ País '{nombre}' agregado correctamente."


def actualizar_pais(paises: list[dict]) -> tuple[bool, str]:
    """
    Busca un país por nombre exacto y permite actualizar su población y/o superficie.

    Args:
        paises: Lista de diccionarios de países.

    Returns:
        Tupla (éxito: bool, mensaje: str).
    """
    if not paises:
        return False, "No hay países cargados para actualizar."

    print("\n--- Actualizar datos de un país ---")
    nombre_buscar = input("Ingrese el nombre exacto del país a actualizar: ").strip()

    if not nombre_buscar:
        return False, "Debe ingresar un nombre."

    # Buscar el país (case-insensitive)
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break

    if pais_encontrado is None:
        return False, f"No se encontró ningún país con el nombre '{nombre_buscar}'."

    print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
    print(f"  Población actual : {pais_encontrado['poblacion']:,}")
    print(f"  Superficie actual: {pais_encontrado['superficie']:,} km²")
    print("(Presione Enter para mantener el valor actual)")

    # ── Nueva población ───────────────────────────────────────────────────
    pob_raw = input(f"Nueva población [{pais_encontrado['poblacion']:,}]: ").strip()
    if pob_raw:
        valido, mensaje, nueva_poblacion = validar_entero_positivo(pob_raw, "población")
        if not valido:
            return False, mensaje
        pais_encontrado["poblacion"] = nueva_poblacion

    # ── Nueva superficie ──────────────────────────────────────────────────
    sup_raw = input(f"Nueva superficie [{pais_encontrado['superficie']:,} km²]: ").strip()
    if sup_raw:
        valido, mensaje, nueva_superficie = validar_entero_positivo(sup_raw, "superficie")
        if not valido:
            return False, mensaje
        pais_encontrado["superficie"] = nueva_superficie

    return True, f"✅ Datos de '{pais_encontrado['nombre']}' actualizados correctamente."

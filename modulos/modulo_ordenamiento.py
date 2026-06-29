"""
modulo_ordenamiento.py
----------------------
Módulo responsable de ordenar la lista de países según distintos criterios:
    - Por nombre (ascendente/descendente)
    - Por población (ascendente/descendente)
    - Por superficie (ascendente/descendente)

Utiliza el algoritmo de ordenamiento burbuja (Bubble Sort) para demostrar
el concepto de ordenamiento sin depender de funciones nativas, y también
ofrece la versión con sorted() para mayor eficiencia en producción.
"""


# ── Algoritmos de ordenamiento ─────────────────────────────────────────────

def ordenar_burbuja(paises: list[dict], clave: str, ascendente: bool = True) -> list[dict]:
    """
    Ordena una copia de la lista de países usando el algoritmo de burbuja (Bubble Sort).
    Se usa para ilustrar el concepto de ordenamiento de estructuras de datos.

    Args:
        paises: Lista de diccionarios de países.
        clave: Campo por el que ordenar ("nombre", "poblacion" o "superficie").
        ascendente: True para orden ascendente, False para descendente.

    Returns:
        Nueva lista ordenada (no modifica la original).
    """
    lista = list(paises)  # Copia para no alterar la original
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            val_a = lista[j][clave]
            val_b = lista[j + 1][clave]

            # Para cadenas de texto, comparar en minúsculas
            if isinstance(val_a, str):
                val_a = val_a.lower()
                val_b = val_b.lower()

            if ascendente:
                debe_intercambiar = val_a > val_b
            else:
                debe_intercambiar = val_a < val_b

            if debe_intercambiar:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def ordenar_nativo(paises: list[dict], clave: str, ascendente: bool = True) -> list[dict]:
    """
    Ordena una copia de la lista de países usando la función sorted() de Python.
    Más eficiente que Bubble Sort para listas grandes.

    Args:
        paises: Lista de diccionarios de países.
        clave: Campo por el que ordenar ("nombre", "poblacion" o "superficie").
        ascendente: True para orden ascendente, False para descendente.

    Returns:
        Nueva lista ordenada (no modifica la original).
    """
    if clave == "nombre":
        return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=not ascendente)
    return sorted(paises, key=lambda p: p[clave], reverse=not ascendente)


# ── Función de menú (interacción con el usuario) ───────────────────────────

def menu_ordenar(paises: list[dict]) -> None:
    """
    Presenta al usuario las opciones de ordenamiento, solicita la dirección
    y muestra la lista ordenada en pantalla.
    """
    if not paises:
        print("⚠️  No hay países cargados.")
        return

    print("\n--- Ordenar países ---")
    print("  Ordenar por:")
    print("    1. Nombre")
    print("    2. Población")
    print("    3. Superficie")
    opcion_campo = input("Seleccione el campo (1-3): ").strip()

    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if opcion_campo not in campos:
        print("❌ Opción no válida.")
        return

    clave = campos[opcion_campo]

    print("  Dirección:")
    print("    1. Ascendente (menor → mayor / A → Z)")
    print("    2. Descendente (mayor → menor / Z → A)")
    opcion_dir = input("Seleccione la dirección (1-2): ").strip()

    if opcion_dir == "1":
        ascendente = True
        etiqueta_dir = "ascendente"
    elif opcion_dir == "2":
        ascendente = False
        etiqueta_dir = "descendente"
    else:
        print("❌ Dirección no válida.")
        return

    # Usar ordenamiento burbuja (para demostrar el concepto académico)
    lista_ordenada = ordenar_burbuja(paises, clave, ascendente)

    print(f"\n✅ Países ordenados por '{clave}' ({etiqueta_dir}):")
    _imprimir_tabla(lista_ordenada)


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

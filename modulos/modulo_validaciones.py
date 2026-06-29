"""
modulo_validaciones.py
----------------------
Módulo responsable de validar las entradas del usuario antes de procesarlas.
Provee funciones de verificación para campos individuales y conjuntos de datos.
"""


def validar_nombre(nombre: str) -> tuple[bool, str]:
    """
    Valida que el nombre de un país no esté vacío y solo contenga caracteres válidos.

    Args:
        nombre: Cadena con el nombre del país.

    Returns:
        Tupla (es_valido: bool, mensaje: str).
    """
    nombre = nombre.strip()
    if not nombre:
        return False, "El nombre no puede estar vacío."
    if len(nombre) < 2:
        return False, "El nombre debe tener al menos 2 caracteres."
    if len(nombre) > 100:
        return False, "El nombre no puede superar los 100 caracteres."
    return True, ""


def validar_entero_positivo(valor_str: str, campo: str) -> tuple[bool, str, int]:
    """
    Valida que una cadena represente un número entero positivo.

    Args:
        valor_str: Cadena a validar.
        campo: Nombre del campo (para mensajes de error).

    Returns:
        Tupla (es_valido: bool, mensaje: str, valor_int: int).
        Si no es válido, valor_int = -1.
    """
    valor_str = valor_str.strip()
    if not valor_str:
        return False, f"El campo '{campo}' no puede estar vacío.", -1

    try:
        valor = int(valor_str)
    except ValueError:
        return False, f"'{campo}' debe ser un número entero. Ingresó: '{valor_str}'.", -1

    if valor < 0:
        return False, f"'{campo}' no puede ser negativo.", -1

    return True, "", valor


def validar_continente(continente: str) -> tuple[bool, str]:
    """
    Valida que el continente ingresado sea uno de los continentes reconocidos.

    Args:
        continente: Cadena con el nombre del continente.

    Returns:
        Tupla (es_valido: bool, mensaje: str).
    """
    continentes_validos = {"América", "Europa", "Asia", "África", "Oceanía", "Antártida"}
    continente = continente.strip()

    if not continente:
        return False, "El continente no puede estar vacío."

    # Comparación case-insensitive
    for c in continentes_validos:
        if c.lower() == continente.lower():
            return True, c  # Devuelve el nombre normalizado en mensaje

    return (
        False,
        f"Continente no reconocido: '{continente}'. "
        f"Válidos: {', '.join(sorted(continentes_validos))}.",
    )


def validar_rango(min_str: str, max_str: str, campo: str) -> tuple[bool, str, int, int]:
    """
    Valida que dos valores formen un rango mínimo–máximo coherente.

    Args:
        min_str: Cadena con el valor mínimo.
        max_str: Cadena con el valor máximo.
        campo: Nombre del campo (para mensajes de error).

    Returns:
        Tupla (es_valido: bool, mensaje: str, valor_min: int, valor_max: int).
        Si no es válido, valor_min y valor_max son -1.
    """
    valido_min, msg_min, valor_min = validar_entero_positivo(min_str, f"{campo} mínimo")
    if not valido_min:
        return False, msg_min, -1, -1

    valido_max, msg_max, valor_max = validar_entero_positivo(max_str, f"{campo} máximo")
    if not valido_max:
        return False, msg_max, -1, -1

    if valor_min > valor_max:
        return (
            False,
            f"El valor mínimo ({valor_min:,}) no puede ser mayor que el máximo ({valor_max:,}).",
            -1,
            -1,
        )

    return True, "", valor_min, valor_max


def pais_ya_existe(nombre: str, paises: list[dict]) -> bool:
    """
    Verifica si un país con ese nombre ya existe en la lista.

    Args:
        nombre: Nombre del país a buscar.
        paises: Lista de diccionarios de países.

    Returns:
        True si ya existe (comparación case-insensitive), False si no.
    """
    nombre_lower = nombre.strip().lower()
    return any(p["nombre"].lower() == nombre_lower for p in paises)

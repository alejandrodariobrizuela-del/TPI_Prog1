"""
modulo_csv.py
-------------
Módulo responsable de leer y guardar datos de países desde/hacia un archivo CSV.
Cada país se representa como un diccionario con las claves:
    nombre (str), poblacion (int), superficie (int), continente (str)
"""

import csv
import os


def cargar_paises(ruta_archivo: str) -> list[dict]:
    """
    Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada país.
    Controla errores de formato (campos faltantes, tipos incorrectos, filas vacías).

    Args:
        ruta_archivo: Ruta al archivo CSV.

    Returns:
        Lista de diccionarios con los datos de los países.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el archivo tiene un formato incorrecto.
    """
    
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")

    paises = []
    errores = []

    try:
        with open(ruta_archivo, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Verificar que el CSV tenga las columnas requeridas
            columnas_requeridas = {"nombre", "poblacion", "superficie", "continente"}
            if lector.fieldnames is None or not columnas_requeridas.issubset(set(lector.fieldnames)):
                raise ValueError(
                    f"El CSV debe tener las columnas: {columnas_requeridas}. "
                    f"Columnas encontradas: {lector.fieldnames}"
                )

            for numero_fila, fila in enumerate(lector, start=2):  # start=2 porque fila 1 es cabecera
                # Verificar que ningún campo esté vacío
                if any(valor.strip() == "" for valor in fila.values()):
                    errores.append(f"Fila {numero_fila}: contiene campos vacíos, se omitirá.")
                    continue

                # Convertir y validar tipos numéricos
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip(),
                    }

                    if pais["poblacion"] < 0:
                        errores.append(f"Fila {numero_fila}: población negativa, se omitirá.")
                        continue

                    if pais["superficie"] < 0:
                        errores.append(f"Fila {numero_fila}: superficie negativa, se omitirá.")
                        continue

                    paises.append(pais)

                except ValueError:
                    errores.append(
                        f"Fila {numero_fila}: 'poblacion' o 'superficie' no son números enteros válidos, se omitirá."
                    )

    except UnicodeDecodeError:
        raise ValueError("El archivo no tiene codificación UTF-8 válida.")

    # Mostrar advertencias si hubo filas problemáticas (pero continúa la carga)
    if errores:
        print("\n⚠️  Advertencias durante la carga del CSV:")
        for error in errores:
            print(f"   → {error}")
        print()

    return paises


def guardar_paises(paises: list[dict], ruta_archivo: str) -> None:
    """
    Guarda la lista de países en el archivo CSV.

    Args:
        paises: Lista de diccionarios con datos de países.
        ruta_archivo: Ruta donde se escribirá el archivo CSV.
    """
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

    with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)

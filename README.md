# 🌍 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**
Tecnicatura Universitaria en Programación — UTN

---

## Descripción

Aplicación de consola en Python 3 que permite gestionar un dataset de países del mundo.
El sistema lee datos desde un archivo CSV y ofrece un menú interactivo para buscar, filtrar, ordenar y obtener estadísticas sobre los países.

---

## Integrantes

|      Nombre      |
|------------------|
|Alejandro Brizuela|

---

## Estructura del proyecto

```
tpi_paises/
├── main.py                        # Punto de entrada del programa
├── datos/
│   └── paises.csv                 # Dataset base (101 países)
└── modulos/
    ├── __init__.py
    ├── modulo_csv.py              # Lectura y escritura del CSV
    ├── modulo_validaciones.py     # Validación de entradas del usuario
    ├── modulo_paises.py           # Agregar y actualizar países
    ├── modulo_busqueda.py         # Búsqueda y filtros
    ├── modulo_ordenamiento.py     # Ordenamiento (Bubble Sort)
    ├── modulo_estadisticas.py     # Estadísticas del dataset
    └── modulo_menu.py             # Menú principal
```

---

## Requisitos

- Python 3.10 o superior
- No requiere librerías externas (solo módulos de la biblioteca estándar)

---

## Instrucciones de uso

**1. Clonar el repositorio**
```bash
git clone https://github.com/usuario/tpi-paises.git
cd tpi-paises
```

**2. Ejecutar el programa**
```bash
python main.py
```

El programa carga automáticamente el archivo `datos/paises.csv` al iniciar.

---

## Menú de opciones

```
==================================================
    GESTIÓN DE DATOS DE PAÍSES - MENÚ PRINCIPAL
==================================================
  1. Cargar países desde CSV
  2. Agregar un país
  3. Actualizar población/superficie de un país
  4. Buscar país por nombre
  5. Filtrar países
  6. Ordenar países
  7. Ver estadísticas
  8. Guardar cambios en CSV
  0. Salir
==================================================
```

---

## Ejemplos de uso

### Buscar un país (opción 4)
```
Ingrese el nombre (o parte del nombre) a buscar: rep

✅ 3 resultado(s) para 'rep':
--------------------------------------------------------------------
#    Nombre                              Población    Superficie (km²) Continente
--------------------------------------------------------------------
1    República Dominicana               11,117,873           48,671 América
2    República Democrática del Congo    89,561,403        2,344,858 África
3    Corea del Norte                    25,778,816          120,538 Asia
--------------------------------------------------------------------
```

### Filtrar por continente (opción 5 → 1)
```
Ingrese el continente: Oceanía

✅ Países en Oceanía (5):
--------------------------------------------------------------------
#    Nombre                              Población    Superficie (km²) Continente
--------------------------------------------------------------------
1    Australia                          25,499,884        7,692,024 Oceanía
2    Nueva Zelanda                       5,084,300          268,021 Oceanía
...
```

### Ordenar por población descendente (opción 6)
```
Ordenar por: 2 (Población)
Dirección:   2 (Descendente)

✅ Países ordenados por 'poblacion' (descendente):
#    Nombre         Población  ...
1    China      1,411,778,724  ...
2    India      1,380,004,385  ...
3    Estados Unidos 331,002,651 ...
```

### Estadísticas (opción 7)
```
============================================================
          ESTADÍSTICAS DEL DATASET DE PAÍSES
============================================================

📊 Población:
   País más poblado    : China (1,411,778,724 hab.)
   País menos poblado  : Fiji (930,748 hab.)
   Promedio de población: 72,935,699 hab.

🌍 Superficie:
   Promedio de superficie: 1,173,923 km²

🗺️  Cantidad de países por continente:
   África  :  24  ████████████████████████
   América :  22  ██████████████████████
   Asia    :  26  ██████████████████████████
   Europa  :  24  ████████████████████████
   Oceanía :   5  █████

   Total de países en el dataset: 101
============================================================
```

### Agregar un país (opción 2)
```
--- Agregar nuevo país ---
Nombre del país: Islandia
Población (número entero): 376248
Superficie en km² (número entero): 103000
Continente (América / Europa / Asia / África / Oceanía): Europa

✅ País 'Islandia' agregado correctamente.
```

---

## Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

Todos los campos son obligatorios. `poblacion` y `superficie` deben ser números enteros no negativos.
Los continentes válidos son: `América`, `Europa`, `Asia`, `África`, `Oceanía`.

---

## Links

- 🎥 [Video demostrativo Youtube](https://youtu.be/vNLMOhrcPVY)
- 📄 [Informe PDF](https://drive.google.com/file/d/1YBhkSPCCwpm2jnf1d3cSHCb7Dhqu3F-z/view?usp=sharing)
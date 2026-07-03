"""
Módulo de validaciones.
Funciones genéricas de lectura de datos por teclado con
validación y manejo básico de errores, reutilizadas en
todo el sistema.
"""


def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Solicita un número entero al usuario hasta que ingrese un valor válido.
    Permite acotar el valor a un rango [minimo, maximo].
    """
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
        except ValueError:
            print("  Error: debe ingresar un número entero válido.")
            continue

        if minimo is not None and valor < minimo:
            print(f"  Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  Error: el valor debe ser menor o igual a {maximo}.")
            continue
        return valor


def leer_texto_no_vacio(mensaje):
    """Solicita un texto que no puede quedar vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("  Error: el campo no puede estar vacío.")
        else:
            return texto


def leer_si_no(mensaje):
    """Solicita una respuesta Sí/No y devuelve un booleano."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("  Error: respuesta inválida. Ingrese S (Sí) o N (No).")

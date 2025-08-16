"""
Tarea 1 - parejas
Estudiantes: Adrián Alonso Arguedas Arias y Héctor Jiménez Viales
Curso: Microprocesadores y Microcontroladores
Este archivo contiene lo siguiente:
1. count_char: Cuenta apariciones de un carácter en una cadena validada.
2. multiplo_2: Calcula múltiplos válidos de una base usando solo operaciones
   de desplazamiento.
"""

# códigos de error o éxito
exito = 0  # Todo excelente
error_no_es_cadena = -100  # El valor no es un string
error_str_no_valido = -200  # Cadena no es válida
error_car_no_valido = -300  # Caracteres no válidos
error_no_entero = -400  # No es número entero
error_mult_no_valido = -500  # No es múltiplo de los solicitados (1,2,4,8,16)


def count_char(cadena, caracter):
    """
    Cuenta la cantidad de veces que aparece un caracter específico en
    una cadena que ingresemos.

    Parámetros que se utilizan en esta función:
    -> cadena (str): Texto a analizar.
    -> caracter (str): Carácter a contar.

    Retorna:
        resultado: (código, cantidad)
        -> código -> int (0 = éxito, distinto de 0 = error)
        -> cantidad -> int o None
    """
    # Con esto se verifica que la cadena sea string
    if not isinstance(cadena, str):
        return error_no_es_cadena, None

    # Se verifica que la cadena contenga solo letras o dígitos
    if not cadena.isalnum():
        return error_str_no_valido, None

    # Se verifica que "caracter" sea un único carácter válido
    if (
        not isinstance(caracter, str)
        or len(caracter) != 1
        or not caracter.isalnum()
    ):
        return error_car_no_valido, None

    # Con esto se cuenta la cantidad de veces que aparece ese caracter
    cantidad = cadena.count(caracter)
    return exito, cantidad


def multiplo_2(base, multiplo):
    """
    Calcula base * multiplo usando desplazamientos binarios.

    Parámetros:
    -> base (int): Número base (entero positivo).
    -> multiplo (int): 1, 2, 4, 8, 16.

    Retorna:
        resultado: (código, resultado)
        -> código -> int (0 = éxito, distinto de 0 = error)
        -> resultado -> int o None
    """
    # Validar los tipos
    if not isinstance(base, int) or not isinstance(multiplo, int):
        return error_no_entero, None
    if base < 0 or multiplo < 0:
        return error_no_entero, None

    # Validar múltiplos permitidos
    if multiplo not in [1, 2, 4, 8, 16]:
        return error_mult_no_valido, None

    # Se emplean los desplazamientos binarios
    if multiplo == 1:
        resultado = base
    elif multiplo == 2:
        resultado = base << 1
    elif multiplo == 4:
        resultado = base << 2
    elif multiplo == 8:
        resultado = base << 3
    else:  # multiplo == 16
        resultado = base << 4

    return exito, resultado

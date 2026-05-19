"""
Práctica 3.1: Flujo de Inferencia y Predicciones Causales
=========================================================
INSTRUCCIONES:
- Complete las funciones marcadas con TODO
- No modifique las firmas de las funciones
- Puede agregar funciones auxiliares si lo necesita
- Ejecute las celdas en orden para verificar sus resultados
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importar el modelo lineal bayesiano usando el módulo local (incluido en la carpeta de la práctica)
from ModeloLinealFull import BayesianLinearModel

np.random.seed(42)
CMAP = plt.get_cmap("tab10")
N = 5000

# EJERCICIO 1: Realidad causal básica
# Cargar datos: df = pd.read_csv('../datos/modelo_basico.csv')
# Variables: z, x, y
# Estructura causal: Z -> X, Z -> Y, X -> Y
# Objetivo: Estimar el efecto causal de X sobre Y (valor real: -2)


def estimar_efecto_causal_ej1(df):
    """
    Estima el efecto causal de X sobre Y usando regresión bayesiana.

    Debe construir la matriz de diseño Phi con las variables de control
    apropiadas según el criterio backdoor.

    Args:
        df: DataFrame con columnas ['z', 'x', 'y']

    Returns:
        dict con:
            - 'coef_x': Coeficiente estimado de X (debería ser cercano a -2)
            - 'media': Vector de medias del posterior
            - 'covarianza': Matriz de covarianza del posterior
            - 'evidencia': Log-evidencia del modelo
    """
    N = len(df)
    Z = df["z"].values
    X = df["x"].values
    Y = df["y"].values

    # TODO: Construir la matriz de diseño Phi
    # ¿Qué variables necesitás incluir para cumplir backdoor?

    PHI = None  # TODO: np.column_stack([...])

    # TODO: Ajustar el modelo bayesiano
    blm = BayesianLinearModel(basis=lambda x: x)
    # blm.update(PHI, Y.reshape(N, 1))

    return {
        "coef_x": None,  # TODO: extraer de blm.location
        "media": None,
        "covarianza": None,
        "evidencia": None,
    }


# EJERCICIO 2: Realidad causal compleja
# Cargar datos: df = pd.read_csv('../datos/realidad_compleja.csv')
# Variables: z1, z2, z3, w1, w2, w3, x, y
# Objetivo: Identificar variables backdoor y estimar efecto de X sobre Y
#
# DAG:
#   z1 -> w1 -> x
#   z2 -> w2 -> y
#   z1, z2 -> z3 -> x, y
#   x -> w3 -> y
#
# Efecto causal real de X sobre Y: -2
#
# NOTA: Hay MULTIPLES conjuntos validos de variables de control.


def identificar_variables_backdoor_ej2():
    """
    Identifica las variables que cumplen el criterio backdoor para X -> Y.

    Analice el DAG provisto en la consigna y determine:
    - ¿Cual es el camino causal de X a Y?
    - ¿Cuales son los caminos backdoor de X a Y?
    - ¿Que variables cierran esos caminos?
    - ¿Hay mediadores que NO debemos incluir?

    IMPORTANTE: Puede haber multiples conjuntos validos de variables de control.
    El evaluador acepta cualquier conjunto que cierre correctamente el backdoor.

    Returns:
        dict con:
            - 'variables_control': Lista de nombres de variables a incluir
            - 'mediadores': Lista de mediadores (NO incluir en regresion)
            - 'justificacion': String explicando la eleccion
    """
    # TODO: Completar basandose en el analisis del DAG

    return {"variables_control": [], "mediadores": [], "justificacion": ""}


def estimar_efecto_causal_ej2(df):
    """
    Estima el efecto causal de X sobre Y en los datos complejos.

    Args:
        df: DataFrame con columnas ['z1', 'z2', 'z3', 'w1', 'w2', 'w3', 'x', 'y']

    Returns:
        dict con:
            - 'coef_x': Coeficiente estimado de X (deberia ser cercano a -2)
            - 'variables_usadas': Lista de variables incluidas en el modelo
            - 'evidencia': Log-evidencia del modelo
    """
    N = len(df)

    # TODO: Construir Phi segun las variables identificadas en backdoor

    PHI = None  # TODO
    Y = df["y"].values.reshape(N, 1)

    # TODO: Ajustar modelo y extraer coeficiente de X

    return {"coef_x": None, "variables_usadas": [], "evidencia": None}


# EJERCICIO 3: Falacia de la Tabla 2
# Cargar datos: df = pd.read_csv('../datos/falacia_tabla2.csv')
# Variables: u, e, f, s, y
# Estructura: ver DAG en consigna


def estimar_efecto_S_sobre_Y(df):
    """
    Estima el efecto causal de S sobre Y.

    IMPORTANTE: Los coeficientes de las otras variables (E, F) NO son
    sus efectos causales. Son solo controles.

    Args:
        df: DataFrame con columnas ['u', 'e', 'f', 's', 'y']

    Returns:
        dict con:
            - 'coef_s': Coeficiente de S (efecto causal estimado, real: -2)
            - 'coef_otros': Coeficientes de las variables de control
            - 'advertencia': String explicando la falacia
    """
    N = len(df)

    # TODO: Identificar variables de control para el efecto S -> Y
    # según el DAG provisto

    # TODO: Construir PHI y ajustar modelo bayesiano para estimar el efecto de S sobre Y
    # Debe devolver el coeficiente de S ('coef_s') y su desviación estándar ('std_s')
    # Además, incluir los coeficientes de control y una advertencia
    return {
        "coef_s": None,
        "std_s": None,
        "coef_otros": {},
        "advertencia": "Los coeficientes de E y F NO son efectos causales. "
        "Son solo controles para aislar el efecto de S.",
    }


# CÓDIGO DE VERIFICACIÓN (No modificar)

if __name__ == "__main__":
    # Ejercicio 1
    print("\n--- Ejercicio 1: Modelo básico ---")
    try:
        df = pd.read_csv("../datos/modelo_basico.csv")
        resultado = estimar_efecto_causal_ej1(df)
        print(f"Coeficiente de X estimado: {resultado['coef_x']}")
        print(f"Valor real: -2")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique que ../datos/modelo_basico.csv exista.")
    except Exception as e:
        print(f"Error: {e}")

    # Ejercicio 2
    print("\n--- Ejercicio 2: Realidad compleja ---")
    try:
        df = pd.read_csv("../datos/realidad_compleja.csv")
        backdoor = identificar_variables_backdoor_ej2()
        print(f"Variables de control: {backdoor['variables_control']}")
        resultado = estimar_efecto_causal_ej2(df)
        print(f"Coeficiente de X estimado: {resultado['coef_x']}")
    except FileNotFoundError:
        print("Archivo no encontrado. Ejecute primero la generación de datos.")
    except Exception as e:
        print(f"Error: {e}")

    # Ejercicio 3
    print("\n--- Ejercicio 3: Falacia Tabla 2 ---")
    try:
        df = pd.read_csv("../datos/falacia_tabla2.csv")
        resultado = estimar_efecto_S_sobre_Y(df)
        print(f"Coeficiente de S: {resultado['coef_s']} (real: -2)")
        print(f"ADVERTENCIA: {resultado['advertencia']}")
    except FileNotFoundError:
        print("Archivo no encontrado. Ejecute primero la generación de datos.")
    except Exception as e:
        print(f"Error: {e}")

"""
Práctica 1.1: Argumentos causales alternativos e incertidumbre.
============================================
"""

import warnings
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# 1. Definición del espacio de hipótesis
# ------------------------------------------------------------

# H representa las 3 cajas posibles {0, 1, 2}
H = np.arange(3)


# ------------------------------------------------------------
# 2. Priors
# ------------------------------------------------------------


def p_r(r: int) -> float:
    """
    P(R = r).
    Prior sobre la ubicación del regalo.
    r ∈ {0, 1, 2}
    """
    pass


def p_c(c: int) -> float:
    """
    P(C = c).
    Prior sobre la caja elegida por el participante
    c ∈ {0, 1, 2}
    """
    pass


# ------------------------------------------------------------
# 3. Modelos del presentador
# ------------------------------------------------------------


def p_s_rM0(s: int, r: int) -> float:
    """
    P(S = s | R= r, M = 0).
    Modelo 0 (No Monty Hall):
    El presentador abre cualquier caja que no tenga el regalo.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    """
    pass


def p_s_rcM1(s: int, r: int, c: int):
    """
    P(S = s | R= r, C= c, M = 1).
    Modelo 1 (Monty Hall):
    El presentador abre una caja que no tenga el regalo
    ni haya sido seleccionada.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    """
    pass


# ------------------------------------------------------------
# 4. Distribución conjunta P(r, c, s | M)
# ------------------------------------------------------------


def p_rcs_M(r: int, c: int, s: int, m: int) -> float:
    """
    P(r, c, s | M) = P(r | M)P(c | M)P(s | r, c, M)
    Distribución conjunta del modelo m.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    m ∈ {0, 1}
    """
    pass


# ------------------------------------------------------------
# 5. Simulación de datos (asumiendo Monty Hall verdadero)
# ------------------------------------------------------------

np.random.seed(0)


def simular(T=16) -> List[Tuple[int, int, int]]:
    """
    Función para simular datos según el modelo Monty Hall verdadero.
    T: número de datos a generar.
    """
    pass


# ------------------------------------------------------------
# 6. Probabilidad de los datos dado un modelo
# ------------------------------------------------------------


def p_s_cM(s: int, c: int, m: int) -> float:
    """
    P(s | c, M)
    Distribución condicional sobre la caja seleccionada por
    el presentador dada la elección del participante y el
    modelo considerado.
    s ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    m ∈ {0, 1}
    """
    pass


def p_r_csM(r: int, c: int, s: int, m: int) -> float:
    """
    P(r | c, s, M)
    Distribución condicional sobre la posición del regalo dada
    la elección del participante, la caja seleccionada por el presentador
    y el modelo considerado.
    s ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    m ∈ {0, 1}
    """
    pass


def pEpisodio_M(c: int, s: int, r: int, m: int) -> float:
    """
    P(c, s, r | M)
    Probabilidad de ver un episodio dado el modelo considerado.
    s ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    m ∈ {0, 1}
    """
    pass


def pDatos_M(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    P(Datos | M)
    Probabilidad de ver los datos dados el modelo considerado.
    m ∈ {0, 1}
    """
    pass


# ------------------------------------------------------------
# 7. Cálculo del bayes factor
# (diferencia en órdenes de magnitud en escala logarítmica)
# ------------------------------------------------------------


def log_pDatos_M(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    log(P(Datos | M))
    Logaritmo de la probabilidad de ver los datos dados el modelo considerado.
    """
    pass


def log_bayes_factor(datos: List[Tuple[int, int, int]], m_i: int, m_j: int) -> float:
    """
    log(Datos | Mi / Datos | Mj) = log_10P(Datos | Mi) - log_10P(Datos | Mj)
    Bayes factor en escala logarítmica para comparar dos modelos.
    m_i, m_j ∈ {0, 1}
    """
    pass


# ------------------------------------------------------------
# 8. Predicción típica que realizan los modelos sobre los datos
# ------------------------------------------------------------


def log_media_geometrica(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    log(Media Geométrica)
    Logaritmo de la media geométrica de los datos dados el modelo considerado.
    m ∈ {0, 1}
    """
    pass


# ------------------------------------------------------------
# 9. Probabilidad total de ver los datos
# ------------------------------------------------------------


def pM(m: int) -> float:
    """
    P(M)
    Prior sobre los modelos.
    m ∈ {0, 1}
    """
    pass


def pDatos(datos: List[Tuple[int, int, int]]) -> float:
    """
    P(Datos)
    Probabilidad total de ver los datos usando la contribución
    de todos los modelos.
    """
    pass


# ------------------------------------------------------------
# 10. Actualización de creencias sobre los modelos
# ------------------------------------------------------------


def pM_Datos(m: int, datos: List[Tuple[int, int, int]]) -> float:
    """
    P(M | Datos)
    Actualización de la creencia sobre el modelo M dado los datos
    (distribución a posteriori).
    """
    pass


def evolucion_posterior(m: int, datos: List[Tuple[int, int, int]]) -> List[float]:
    """
    Evolución del posterior de los modelos según se observa información.
    """
    pass


# ------------------------------------------------------------
# 11. Ejecución principal
# ------------------------------------------------------------

if __name__ == "__main__":
    # Simulación
    datos = simular(T=16)

    # Print de funciones
    print("log_bayes_factor (M1 contra M0):", log_bayes_factor(datos, 1, 0))
    print("log_media_geometrica (M0):", log_media_geometrica(datos, 0))
    print("log_media_geometrica (M1):", log_media_geometrica(datos, 1))

    # Posteriores
    post_M0 = evolucion_posterior(0, datos)
    post_M1 = evolucion_posterior(1, datos)

    # Gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(post_M0, label="M0: Base")
    plt.plot(post_M1, label="M1: Monty Hall")
    plt.xlabel("Número de episodios")
    plt.ylabel("P(Modelo | Datos)")
    plt.title("Evolución del posterior de los modelos")
    plt.legend()
    plt.tight_layout()
    plt.show()

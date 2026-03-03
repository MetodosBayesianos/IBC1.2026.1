"""
Práctica 1.1: Argumentos causales alternativos e incertidumbre. (opcional)
============================================
"""

import warnings

warnings.filterwarnings("ignore")


# IGNORAR: función de ayuda para verificar consistencia del modelo
def verificar_modelo(tol=1e-9):
    """
    Chequeos de consistencia rápido.
    - Verifica que priors sumen 1.
    - Verifica que cada fila de Cp_ts condicionales sume ~1.
    - Verifica que la suma de la distribución conjunta sobre todo el espacio ≈ 1.
    Lanza AssertionError si alguna verificación falla.
    """
    # priors
    assert abs(p_e(0) + p_e(1) - 1.0) < tol, "Prior P(E) no normalizado"
    assert abs(p_t(0) + p_t(1) - 1.0) < tol, "Prior P(T) no normalizado"

    # Cp_t P(A|E,T)
    for e in V:
        for t in V:
            s = sum(p_a_et(a, e, t) for a in V)
            assert abs(s - 1.0) < tol, (
                f"Cp_t P(A|E,T) no normalizada para (e,t)=({e},{t})"
            )

    # Cp_t P(L|A)
    for a in V:
        s = sum(p_l_a(l, a) for l in V)
        assert abs(s - 1.0) < tol, f"Cp_t P(L|A) no normalizada para a={a}"

    # Cp_t P(R|T)
    for t in V:
        s = sum(p_r_t(r, t) for r in V)
        assert abs(s - 1.0) < tol, f"Cp_t P(R|T) no normalizada para t={t}"

    # suma conjunta sobre todo el espacio
    total = 0.0
    for e in V:
        for t in V:
            for a in V:
                for l in V:
                    for r in V:
                        total += p_conjunta(e, t, a, l, r)
    assert abs(total - 1.0) < 1e-8, f"Suma de la conjunta != 1 (total={total})"


# -------------------------------------------------
# 1. Variables del modelo
# -------------------------------------------------
# E: Entradera
# T: Terremoto
# A: Alarma
# L: Llamada
# R: Redes
#
# Todas las variables son binarias: {0, 1}

V = [0, 1]

# -------------------------------------------------
# 2. Priors
# -------------------------------------------------


def p_e(e: int) -> float:
    """
    P(E = e).
    Prior para Entradera. e debe ser 0 o 1.
    Devuelve la probabilidad puntual P(E=e).
    """
    pass


def p_t(t: int) -> float:
    """
    P(T = t).
    Prior para Terremoto. t debe ser 0 o 1.
    Devuelve la probabilidad puntual P(T=t).
    """
    pass


# -------------------------------------------------
# 3. Distribuciones condicionales
# -------------------------------------------------


def p_a_et(a: int, e: int, t: int) -> float:
    """
    P(A = a | E = e, T = t).
    Tabla condicional del mecanismo de la alarma dado Entradera y Terremoto.
    a,e,t ∈ {0,1}. Devuelve P(A=a | E=e, T=t).
    """
    # Mirar la tabla de la teoríca!
    tabla = {
        (..., ...): {...: ..., ...: ...},
    }
    return tabla[(e, t)][a]


def p_l_a(l: int, a: int) -> float:
    """
    P(L = l | A = a).
    Probabilidad de llamada condicionada en el estado de la alarma.
    l,a ∈ {0,1}. Devuelve P(L=l | A=a).
    """
    pass


def p_r_t(r: int, t: int) -> float:
    """
    P(R = r | T = t).
    Probabilidad de que las redes comenten dado un terremoto.
    r,t ∈ {0,1}. Devuelve P(R=r | T=t).
    """
    pass


# -------------------------------------------------
# 4. Distribución conjunta
# -------------------------------------------------


def p_conjunta(e: int, t: int, a: int, l: int, r: int) -> float:
    """
    P(E=e, T=t, A=a, L=l, R=r).
    Factorización del modelo: P(E) P(T) P(A|E,T) P(L|A) P(R|T).
    Devuelve la probabilidad conjunta puntual para la tupla dada.
    """
    pass


# -------------------------------------------------
# 5. Ejercicio 1 — Consecuencia común
# -------------------------------------------------
# a) P(T | E=0, A=1)
# b) P(T | E=0)


def p_t_ea(t: int, e: int = 0, a: int = 1) -> float:
    pass


def p_t_e(t: int, e: int = 0) -> float:
    pass


# -------------------------------------------------
# 6. Ejercicio 2 — Causa común
# -------------------------------------------------
# a) P(A | T=1, R=1)
# b) P(A | R=1)


def p_a_tr(a: int, t: int = 1, r: int = 1) -> float:
    pass


def p_a_r(a: int, r: int = 1) -> float:
    pass


# -------------------------------------------------
# 7. Ejercicio 3 — Variable intermedia
# -------------------------------------------------
# a) P(T | A=1, L=1)
# b) P(T | L=1)


def p_t_al(t: int, a: int = 1, l: int = 1) -> float:
    pass


def p_t_l(t: int, l: int = 1) -> float:
    pass


# -------------------------------------------------
# 8. Comparaciones
# -------------------------------------------------

if __name__ == "__main__":
    print("Ejercicio 1")
    print("P(T=1 | E=0, A=1):", p_t_ea(1))
    print("P(T=1 | E=0):    ", p_t_e(1))
    print()

    print("Ejercicio 2")
    print("P(A=1 | T=1, R=1):", p_a_tr(1))
    print("P(A=1 | R=1):    ", p_a_r(1))
    print()

    print("Ejercicio 3")
    print("P(T=1 | A=1, L=1):", p_t_al(1))
    print("P(T=1 | L=1):    ", p_t_l(1))

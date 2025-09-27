#!/usr/bin/env python


"""El módulo contiene las siguientes funciones:

- `gaussxw(N)` - Retorna los puntos y pesos para cuadratura Gauss-Legendre
- `escalar(a, b, x, w)` - Escala puntos y pesos al intervalo de integración
- `integrando(x)` - Define la función a integrar
"""

import numpy as np

def gaussxw(N):
    """Calcula puntos y pesos para cuadratura Gaussiana.

    Esta función produce los puntos de colocación y pesos para el método
    de cuadratura Gaussiana, utilizado en integración numérica.

    Examples:
        >>> x, w = gaussxw(3)
        >>> x
        array([-0.77459667, 0., 0.77459667])
        >>> w
        array([0.55555556, 0.88888889, 0.55555556])

    Args:
        N (int): Número de subdivisiones deseado

    Returns:
        tuple: Una tupla que contiene dos arrays:
            - x (ndarray): Puntos de muestreo en el intervalo [-1, 1]
            - w (ndarray): Pesos correspondientes

    Nota:
        Los puntos y pesos se calculan usando la función leggauss 
        del módulo numpy.polynomial.legendre.
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w  

def escalar(a, b, x, w): 
    """Escala puntos y pesos al intervalo de integración [a, b].

    Transforma los puntos y pesos del intervalo estándar [-1, 1] 
    al intervalo de integración específico [a, b].

    Examples:
        >>> x = np.array([-1, 0, 1])
        >>> w = np.array([0.5, 1.0, 0.5])
        >>> x_esc, w_esc = escalar(0, 2, x, w)
        >>> x_esc
        array([0.0, 1.0, 2.0])
        >>> w_esc
        array([0.5, 1.0, 0.5])


    Args:
        a (float): Límite inferior del intervalo de integración
        b (float): Límite superior del intervalo de integración
        x (ndarray): Puntos de muestreo en [-1, 1]
        w (ndarray): Pesos en [-1, 1]

    Returns:
        tuple: Una tupla que contiene:
            - puntos_escalados (ndarray): Puntos escalados a [a, b]
            - pesos_escalados (ndarray): Pesos escalados apropiadamente
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def integrando(x):
    """Define la función matemática a integrar.

    Esta función representa el integrando específico para el problema
    de integración numérica. En este caso: f(x) = x⁶ - x²·sin(2x)

    Examples:
        >>> integrando(0)
        0.0
        >>> integrando(1)
        1 - np.sin(2)  # Aproximadamente -0.9092974268256817

    Args:
        x (float): Punto donde evaluar la función

    Returns:
        float: Valor de la función en el punto dado
   """
    return x**6 - x**2 * np.sin(2 * x)

#Determinación del N con el que se obtiene el resultado correcto

tolerancia = 1e-12 
ext_inicial = 1
ext_final = 3

i = 0

num_subdivisiones = 1

while i == 0:

    #Cálculo de integral para N subdivisiones
    puntosN, pesosN = gaussxw(num_subdivisiones)
    puntos_escN, pesos_escN = escalar(ext_inicial, ext_final, puntosN, pesosN)

    valor_integralN = np.sum(integrando(puntos_escN)*pesos_escN) #cálculo de la integral mediante la cuadratura gaussiana

    #Cálculo de integral para N - 1 subdivisiones
    puntosN1, pesosN1 = gaussxw(num_subdivisiones + 1)
    puntos_escN1, pesos_escN1 = escalar(ext_inicial, ext_final, puntosN1, pesosN1)

    valor_integralN1 = np.sum(integrando(puntos_escN1)*pesos_escN1)
    
    #Verificación de convergencia
    if np.abs(valor_integralN1 - valor_integralN) < tolerancia:
        i = 1
    else:
        num_subdivisiones += 1

print(f'El valor de la integral es {valor_integralN:.10f} y se alcanza para un N de {num_subdivisiones}, con una tolerancia de {tolerancia}')

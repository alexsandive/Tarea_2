# **Método de Cuadratura Gaussiana**

La cuadratura Gaussiana es un método de integración numérica que aproxima una integral definida mediante una suma ponderada de valores de la función en puntos específicos, **no equidistantes** dentro del intervalo de integración. En otras palabras:

$$
\int_{a}^{b} f(x) dx \approx \sum_{i=1}^{N} w_k f(x_k)
$$

donde:

* $x_k$ son los **puntos de muestreo**
* $w_k$ son los **"pesos"**
* $N$ es el número de puntos de evaluación

## **Polinomios de Legendre**

Este método utiliza los polinomios ortogonales de Legendre $P_n(x)$ definidos en el intervalo $[-1, 1]$ para elegir los pesos y los puntos de muestreo que se necesitan. 

* Los puntos de cuadratura $x_k$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre $P_N(x)$ de orden $N$.
* Los pesos se eligen tal que:

    $$
    w_k = \left[ \frac{2}{(1-x^2)} \left(\frac{dP_N}{dx}\right)^{-2} \right]_{x=x_k}; P_N(x_k) = 0
    $$


### Definición de recursividad de los polinomios

Tomando $P_0(x) = 1$ y $P_1(x) = x$,

$$
(N + 1)P_{N+1}(x) = (2N + 1)xP_N(x) - NP_{N-1}(x)
$$

## **Escalado del intervalo**

Debido a que los polinomios de Legendre están definidos en $[-1, 1]$, para integrar en un intervalo arbitrario $[a, b]$, se debe aplicar la siguiente transformación sobre los pesos y los puntos de muestreo:

$$
x_{\text{esc}} = \frac{b-a}{2}x + \frac{a+b}{2}
$$

$$
w_{\text{esc}} = \frac{b-a}{2}w
$$

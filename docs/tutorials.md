# **Tutorial**

Para calcular una integral definida usando este módulo:

1. **Defina el integrando**: Modifique la función `integrando(x)` con la expresión matemática deseada
2. **Especifique los límites**: Asigne los valores correctos a las variables `ext_inicial` y `ext_final`  

## **Ejemplo práctico de implementación**

Para calcular:

$$
\int_{0}^{3} (\cos(x)\sin(2x))  dx
$$

`integrando(x)`, `ext_inicial` y `ext_final` deben verse de esta forma:

~~~

def integrando(x):
    return np.cos(x) * np.sin(2 * x)

ext_inicial = 0
ext_final = 3

~~~

Asimismo, a la hora de ejecutar el script, este debe dar el siguiente resultado:

~~~

El valor de la integral es 1.3135179586 y se alcanza para un N de 12, con una tolerancia de 1e-12

~~~


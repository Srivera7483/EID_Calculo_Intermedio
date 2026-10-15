# Guion del video — Teorema Fundamental del Cálculo, Parte I

**Pregunta central:** ¿Por qué la derivada de una acumulación recupera la función que se está acumulando?

---

## 1. Presentación

**Diego:** Hola, somos el grupo 8: Diego, Sebastián y David. El tema de hoy es el Teorema Fundamental del Cálculo, Parte I. El apunte de partida plantea una pregunta complementaria a la que ya nos hizo conocer la derivada: si sabemos cómo cambia una cantidad, ¿cómo describimos lo que se acumula en un intervalo? Y la pregunta central que vamos a responder es: ¿por qué la derivada de una acumulación recupera la función que se está acumulando?

**Sebastián:** Derivar reduce a una tasa instantánea, integrar suma y acumula. Este teorema muestra que, en el fondo, son la misma idea mirada desde dos lados. Vamos con la teoría primero, y después con un ejemplo propio.

---

## 2. Teoría: el concepto de acumulación

**Sebastián:** Si tenemos una función continua $f$, para medir el acumulado en $[a, b]$ dividimos el intervalo, elegimos un punto muestra en cada trozo y formamos rectángulos: altura representativa por ancho $\Delta x$. La suma de sus aportes es una suma de Riemann:

$$S_n = \sum_{i=1}^{n} f(x_i^*) \, \Delta x$$

Cuando aumentamos el número de subintervalos, $\Delta x$ tiende a cero y esas sumas se acercan a un valor: así nace la integral definida. **Suma → límite → integral.**

**David:** Ahora viene la evolución. En vez de dejar el límite superior como el número fijo $b$, lo dejamos como variable $x$. Así nace la **función de acumulación**:

$$A(x) = \int_{a}^{x} f(t) \, dt$$

Cada valor de $x$ devuelve cuánto se acumuló desde el punto de partida $a$ hasta ese $x$: al agrandar $x$, se abre un tramo nuevo y el área bajo la curva crece con él.

**Diego:** Eso nos permite responder ya las dos preguntas del apunte sobre la integral como acumulación. Primero: si $f$ representa una tasa de cambio —velocidad, flujo, producción—, su integral representa la **cantidad neta acumulada** en el intervalo medido. Segundo: esa cantidad acumulada **no** es siempre la cantidad final del sistema, porque la integral solo cuenta lo que ocurre entre $a$ y $x$; lo anterior al punto de partida queda fuera. Eso es el teorema del cambio neto.

---

## 3. Ejemplo desarrollado

**David:** Vamos con nuestro ejemplo. Un auto circula por una autopista en línea recta con velocidad $f(t) = 2t$ km/h. La velocidad es la tasa de cambio de la distancia: esa es la función que se está acumulando.

**Diego:** La distancia acumulada hasta el instante $x$ es la función de acumulación con $a = 0$. Como una antiderivada de $2t$ es $t^2$, el resultado $\int_a^b f = F(b) - F(a)$ del teorema nos dice que la integral vale $F(x) - F(0)$:

$$A(x) = \int_{0}^{x} 2t \, dt = t^2 \Big|_{0}^{x} = x^2 - 0 = x^2$$

$A(1) = 1$ km, $A(2) = 4$ km, $A(3) = 9$ km. Cada vez que ampliamos el límite superior $x$, la integral recorre un intervalo más largo y la cantidad acumulada cambia.

**David:** Y acá está la pregunta central. Si ahora derivamos esa acumulación:

$$A'(x) = \frac{d}{dx}\left(x^2\right) = 2x = f(x)$$

Recuperamos exactamente la función que estábamos acumulando. ¿Por qué? Porque la derivada mide el cambio instantáneo de $A$: al aumentar $x$ en una cantidad diminuta $\Delta x$, la acumulación gana el área de una franja bajo $f$, entre $x$ y $x + \Delta x$. Esa franja es la nueva distancia recorrida en ese instante, y su altura es, precisamente, $f(x)$.

---

## 4. Cierre: la relación $A'(x) = f(x)$

**Sebastián:** En pantalla, con Manim, se ve exactamente eso: los rectángulos de la suma de Riemann afinándose, y después esa franja de base $\Delta x$ corriéndose a lo largo de la curva de $f$. Su área es $f(c) \cdot \Delta x$ para algún punto intermedio $c$ entre $x$ y $x + \Delta x$: eso lo garantiza el teorema del valor medio para integrales.

**Diego:** Aplicamos la definición de derivada sobre $A(x)$:

$$A'(x) = \lim_{\Delta x \to 0} \frac{A(x + \Delta x) - A(x)}{\Delta x} = \lim_{\Delta x \to 0} \frac{1}{\Delta x} \int_{x}^{x + \Delta x} f(t) \, dt$$

El numerador es justamente esa franja. Sustituyendo por $f(c) \cdot \Delta x$, el $\Delta x$ se cancela con el denominador, y al tender a cero el intervalo se encoge hasta desaparecer: $c$ queda forzado a caer en $x$, y queda $f(x)$.

**David:** Verifiquémoslo en el auto. Como $A(x) = x^2$:

$$A'(x) = \lim_{\Delta x \to 0} \frac{(x + \Delta x)^2 - x^2}{\Delta x} = \lim_{\Delta x \to 0} \frac{2x\,\Delta x + (\Delta x)^2}{\Delta x} = \lim_{\Delta x \to 0} \left(2x + \Delta x\right) = 2x = f(x)$$

El término $(\Delta x)^2$ se vuelve insignificante: la ganancia de área se comporta cada vez más como un rectángulo de altura $2x$. La derivada de la distancia acumulada devuelve la velocidad del instante.

**Sebastián:** Esa es la respuesta. La derivada de la acumulación *deshace* la suma: la integral va acumulando trocitos de área, y la derivada recupera, instante por instante, la tasa que originó cada trocito. En pantalla se cierra el ciclo: curva de $f$ → área que crece → gráfica de $A$ → derivada que devuelve $f$.

**Diego:** El teorema, tal como lo plantean Stewart, Thomas y Larson, es el puente entre ambas operaciones:

$$\frac{d}{dx} \left[ \int_{a}^{x} f(t) \, dt \right] = f(x)$$

Integrar acumula; derivar recupera la tasa. Acumulación y cambio son la misma historia contada de dos formas. Somos el grupo 8, gracias por ver.

# Guion del video — Teorema Fundamental del Cálculo

**Grupo:** 8 — Diego, Sebastián y David
**Pregunta central:** ¿Por qué la derivada de una acumulación recupera la función que se está acumulando?
**Duración:** el video dura ≈ 4:32; el guion sigue el orden y los tiempos de sus escenas.

> **Nota de nomenclatura:** el video titula el resultado central como **Segundo Teorema Fundamental del Cálculo** (convención Larson & Edwards). En la presentación se menciona el **Primer Teorema del Cálculo** solo como herramienta para evaluar la integral.
>
> **Regla general:** después del bloque del ejemplo (~0:23–0:32) **ya no se reintroduce el ejemplo**. Todo lo que se grafica se asume como el vehículo con aceleración constante 2 km/h² y velocidad $v(t)=2t$.

---

## 1. Presentación (~0:00–0:32)

**Diego (0:00–0:23):** Hola, somos el grupo 8: Diego, Sebastián y David. Nuestro tema es el Teorema Fundamental del Cálculo y la integral como acumulación. Estas son las preguntas que guían el video, dentro de las cuales nos enfocaremos en las dos últimas: la número 3 describe cómo crece el acumulado y la número 4 corresponde a la pregunta central «¿Por qué la derivada de la acumulación es igual a la función original?»

**Sebastián (0:23–0:32):** En todo el video usamos el ejemplo del vehículo con velocidad $v(t)=2t$. Para medir su acumulación usamos el Primer Teorema del Cálculo.

---

## 2. Teoría: el concepto de acumulación (~0:32–2:47)

**Sebastián (0:32–0:51):** Si graficamos velocidad contra tiempo, el área bajo $v(t)=2t$ entre dos instantes es la distancia recorrida. Para aproximarla usamos una **suma de Riemann**: partimos el intervalo en subintervalos y sumamos rectángulos de base $\Delta t$ y altura $v(t)$. Es, simplemente, una sumatoria: un recurso que ya conocemos y que aquí mencionamos solo de paso.

**Sebastián (0:51–1:18):** Al afinar cada vez más los rectángulos, esa suma se convierte en la integral definida, y las unidades lo confirman: la altura se mide en km/h y la base en horas, así que cada área vale km/h × h = km. Por eso la integral de la velocidad es la **distancia acumulada**. En el tramo de 1 a 3 horas: $\int_{1}^{3} 2t\,dt = [t^2]_{1}^{3} = 9 - 1 = 8$ km.

**Diego (1:18–1:55):** Pero cuidado: esos 8 km son la distancia acumulada en ese tramo, no la posición total del vehículo. La integral solo entrega el **cambio neto**, $\Delta s$. El **Teorema del Cambio Neto** lo formaliza como $\int_{a}^{b} F'(t)\,dt = F(b) - F(a)$: la acumulación depende del punto de partida. Si a la hora 1 el odómetro marcaba $s(1)=50$ km, al sumar el cambio neto obtenemos $s(3) = 50 + 8 = 58$ km. La cantidad acumulada, entonces, **no** es automáticamente el total del sistema: hay que agregarle el estado inicial.

**David (1:55–2:47):** Ahora, ¿qué pasa si dejamos el límite superior como variable? Definimos la **función de acumulación** $A(x) = \int_{0}^{x} 2t\,dt$. Al resolverla, $A(x)=x^2$: en $x=1$ se acumuló 1 km, en $x=2$ van 4 km y en $x=3$ ya son 9 km. En pantalla se ve la franja de área que crece al desplazar $x$, y la distancia acumulada lo hace de forma cuadrática, siguiendo la parábola $x^2$.

---

## 3. Ejemplo desarrollado: el Segundo Teorema Fundamental (~2:47–3:30)

**Sebastián (2:47–3:05):** Aquí entra el **Segundo Teorema Fundamental del Cálculo**: $\frac{d}{dx}\left[\int_{a}^{x} f(t)\,dt\right] = f(x)$. Es decir, la derivada de la función de acumulación devuelve la función original. Lo demostramos con nuestro ejemplo. Partimos de la definición formal de derivada:

$$A'(x) = \lim_{\Delta x \to 0} \frac{A(x+\Delta x) - A(x)}{\Delta x}$$

**David (3:05–3:30):** Como cada término es una integral, esa diferencia equivale al área entre $x$ y $x+\Delta x$:

$$A(x+\Delta x) - A(x) = \int_{x}^{x+\Delta x} 2t\,dt$$

Es exactamente la franja que aparece en pantalla. Por el **teorema del valor medio**, esa franja tiene la misma área que un rectángulo de base $\Delta x$ y altura $v(c)$, para algún $c$ entre $x$ y $x+\Delta x$; como $v(t)=2t$, el área es $2c \cdot \Delta x$.

---

## 4. Cierre: la relación $A'(x)=f(x)$ (~3:30–3:57)

**Diego (3:30–3:57):** Sustituyendo en el cociente de la derivada, el $\Delta x$ se cancela y queda $A'(x) = \lim_{\Delta x \to 0} 2c$. En pantalla la franja se encoge hasta desaparecer, y eso obliga al punto $c$ a caer en $x$; por lo tanto $\lim 2c = 2x$. Como $v(x)=2x$, concluimos que $A'(x) = v(x)$. **Queda demostrado**: la razón de cambio de la distancia acumulada es la velocidad instantánea; derivar la acumulación recupera la función que se estaba acumulando.

---

## 5. Síntesis: respuestas a las preguntas guía (~3:57–4:32)

**Diego (3:57–4:05):** Recapitulando las preguntas del inicio: la integral de una tasa de cambio representa la magnitud neta acumulada —aquí, velocidad por tiempo igual a distancia—; y **no**, la acumulación no es el total del sistema, porque es solo el cambio neto $\Delta s$ y hay que sumarle el estado inicial $s(a)$.

**David (4:05–4:15):** Al ampliar el límite superior $x$, la acumulación forma la función $A(x)=x^2$, de crecimiento cuadrático; y su derivada recupera la función original por el Segundo Teorema Fundamental: al encoger la franja con $\Delta x \to 0$, el área rectangular colapsa en la altura $f(x)$.

**Sebastián (4:15–4:32):** Con esto cerramos: acumular y derivar son operaciones inversas, dos formas de mirar la misma relación entre una cantidad y su razón de cambio. Somos el grupo 8, gracias por ver.

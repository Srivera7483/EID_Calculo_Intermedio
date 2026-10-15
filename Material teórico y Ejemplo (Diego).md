
![[Pasted image 20261014132331.png|655]]

# Material teórico
---



La <span style="color:rgb(192, 0, 0)">integral</span> es un concepto fundamental del cálculo matemático que representa una suma continua de infintios elementos extremadamente pequeños.

Teniendo como base el material de apunte ***Introducción a la integral*** del curso, solo vale recordar que el concepto de integral (integral definida) se desprende de la idea de tomar varios subintervalos de intervalo cualquiera de una función y, pensando en su gráfica, calcular el área de cada subintervalo individualmente para obtener un área aproximada a la de ese intervalo completo cualquiera que se tomó de esa función: el punto a partir de acá es ir aumentando cada vez más (infinitamente) esos intervalos para que las formas seleccionadas sean cada vez más diminutas y en su conjunto se acerquen lo máximo posible al área real de la función.

Bien, si se hace esta operación conocida como integral ahora en una función cuya relación $\frac{\Delta{y}}{\Delta{x}}$ representa una tasa de cambio, como la velocidad, surge la pregunta: ¿qué representa esa área de ese intervalo que se tome? 

- El foco de la explicación y el ejemplo deben ser:
	- Responder a las preguntas:  ¿Qué representa la integral de una tasa de cambio? ¿La cantidad acumulada corresponde siempre a la cantidad final del sistema?
	- Demostrar que la derivada de una acumulación (integral) es igual a la función original que se está acumulando.
	- Cómo cambia la cantidad acumulada a medida que se amplía el límite superior x.


#### Antiderivadas
---
Una <span style="color:rgb(192, 0, 0)">antiderivada</span> de una función $f(x)$ es básicamente asumir que $f(x)$ es una derivada, y la antiderivada sería la función original desde la que se derivó.

## Primer Teorema Fundamental del Cálculo
---
El teorema fundamental del cálculo establece que si $f$ es continua en el intervalo cerrado $[a,b]$ y $F$ es una antiderivada de $f$ en $[a,b]$  entonces

$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$ 

→ **Lógica del teorema:** Sumar infinitos trozos integrales entre $a$ y $b$ es lo mismo que calcular la función original en $b$ y restarle lo de la función original en $a$.

Pensándolo con un auto:

![[Pasted image 20261014171402.png]]


## El Segundo Teorema Fundamental del Cálculo
--- ^w5774x
### Previo al teorema
---
#### La integral como acumulador: Función de Acumulación $A(x)$
---
Larson y Edwards proponen una EVOLUCIÓN de la integral: dejar el límite superior como una variable $x$. 
Así, $F(x) = \int_a^x f(t) dt$ se convierte en una **función de acumulación**.

![[Pasted image 20261014155814.png|567]]

#### ¿Por qué nos sirve hacer esto?
---
Para no sacar individualmente cada integral con punto x superior distinto:

![[Pasted image 20261014181809.png]]

Aprovechamos el teorema fundamental del cálculo ($\int_{a}^{b} f(x) \, dx = F(b) - F(a)$) para simplificar la integral:

![[Pasted image 20261014181823.png]]

Y así, nos queda que el área es igual a seno de x, solo convertimos:

![[Pasted image 20261014160349.png]]

## Declaración y demostración del Segundo Teorema
---
#### Declaración
---
Si $f$ es continua en un intervalo abierto $I$ que contiene $a$, entonces para todo $x$ en el intervalo:

$\frac{d}{dx} \left[ \int_{a}^{x} f(t) \, dt \right] = f(x)$ 

Es decir, **la derivada de la integral acumulada es igual a la función original**.

#### Demostración
---

![[Pasted image 20261014171815.png]]

![[Pasted image 20261014160844.png|599]]

**Explicación:**
- Se define la derivada de $F(x)$ con la definición formal de derivada.
- Se expresan las funciones de acumulación como sus formas integrales definidas.
- Se aplica la propiedad básica de inversión entre x y a, implicando ello una suma.
- Se suman las integrales: integrar de $x$ hasta $a$ y luego seguir de $a$ hasta $x + \Delta{x}$, es lo mismo que cubrir de $x$ hasta $x+\Delta{x}$.
- **Teorema del valor medio**: El área de esa única integral sobrante se reescribe como el área de un rectángulo exacto, donde la base es delta x y la altura es el valor de la función evaluada en algún punto intermedio $c$.
	- **Evaluación del límite:** El punto $c$ está forzosamente ubicado entre $x$ y $x + \Delta x$. Cuando el límite hace que $\Delta x$ tienda a cero, el intervalo se encoge hasta desaparecer, empujando a $c$ a convertirse exactamente en $x$, lo que da como resultado final $f(x)$.


### El Teorema del Cambio Neto (Larson)
---
El teorema establece que la integral de una tasa de cambio entrega la acumulación neta de esa magnitud en un intervalo específico, no el total absoluto del sistema.

#### Demostración del teorema
---
[[Material teórico (Diego)#Antiderivadas]]

Básicamente es meter el **Segundo Teorema** dentro del **Primer Teorema**, o mejor dicho reinterpretar el primer teorema.

El teorema fundamental del cálculo establece que si $f$ es continua en el intervalo cerrado $[a,b]$ y $F$ es una antiderivada de $f$ en $[a,b]$  entonces

$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$ 

Dado que $F'(x) = f(x)$, el enunciado se puede reescribir como:

$$\int_{a}^{b} F'(x) \, dx = F(b) - F(a)$$

Donde la cantidad $F(b) - F(a)$ representa el **cambio neto** de $F$ sobre el intervalo $[a, b]$.

![[Pasted image 20261014182742.png]]

**Ejemplo**
![[Pasted image 20261014182751.png]]


# Ejemplo para el video
---

Reiterando los objetivos del video:

- El foco de la explicación y el ejemplo deben ser:
	1. Responder: ¿Qué representa la integral de una tasa de cambio?
	2. Responder: ¿La cantidad acumulada corresponde siempre a la cantidad final del sistema?
	3. Demostrar que la derivada de una acumulación (integral) es igual a la función original que se está acumulando.
	4. Enseñar cómo cambia la cantidad acumulada a medida que se amplía el límite superior x.


**Vamos con el ejemplo.**

Tomamos una función que represente una tasa de cambio entonces. En vez de $distancia / tiempo$, usaremos $velocidad/tiempo$, es decir, una función, cuya salida represente una tasa de cambio.

En distancia/tiempo, habría sido fácil decir que representaba el área bajo la función, pero acá?

Pongamos valores concretos y seamos específicos con el ejemplo: Un vehículo va por una autopista en línea recta con una aceleración de 2km/h, es decir, $f(t) = 2t$

### 1. ¿Qué represnta la integral de una tasa de cambio?
---
- La integral o el acumulado bajo el área es evidentemente la multiplicación de las magnitudes que representan los ejes vertical y horizontal, es decir, velocidad x tiempo, esto es, la distancia pura en kilómetros recorrida.

### 2. ¿La cantidad acumulada corresponde siempre a la cantidad final del sistema?
---
**NO.** La integral calcula solo la cantidad acumulada (distancia recorrida) durante el tiempo medido. No consideramos nada que venga antes del primer punto de partición $a$.

Esto es el Teorema del Cambio Neto.
[[Material teórico (Diego)#El Teorema del Cambio Neto Larson]]


### 4. ¿Cómo cambia la cantidad acumulada al ampliar el límite superior?
---
Ver Segundo Teorema del Cálculo: [[Material teórico (Diego)#^w5774x]]

Tratemos de implemenetar la acumulación variable a la función y con ello demostrar que la derivada de dicha función acumulable es igual a la función original:

Función de velocidad del auto con tiempo de partición final variable:

$$A(x) = \int_0^x 2t \, dt$$
Tal como establece el Primer Teorema del Cálculo, si aumentamos el tiempo final de partición o final del intervalo de la integral (b), el resultado nueva diferencia entre F(b) y F(a).

![[Pasted image 20261014160049.png]]

En este caso, las funciones F serían $t^2$ al ser las antiderivadas (o funciones originales) de $2t$.

### 3. La derivada de una acumulación (integral) es igual a la función original que se está acumulando
---

Ahora, lo que propone el Segundo Teorema del Cálculo, es que si derivamos la distancia acumulada, obtendremos la velocidad original:

![[Pasted image 20261014162631.png|589]]

La demostración del teorema está arriba con la descripción del procedimiento está arriba, pero aplicado al ejemplo del auto:

1. $$A'(x) = \lim_{\Delta x \to 0} \frac{A(x + \Delta x) - A(x)}{\Delta x}$$
2. $$A'(x) = \lim_{\Delta x \to 0} \frac{1}{\Delta x} \left[ \int_0^{x + \Delta x} 2t \, dt - \int_0^x 2t \, dt \right]$$
3. $$\int_0^{x + \Delta x} 2t \, dt - \int_0^x 2t \, dt = \int_x^{x + \Delta x} 2t \, dt$$
4. $$\int_x^{x + \Delta x} 2t \, dt \approx 2x \cdot \Delta x$$
5. $$A'(x) = \lim_{\Delta x \to 0} \frac{2x \cdot \Delta x}{\Delta x}$$
6. $$A'(x) = \lim_{\Delta x \to 0} [ 2x ]$$
7. $$A'(x) = 2x$$
Y se cumple efectivamente el teorema en el ejemplo también.
# EID_Calculo_Intermedio

El siguiente repositorio aloja el desarrollo de la Evaluación Integral de Desemepeño (EID) correspondiente al grupo 8 del curso *Cálculo Intermedio* del plan 3 de Ingeniería Civil en Informática, año 2026.

### Integrantes

- Diego Hernández (`ediuh`)
- Sebastián Rivera (`Srivera7483`)
- David Villegas (`David7985`)

### Tema

- **Tema:** Derivar una función de acumulación
- **Pregunta central:** ¿Por qué la derivada de una acumulación recupera la función que se está acumulando?

### Versiones y Dependencias

- **Versión de Python**: 3.14
- **Versión de Manim**: 0.18.0
- **Dependencias adicionales**: Numpy, Scipy.
- **Programas externos para generación de video:** FFmpeg.


### Escenas

Se montaron un total de 6 escenas modulares:

- *`Escena1Introduccion`*
- *`Escena2TasaDeCambio`*
- *`Escena3CambioNeto`*
- *`Escena4FuncionAcumulacion`*
- *`Escena5SegundoTeorema`*
- *`Escena6SintesisYCierre`*

Estas escenas se montaron en una sola escena compuesta global: *`VideoCompleto`*.

### Guía de ejecución

1. Asegurarse de tener instalados Python y programas para la preparación de video como los mencionados anteriormente.
2. Clonar repositorio GitHub (comando `git clone https://github.com/Srivera7483/EID_Calculo_Intermedio.git`)
3. En un entorno virtual (recomendable) o en global, instalar las dependencias con el comando `pip install -r Requiriments.txt`.
4. Ejecutar la compilación y generación del video con el comando `manim -pql escenas.py` y seleccionar la escena *`VideoCompleto`*.



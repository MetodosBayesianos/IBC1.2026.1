
# IBC1.2026.1

La materia <code>Inferencia Bayesiana Causal 1</code> se imparte como electiva en las licenciaturas y doctorados de la Escuela de Ciencia y Tecnología de la Universidad Nacional de San Martín.
Además, se ofrece como curso para la comunidad [Bayes Plurinacional](https://bayesplurinacional.org/).

0. [Introducción y objetivos](#objetivos)
0. [Programa y materiales](#programa)
0. [Cursada y evaluación](#evaluacion)
0. [Bibliografía sugerida](#biblio)

---

<a name="objetivos"></a>
## Introducción y objetivos

**Todas las ciencias con datos desarrollan argumentos causales para explicar y predecir el mundo**.
La evaluación de hipótesis causales atrae cada vez más el interés de las industrias, que necesitan medir el impacto real de sus acciones.
La ventaja de los modelos causales radica en su **capacidad predictiva, que se adapta naturalmente** a los cambios del contexto como son las intervenciones humanas.
Además sabemos que si los argumentos causales se corresponden con la realidad causal subyacente ningún modelo de inteligencia artificial, por más complejo que sea, puede mejorar su desempeño.

En este curso revisaremos los fundamentos de la **evaluación de modelos causales alternativos** $M$ dado los datos $D$, $P(M|D)$, tanto con y sin intervenciones.
Además revisaremos los métodos para hacer **predicciones de las hipótesis $H$ internas a los modelos $M$**, $P(H|D,M)$, tanto para evaluar efectos causales out-of-sample como para predecir el impacto de acciones alternativas contrafactuales.
Finalmente abordaremos el problema de **tomar decisiones óptimas como un problema de inferencia** en el que se revisa que ninguna de las decisiones contrafactuales alternativas mejoren el resultado de la variable objetivo.

Ante el vértigo de una IA plagada de herramientas efímeras, **este curso prioriza los fundamentos inmutables**.
A pesar de todos los avances, desde el siglo 18 hasta ahora no se ha propuesto un nuevo sistema para razonar bajo incertidumbre.
Si algún día las máquinas superan a los humanos, deberán hacer ciencia aplicando estrictamente las reglas de probabilidad para evaluar teorías causales.
Para alcanzar verdades (intersubjetivas) en contextos de incertidumbre, simplemente hay que saber aplicar y preservar el **principio universal de no mentir**: no afirmar más de lo que se sabe, sin ocultar lo que sí se sabe.
Así se obtienen las **distribuciones de creencia óptima dada la información disponible**, inmejorables en términos prácticos.

Al final siempre es bueno recordar que **la verdadera inteligencia** no es ni artificial ni humana, sino que **está en todas las formas de vida** que son capaces de sobrevivir en el tiempo.
Especialmente las plantas que son 83% de la biomasa, no molestan a nadie y dan vida. 
El problema real detrás de los problemas de conocimiento es responder preguntas **¿qué acciones nos generan bienestar?**.

</p>

<a name="programa"></a>
## Programa y materiales

Los contenidos completos del programa se encuentran en [su carpeta específica](https://github.com/MetodosBayesianos/IBC1.2026.1/blob/main/0-0-programa/programa.pdf).

### Unidad 1. Especificación y evaluación de argumentos causales.
#### 1.1. Argumentos causales alternativos e incertidumbre.

*Materiales*:

* [Video](https://youtu.be/5pzmCWPaRMM?si=qDESYdtz3q6Z9F-z)
* [Teórica](https://github.com/MetodosBayesianos/IBC1.2026.1/tree/main/1.1-argumentos_causales/teorica)
* [Práctica](https://github.com/MetodosBayesianos/IBC1.2026.1/tree/main/1.1-argumentos_causales/practica)

#### 1.2. Sorpresa: el problema de la comunicación con la realidad.

*Materiales*:

* [Video](https://youtu.be/2K9h6mB-xfc?si=uUAxLgBLR-HQ_3Ku)
* [Teórica](https://github.com/MetodosBayesianos/IBC1.2026.1/tree/main/1.1-argumentos_causales/teorica)
* [Práctica](https://github.com/MetodosBayesianos/IBC1.2026.1/tree/main/1.1-argumentos_causales/practica)

### Unidad 2. Métodos de inferencia y programación probabilística.

#### 2.1. nferencia exacta y pasaje de mensajes.
#### 2.2. Olvido: el problema de la inferencia aproximada

### Unidad 3. Predicciones causales.
#### 3.1. Flujo de inferencia y eliminación de la influencia espuria.
#### 3.2. Estimandos, Do-Calculus.

### Unidad 4. El zoológico de algoritmos.
#### 4.1. Métodos tradicionales.
#### 4.2. Algoritmos principales en las competencias de inferencia causal.

### Unidad 5. Tiempo.
#### 5.1. Algoritmos temporales.
#### 5.2. Modelos causales generativos temporales.

### Unidad 6. Contrafactuales.
#### 6.1. Modelos con contrafactuales y enfoques de inferencia causal.
#### 6.2. Estimación de efectos causales directos mediante contrafactuales.

### Unidad 7. Toma de decisiones.
#### 7.1. Decisiones en el tiempo: la función de costo epistémica-evolutiva.
#### 7.2. Corrección temporal de la Teoría de Utilidad Esperada.

### Unidad 8. Intervenciones socioeconómicas.
#### 8.1. Instituciones exitosas en la administración de los bienes comunes.
#### 8.2. Diseño de instrumento financiero productivo.


<a name="evaluacion"></a>
## Cursada 

**Calendario**:

- 16 semanas totales, dos por unidad.

**Días y horarios**:

- Lunes de 15h30 a 17h30 GMT-3
- Viernes de 15h30 a 17h30 GMT-3

**Lugar**:

- Virtual: https://bayesplurinacional.org/link/SalaIBC.html

**Comunicación**

- Discord de la materia: pedir acceso.
- Discord de la [comunidad Bayes Plurinacional](https://discord.gg/BPw3GX8xBg)

### Evaluación

Para las evaluaciones es necesario que tengas un **repositorio privado** (agregando al equipo docente como colaboradores) donde puedas subir la solución a los ejercicios prácticos y teóricos. Te proponemos, además, que incluyas este repositorio público como submódulo, lo que te permitirá tener actualizados los materiales de la materia haciendo pull.

Habrá evaluaciones prácticas y teóricas.

* **Prácticas**. Cada unidad tiene una práctica obligatoria que será evaluada comparando el resultado real oculto conocido por la materia. Cuando se trate de calcular distribuciones de probabilidad sobre hipótesis ocultas, se va a implementar proper scoring rules, como la entropía cruzada. En caso de que se trate de estimaciones puntuales, se utilizarán otro tipo de funciones de costo clásicas.</li>
* **Teórica**. Cada unidad tienen un _multiple choise_ sobre el que deberán distribuir creencias y justificar de forma escrita. También se evaluará usando proper scoring rules, como le entropía cruzada, que los obliga a ser honestos respecto de su propia incertidumbre.</li>

#### Guía para reconfigurar tu repositorio

Pasos:

1. **Crear tu repositorio privado** en github o gitlab y agregar el .gitignore de este repositorio público en tu reposoitorio privado.
2. **Agregar a los docentes como colaboradores** para que podamos ver tu trabajo y corregirlo. En la misma página de **`Settings`**, ve a la sección **`Collaborators`** en el menú de la izquierda. Haz clic en el botón verde **`Add people`**. Agrega a los siguientes usuarios (debes hacerlo uno por uno): `glandfried`, `gerardo1909`, `lucasbarreiroe`. Ellos recibirán una invitación por correo que deberán aceptar para tener acceso.
3. **Organización interna de los archivos**. Crea una carpeta en la raíz llamada `entregas`, idealmente ordenado con la misma estructura que el repositorio público, una carpeta por semana. Agregar en la raíz este repositorio público como un submódulo `git submodule add -f git@github.com:MetodosBayesianos/IBC1.2026.1.git materiales_del_curso`

¡Listo! Al terminar, la estructura de tu repositorio en tu computadora y en GitHub se verá así:

```
tu_repositorio/
|
|-- entregas/
|   |-- 1.1-argumentos_causales/
|   `-- ...
|
|-- materiales_del_curso/   <-- (Submódulo de éste repositorio público)
|
|-- .gitignore              <-- (Copiarlo de éste repositorio público)
`-- .gitmodules             <-- (Se genera automáticamente al agregar el submómudo)
```

<a name="biblio"></a>
## Bibliografía sugerida

### Teórica

- **Bishop, C. M. (2006). Pattern Recognition and Machine Learning.** [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
- Bishop, C. M. (2024). Deep Learning. [PDF](https://github.com/glandfried/biblio/releases/download/teca/bishop2024.pdf)
- Jaynes, E. T. (2003). Probability Theory: The Logic of Science. [PDF](http://www.med.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/JaynesProbabilityTheory.pdf)
- **Koller, D (2009). Probabilistic Graphical Models.** [PDF](http://mcb111.org/w06/KollerFriedman.pdf)
- MacKay, D. J. C. (2003). Information Theory, Inference, and Learning Algorithms. [PDF](https://www.inference.org.uk/itprnn/book.pdf)
- Pearl, J. (2009). Causality: Models, Reasoning, and Inference. [PDF](https://github.com/glandfried/biblio/releases/download/teca/pearl2009-cuasality.pdf)
- Pearl, J. (2018). The Book of Why. [PDF](https://github.com/glandfried/biblio/releases/download/teca/pearl2018-why.pdf)
- Hernán, M. A., & Robins, J. M. (2020). Causal Inference: What If. [PDF](https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf)

### Práctica

- Facure, M. (2023). Causal Inference for the Brave and True. [PDF](https://github.com/glandfried/biblio/releases/download/teca/facure2023.pdf)
- **McElreath, R. (2020). Statistical Rethinking.** [PDF](https://github.com/glandfried/biblio/releases/download/teca/mcelreath2020)
- **Molak, V. (2023). Causal Inference in Python.** [PDF](https://github.com/glandfried/biblio/releases/download/teca/molak2023-causalPython.pdf)
- Neal, B. (2020). Introduction to Causal Inference. [PDF](https://www.bradyneal.com/Introduction_to_Causal_Inference-Dec17_2020-Neal.pdf)

### Lenguajes de programación probabilística

- **Pyro**: [https://pyro.ai/](https://pyro.ai/)
- Turing: [https://turinglang.org/](https://turinglang.org/)
- **PyMC**: [https://www.pymc.io/welcome.html](https://www.pymc.io/welcome.html)
- Stan: [https://mc-stan.org/](https://mc-stan.org/)

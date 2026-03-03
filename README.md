
# IBC1.2026.1

## Materiales

1. Argumentos causales e incertidumbre: [video](https://youtu.be/5pzmCWPaRMM?si=qDESYdtz3q6Z9F-z).


## Índice

1. [Descripción general](#descripcion-general)
2. [Materia](#materia-inferencia-bayesiana-causal-1-ibc120261)
3. [Evaluación](#evaluacion)
4. [Objetivos](#objetivos)
5. [Marco Conceptual](#marco-conceptual)
6. [Programa](#programa)
7. [Guía para reconfigurar tu repositorio](#guia-para-reconfigurar-tu-repositorio)
8. [Bibliografía Recomendada](#bibliografía-recomendada)

---

<a name="descripcion-general"></a>

<p>Este es el repositorio oficial de la materia <code>Inferencia Bayesiana Causal 1</code>, 2026, primer semestre.</p>
<!--
<tr>
  <td width="50%" align="center"><img src="auxiliar/static/ecyt.jpeg" width="250"/></td>
</tr>-->





<a name="materia-inferencia-bayesiana-causal-1-ibc120261"></a>

## Materia <code>Inferencia Bayesiana Causal 1</code>. (IBC1.2026.1)

La materia <code>Inferencia Bayesiana Causal 1</code> se imparte como optativa en las licenciaturas de ciencias de datos de la Escuela de Ciencia y Tecnología de la UNSAM.

<br>

<table>
  <tr>
    <td width="50%" align="center"><img src="https://raw.githubusercontent.com/glandfried/images/master/logos/ecyt.jpeg" width="250"/></td>
    <td width="50%" align="center"><img src="https://raw.githubusercontent.com/glandfried/images/master/logos/UNSAM_blanco.png" width="250"/></td>
  </tr>
</table>



<a name="evaluacion"></a>

## Evaluación

<p>Si sos estudiante, es necesario que tengas una copia privada de este repositorio oficial (con el equipo docente como colaboradores), donde deberán subir los ejercicios y donde podrán actualizar los materiales de la materia haciendo pull del repo fuente.

<br>

Las evaluaciones se realizarán por el equipo docente, que al tener acceso a su repositorio privado tendrá acceso a sus soluciones y ejecutará tests para validar la correctitud de sus ejercicios usando diversas métricas probabilísticas.

<a name="objetivos"></a>

## Objetivos

<p>
Esta materia está enfocada en la evaluación de argumentos causales alternativos mediante la (aproximación a) la aplicación estricta de las reglas de la probabilidad, el sistema de razonamiento en contextos de incertidumbre. La materia tiene por principal objetivo revisar los métodos desarrollados en las últimas décadas para:

<ul>
<li> Especificar matemáticamente los argumentos causales expresados en lenguaje natural mediante métodos gráficos intuitivos</li>
<li> Precisar cómo la estructura causal influye en el flujo de inferencia entre las variables del modelo.</li>
<li> Identificar el efecto causal entre variables de un modelo causal en base de datos observacionales (sin intervenciones).</li>
<li> Diseñar experimentos que permitan evaluar teorías causales alternativos</li>
<li> Seleccionar decisiones óptimas en ciclos de acción-percepción con una naturaleza oculta (simulada).</li>
</ul>

El problema real detrás de este problema de conocimiento es responder preguntas esenciales como **¿Qué acciones generan bienestar?**.

</p>


<a name="marco-conceptual"></a>

## Marco Conceptual

<p>

<strong>Definición de Inferencia</strong>. Las "verdades" son proposiciones válidas para todas las personas. Las ciencias con datos deben validar sus proposiciones (hipótesis) en sistemas naturales abiertos. ¿Tiene sentido hablar de "verdad" si justamente tenemos incertidumbre respecto de su valor real? Al menos podemos evitar mentir: no afirmar más de lo que se sabe (maximizando incertidumbre) sin ocultar todo aquello que sí se sabe (dada la información disponible o restricciones).

<br>

<strong>Definición de Bayes</strong>. Evaluación de todo el espacio de hipótesis mediante la (aproximación a la) aplicación estricta de las reglas de la probabilidad: preservar la creencia previa que sigue siendo compatible con los datos (regla del producto) y predecir con la contribución de todas las hipótesis (regla de la suma). Debido al costo computacional de las reglas de la probabilidad, durante el siglo 20 propusieron una gran cantidad criterios arbitrarios de selección de hipótesis, que genera siempre efectos secundarios indeseados como ocurre con el overfitting. Afortunadamente, la aplicación estricta de las reglas de la probabilidad no exhiben estos problemas. Si lo hicieran, no tendríamos aún un sistema de razonamiento para contexto de incertidumbre.

<br>

<strong>Definición de Causal</strong>. El problema real de todo organismo vivo es orientar el ciclo de acción-percepción con la naturaleza en favor de su reproducción, supervivencia y bienestar. Los problemas del conocimiento científico obtienen su relevancia y jerarquía de los objetivos que persigue alcanzar. Luego de una percepción evaluamos los argumentos causales alternativos maximizando la incertidumbre dada la información disponible, y antes de actuar seleccionamos la acción minimizando la incertidumbre esperada en relación al objetivo que perseguimos.

</p>

<a name="programa"></a>

## Programa
<h4>Unidad 1. Argumentos causales alternativos e incertidumbre.</h4>
<p>Especificación y evaluación de modelos causales (Monty Hall y Base). Modelos adaptativos al contexto, estructura invariante del dato empírico y entropía cruzada.</p>

<h4>Unidad 2. Métodos de inferencia.</h4>
<p>Inferencia exacta, pasaje de mensajes y algoritmo suma-producto. Inferencia aproximada (Expectation Propagation, Variational Inference, MCMC) y lenguajes de programación probabilística.</p>

<h4>Unidad 3. Predicciones causales.</h4>
<p>Flujo de inferencia y eliminación de asociación espuria (d-separation, backdoor). Estimandos y Do-Calculus (adjustment formula, frontdoor, variables instrumentales).</p>

<h4> Unidad 4. El zoológico de algoritmos.</h4>
<p>Métodos tradicionales (Matching, IPW). Algoritmos de competencia (CausalML, Meta-Learners, Causal Forest, Double Machine Learning) y estimación de efectos heterogéneos.</p>

<h4>Unidad 5. Tiempo.</h4>
<p>Algoritmos temporales (Difference-in-Differences, Synthetic Control). Modelos causales generativos temporales (HMM, TrueSkill Through Time, smoothing).</p>

<h4>Unidad 6. Contrafactuales.</h4>
<p>Twin Networks y equivalencia entre enfoques (Potential Outcomes vs SCM). Descomposición de efectos (Directos e Indirectos) y Mediation Formula.</p>

<h4>Unidad 7. Toma de decisiones.</h4>
<p>Función de costo epistémica-evolutiva (Criterio Kelly). Corrección temporal de la Teoría de Utilidad Esperada y optimización como inferencia. Micro experimentos.</p>

<h4>Unidad 8. Intervenciones socioeconómicas.</h4>
<p>Instituciones exitosas y bienes comunes. Diseño de instrumento financiero-productivo (ahorro, ordenamiento territorial, ciclo de reproducción).</p>

<a name="guia-para-reconfigurar-tu-repositorio"></a>

## Guía para reconfigurar tu repositorio

En este curso vamos a usar una configuración novedosa de tu repositorio de entregas, que te da control total, mantiene tu trabajo privado y te permite sincronizar los materiales de la cátedra fácilmente.

Sigue estos pasos **una sola vez** con atención.

### Parte 1: Convertir tu fork en un repositorio privado.

Primero, vamos a desvincular tu repositorio de la red de forks para poder cambiar su visibilidad.

1.  Ve a la página principal de **tu fork** en GitHub.
2.  Haz clic en la pestaña **`Settings`**.
3.  Baja hasta el final, a la sección roja llamada **`Danger Zone`**.
4.  **Desvincular el Fork**: Haz clic en el botón **`Leave fork network`**.
    * GitHub te pedirá que leas unas advertencias y que confirmes escribiendo el nombre de tu repositorio.
5.  **Cambiar Visibilidad**: Una vez desvinculado, la opción **`Change visibility`** (la primera en la `Danger Zone`) estará activa.
    * Haz clic en ella y selecciona la opción para hacerlo **`Private`**.

### Parte 2: Agregar a los docentes como colaboradores.

Para que podamos ver tu trabajo y corregirlo, debes agregarnos como colaboradores.

1.  En la misma página de **`Settings`**, ve a la sección **`Collaborators`** en el menú de la izquierda.
2.  Haz clic en el botón verde **`Add people`**.
3.  Agrega a los siguientes usuarios (debes hacerlo uno por uno):
    * `glandfried`
    * `gerardo1909`
    * `lucasbarreiroe`
4.  Ellos recibirán una invitación por correo que deberán aceptar para tener acceso.

### Parte 3: Reorganizar tus archivos y agregar el repositorio de la materia como un submódulo.

Agregar el respositorio de la materia como submodulo te va a permitir tener los materiales en una simple carpeta y mantenerlos actualizados a medida que avanza la cursada.
Esto te permite trabajar libremente en el resto de tu repositorio sin que se produzca conflicto alguno con la actualización del repositorio de la materia.
Para poder automatizar las correcciones, vamos a pedir que tus entregas estén adentro de una carpeta llamada `entregas`.
Ahora vamos a organizar la estructura de archivos de tu repositorio desde tu computadora usando la línea de comandos.

1.  Crea una nueva carpeta llamada `entregas`.

  ```bash
  mkdir entregas
  ```

2.  Mueve **todo el contenido que tenías antes** (tus notebooks, el `README.md`, etc.) a la nueva carpeta `entregas`.

  ```bash
  # USA ESTE COMANDO UNA SOLA VEZ
  # Moverá todos los archivos y carpetas (excepto los ocultos como .git) a 'entregas/'
  git mv * entregas/
  ```

  *Nota: Si el comando anterior da un error porque no puede mover la carpeta `entregas` dentro de sí misma, no te preocupes, es normal. Verifica que el resto de tus archivos se haya movido.*

3.  Agrega el repositorio original de la materia como un **submódulo**. Esto creará una carpeta `materiales_del_curso` que podrás actualizar para recibir nuevo contenido de la cátedra.

  ```bash
  # Este comando conecta tu repo con el de la materia
  git submodule add -f https://github.com/MetodosBayesianos/IBC1.2026.1.git materiales_del_curso
  ```

4.  Finalmente, guarda y sube todos estos cambios estructurales a GitHub.

  ```bash
  git commit -m "Reestructura a repo privado y agrega submódulo de materiales"
  git push
  ```

#### Estructura Final

¡Listo! Al terminar, la estructura de tu repositorio en tu computadora y en GitHub se verá así:

```
/tu_repositorio
|
|-- /entregas/
|   |-- 0-previa/
|   `-- README.md
|
|-- /materiales_del_curso/  <-- (Submódulo con los contenidos de la cátedra)
|
`-- .gitmodules               <-- (Archivo de configuración del submódulo)
```

# Bibliografía Recomendada

- Bishop, C. M. (2006). Pattern Recognition and Machine Learning. [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
- Bishop, C. M. (2024). Aprendizaje estadístico y modelado probabilístico. [PDF](https://github.com/glandfried/biblio/releases/download/teca/bishop2024.pdf)
- Jaynes, E. T. (2003). Probability Theory: The Logic of Science. [PDF](http://www.med.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/JaynesProbabilityTheory.pdf)
- MacKay, D. J. C. (2003). Information Theory, Inference, and Learning Algorithms. [PDF](https://www.inference.org.uk/itprnn/book.pdf)
- Pearl, J. (2009). Causality: Models, Reasoning, and Inference. [PDF](https://github.com/glandfried/biblio/releases/download/teca/pearl2009-cuasality.pdf)
- Pearl, J. (2018). The Book of Why. [PDF](https://github.com/glandfried/biblio/releases/download/teca/pearl2018-why.pdf)
- Hernán, M. A., & Robins, J. M. (2020). Causal Inference: What If. [PDF](https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf)
- Facure, M. (2023). Causal Inference for the Brave and True. [PDF](https://github.com/glandfried/biblio/releases/download/teca/facure2023.pdf)
- McElreath, R. (2020). Statistical Rethinking. [PDF](https://github.com/glandfried/biblio/releases/download/teca/mcelreath2020)
- Molak, V. (2023). Causal Inference in Python. [PDF](https://github.com/glandfried/biblio/releases/download/teca/molak2023-causalPython.pdf)
- Neal, B. (2020). Introduction to Causal Inference. [PDF](https://www.bradyneal.com/Introduction_to_Causal_Inference-Dec17_2020-Neal.pdf)

### Lenguajes de programación probabilística

- Pyro: [https://pyro.ai/](https://pyro.ai/)
- Turing: [https://turinglang.org/](https://turinglang.org/)
- PyMC: [https://www.pymc.io/welcome.html](https://www.pymc.io/welcome.html)
- Stan: [https://mc-stan.org/](https://mc-stan.org/)

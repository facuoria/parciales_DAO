[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/toM85Sq6)
# Sistema de Gestión de Cursos Universitarios

Una universidad necesita un sistema para administrar los cursos dictados.

• **Cursos teóricos**: tienen un precio base por estudiante. Si superan los 50 alumnos, se descuenta un 10%.

• **Cursos prácticos**: tienen un precio base más $500 adicionales por cada práctica de laboratorio .

• **Cursos online**: tienen un precio base + 15% adicional si incluyen tutorías personalizadas.

## Archivo cursos.csv:

    • Tipo de curso (1 = teórico, 2 = práctico, 3 = online)
    • Código del curso
    • Nombre del curso
    • Precio base por estudiante
    • Cantidad de alumnos
    • Extra (prácticas de laboratorio o tutorías)

## Funcionalidades:

    1. Cargar cursos desde archivo.
    2. Calcular el promedio entero de precio por estudiante.
    3. Obtener el curso más caro.
    4. Calcular el ingreso total de la universidad.
    5. Contar cuántos cursos teóricos superan 50 alumnos.
    6. Contar cuántos cursos online incluyen tutorías.
    7. Calcular en un diccionario la cantidad de cursos de cada tipo, las claves del diccionario deben ser "Teórico", "Práctico" y "Online".

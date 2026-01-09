#  Automatización del campo "Añadir Kit" de la aplicación Urban Grocers

Comprobación del campo name en la solicitud de creación de un kit de productos de la aplicación Urban Groceries.


## Descripción general
<p>


Este proyecto está enfocado en la automatización de pruebas funcionales para validar el correcto comportamiento del campo “Añadir Kit” dentro de la aplicación Urban Grocers, específicamente en el proceso de creación de kits de productos a través de su API.

El objetivo es asegurar, mediante pruebas automatizadas, que el sistema gestione de forma correcta los distintos valores de entrada, cumpla con las reglas de negocio y mantenga la estabilidad del servicio
</p>

Objetivo del proyecto

Implementar pruebas automatizadas que permitan:

Validar el funcionamiento del campo “Añadir Kit” bajo diferentes condiciones.

Garantizar la correcta creación de kits de productos.

Detectar defectos de manera temprana en el flujo de creación.

Reducir la dependencia de pruebas manuales mediante automatización.

Alcance de la automatización

La automatización de pruebas cubre los siguientes procesos clave:

Automatización de la creación de usuarios, necesaria para ejecutar solicitudes autenticadas.

Automatización del flujo de creación de kits, enviando solicitudes HTTP que incluyen el campo “Añadir Kit”.

Validación de respuestas de la API, verificando códigos de estado, estructura de la respuesta y mensajes devueltos.

Escenarios de prueba automatizados

Se desarrollaron distintos escenarios de prueba automatizados, entre los que se incluyen:

Pruebas positivas, donde el campo “Añadir Kit” cumple con los criterios establecidos.

Pruebas negativas, donde el campo recibe valores inválidos, vacíos o fuera de los parámetros permitidos.

Estos escenarios permiten evaluar la robustez del sistema ante diferentes tipos de entrada.

Tecnologías y herramientas utilizadas

Python como lenguaje principal para la automatización.

Pytest como framework de pruebas automatizadas.

Requests para el envío de solicitudes HTTP.

REST API para la validación de servicios.

Estructura modular para facilitar el mantenimiento y escalabilidad de los tests.

Estructura del proyecto

El repositorio se encuentra organizado de la siguiente manera:

configuration.py – Configuración del entorno y endpoints.

create_kit_name_kit.py – Casos de prueba automatizados para el campo “Añadir Kit”.

data.py – Datos de prueba y escenarios de entrada.

sender_stand_request.py – Envío y manejo de solicitudes HTTP.

README.md – Documentación del proyecto.

.gitignore – Archivos excluidos del control de versiones.

Ejecución de las pruebas automatizadas
1. Preparación de datos

Antes de ejecutar las pruebas, verifica que en el archivo data.py estén correctamente definidos:

create_user_body

headers

kit_name

kit_body (escenarios del 1 al 9)

2. Ejecución con Pytest

Las pruebas están diseñadas para ejecutarse con Pytest, permitiendo una ejecución rápida y repetible.

Al ejecutar las pruebas, el resultado esperado es:

5 pruebas positivas exitosas

4 pruebas negativas correctamente validadas

Valor del proyecto

Este proyecto demuestra la automatización de pruebas como eje central del aseguramiento de calidad, evidenciando cómo los tests automatizados permiten validar reglas de negocio, mejorar la calidad del software y optimizar los procesos de testing en aplicaciones basadas en APIs.







-

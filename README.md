Integrantes del grupo: Dirie Cesar Luis, Frutos Agostina Madelein, Granich Erika Ludmila, Castillo Catalina

Comisión: K1.2

Grupo: B2

Descripcion general del sistema: El sistema desarrollado es una solución de consola en Python diseñada para automatizar la gestión operativa de una caja de supermercado. El software permite centralizar las transacciones comerciales diarias, facilitando tanto el proceso de venta como el control de inventario.
Las funcionalidades principales del sistema incluyen:
Gestión de Ventas: Registro dinámico de productos mediante códigos, control de stock en tiempo real y aplicación de promociones comerciales (2x1 en artículos seleccionados).
Validaciones y Seguridad: Implementación de manejo de excepciones para garantizar la integridad de los datos ingresados por el usuario y evitar la interrupción del flujo ante errores de tipeo.
Cálculo Automático: Procesamiento de subtotales, aplicación automática de descuentos por volumen (10% de descuento en compras superiores a $10.000) y cálculo preciso del total de cada ticket.
Reporting y Estadísticas: Generación de un reporte diario que incluye la cantidad de clientes atendidos, el total recaudado, el desglose de ventas por producto, la identificación del producto "estrella" (más vendido) y un historial detallado de las operaciones realizadas.

Instrucciones de ejecución: 
* Asegurate de tener instalado Python en tu computadora.
* Descargá el código y abrí una terminal en esa carpeta.
* Ejecutalo con el comando: python main.py
* Seguí las opciones del menú que aparece en pantalla para cargar productos, ver ventas o cerrar el sistema.

Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto, hemos integrado herramientas de Inteligencia Artificial (ChatGPT y Google Gemini) como apoyo al aprendizaje y al proceso de desarrollo. El uso de estas herramientas se ha llevado a cabo bajo los siguientes criterios:

* **Organización del código:** Utilizamos IA para consultar sugerencias sobre la modularización del sistema y cómo estructurar correctamente las funciones para cumplir con los estándares de limpieza y legibilidad solicitados en la cátedra.
* **Depuración y análisis de errores (Debugging):** La IA fue utilizada como una herramienta de apoyo para identificar causas raíz ante errores de ejecución (como excepciones de tipo `ValueError` durante el ingreso de datos) y para comprender cómo implementar correctamente bloques de manejo de errores (`try/except`).
* **Buenas prácticas:** Consultamos sobre la implementación de PEP8 y cómo optimizar la lógica de los acumuladores y contadores utilizados para las estadísticas del supermercado.

**Compromiso del equipo:**
Todo el equipo comprende integralmente la lógica implementada, el flujo de ejecución y las validaciones de datos presentes en el código fuente. La asistencia de la IA fue utilizada de forma crítica; cada sugerencia proporcionada fue analizada, validada y, en muchos casos, adaptada manualmente por nosotros para asegurar que el sistema cumpliera con las necesidades específicas del Escenario 12 y con las exigencias pedagógicas de la materia.

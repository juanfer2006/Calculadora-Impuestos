# Creadores:
Heiver David Ruales Luna

Juan Fernando Castañeda Agudelo

# Entrega 5:

Juan Fernando Castañeda Agudelo

Kevin Andres Silva Bedoya

# ¿Qué es y para qué es?

Este proyecto es una aplicación diseñada para calcular el impuesto de una compra, considerando diferentes factores como el valor de la compra, el porcentaje de IVA, descuentos, y el costo adicional de las bolsas plásticas. El propósito principal de este proyecto es realizar estos cálculos de manera eficiente, asegurando que los datos proporcionados sean correctos a través de excepciones personalizadas, las cuales validan los parámetros antes de proceder con el cálculo.

# ¿Cómo lo hago funcionar?

- Prerrequisitos: Antes de ejecutar este proyecto, debes asegurarte de tener instalado Python en tu máquina. Este proyecto no depende de bibliotecas externas, por lo que no se necesitan instalaciones adicionales fuera del entorno estándar de Python.
- Ejecucion: Pasos para Ejecutar el Programa:
  1. Descargar o Clonar el Proyecto: Si no tienes el proyecto, clónalo o descárgalo y descomprímelo en tu máquina local.
  2. Navegar a la Carpeta del Proyecto: Abre una terminal o línea de comandos y navega hasta la carpeta raíz del proyecto: "cd ruta\del\proyecto"
  3. Ejecutar el Programa: Para ejecutar el cálculo de impuestos, usa el siguiente comando en la carpeta del proyecto: "py src\view\console\console.py"

# Ejecucion de interfaz grafica:
  1. Descargar o Clonar el Proyecto: Si no tienes el proyecto, clónalo o descárgalo y descomprímelo en tu máquina local.
  2. Navegar a la Carpeta del Proyecto: Abre una terminal o línea de comandos y navega hasta la carpeta raíz del proyecto: "cd ruta\del\proyecto"
  3. Ejecutar desde la carpeta del proyecto el siguiente comando:
     ```bash
     python src\view\gui\taxes_gui.py
     ```

# ¿Cómo está hecho?

Arquitectura del Proyecto
- Model: Maneja la lógica del negocio y los datos del programa.
- View: Se encarga de la presentación y la interacción con el usuario.
- Controller: Gestiona la comunicación entre la vista y el modelo.
- Carpeta tests: Pruebas Unitarias

# Uso
Para ejecutar las pruebas unitarias, desde la carpeta raiz, use el comando "py test\test.py".

# Ejecución de la Aplicación Web Localmente con Base de Datos en Blanco

# Configuración de la base de datos
Para esta aplicación, se utiliza Neon como servicio de base de datos PostgreSQL. Debes crear una cuenta en Neon y configurar un nuevo proyecto. Al crear el proyecto, Neon te proporcionará una URL de conexión que deberás usar para conectar la aplicación a la base de datos.

Dentro de tu proyecto local, debes crear un archivo de configuración donde colocarás esta URL para que la aplicación pueda acceder a la base de datos.

# Creación de las tablas en la base de datos
Una vez configurada la conexión, la aplicación cuenta con mecanismos para crear automáticamente las tablas necesarias en la base de datos vacía. Esto se realiza mediante la ejecución de scripts o pruebas que inicializan la estructura de la base de datos con los modelos definidos.

Asegúrate de que esta creación de tablas se haya completado exitosamente antes de iniciar la aplicación para evitar errores en la ejecución.

# Ejecución de la aplicación web
Para iniciar la aplicación web localmente, desde la carpeta raíz del proyecto debes ejecutar el archivo principal que contiene la configuración del servidor web. Esto levantará el servidor Flask en modo desarrollo, generalmente accesible a través de la dirección local en el puerto 5000.

Una vez que el servidor esté corriendo, podrás abrir tu navegador y acceder a la interfaz web mediante la dirección indicada para interactuar con la aplicación.

# Uso de la aplicación web

Desde la interfaz web, podrás ingresar datos relacionados con las compras y sus respectivos impuestos. Estos datos se procesarán, calcularán los impuestos correspondientes y se almacenarán en la base de datos configurada en Neon.

Notas importantes
Si realizas cambios en la estructura de datos o modelos, recuerda actualizar o recrear las tablas en la base de datos para mantener la consistencia con la aplicación.

Para detener el servidor web, simplemente cierra la terminal o usa la combinación de teclas para detener la ejecución del programa.

# Escenarios Específicos para Cálculo de Impuestos

# Casos Normales

# 1. Cálculo del IVA para una Factura

- Entradas: Valor de la compra: $1,000,000, Porcentaje de IVA: 19%

- Salida Esperada: IVA a pagar: $190,000

# 2. Cálculo del IVA para una Factura Pequeña

- Entradas: Valor de la compra: $200,000, Porcentaje de IVA: 19%

- Salida Esperada: IVA a pagar: $38,000

# 3. Cálculo del IVA para una Factura con Descuento

- Entradas: Valor de la compra: $1,500,000, Descuento: 10%, Porcentaje de IVA: 19%

- Salida Esperada: IVA a pagar: $256,500

# Casos Extraordinarios

# 4. Cálculo del IVA con Tasa Cero

- Entradas: Valor de la compra: $500,000, Porcentaje de IVA: 0%

- Salida Esperada: IVA a pagar: $0

# 5. Cálculo del IVA con Valor en Moneda Extranjera

- Entradas: Valor de la compra: 1,200 USD, Tipo de cambio: 4,500 COP/USD, Porcentaje de IVA: 19%

- Salida Esperada: IVA a pagar: $1,026,000 COP

- Descripción: El cálculo debe tomar en cuenta el tipo de cambio para convertir el valor de la compra a la moneda local antes de aplicar el IVA.

# 6. Cálculo del IVA con Impuesto a las Bolsas Plásticas

- Entradas: Valor de la compra: $150,000, Cantidad de bolsas plásticas: 3, Costo del impuesto por bolsa: $65 (valor estimado para 2024), IVA 19%

- Salida Esperada: Total a pagar: $178,695

# Casos de Error

# 7. Valor de la Compra Negativo para Cálculo de IVA

- Entradas: Valor de la compra: -$1,000,000, Porcentaje de IVA: 19%

- Salida Esperada: Error: "El valor de la compra no puede ser negativo"

# 8. Porcentaje de IVA Incorrecto

- Entradas: Valor de la compra: $1,000,000, Porcentaje de IVA: 150%

- Salida Esperada: Error: "El porcentaje de IVA no es válido"

# 9. Monto de Compra en Formato Incorrecto

- Entradas: Valor de la compra: 'Un millón de pesos', Porcentaje de IVA: 19%

- Salida Esperada: Error: "Formato de número inválido para el valor de la compra"

# 10. IVA en formato incorrecto

- Entradas: Valor de la compra: $1,000,000, Porcentaje de IVA: Diecinueve%

- Salida Esperada: Error: "Formato de número de IVA inválido"

# Archivo Excel:
https://1drv.ms/x/s!AqPSu27mK3cQpvgaka5NFwccxsHz1w?e=ahm3ae

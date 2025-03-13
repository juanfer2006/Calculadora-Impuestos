# Creadores:
Heiver David Ruales Luna

Juan Fernando Castañeda Agudelo

# ¿Qué es y para qué es?

Este proyecto es una aplicación diseñada para calcular el impuesto de una compra, considerando diferentes factores como el valor de la compra, el porcentaje de IVA, descuentos, y el costo adicional de las bolsas plásticas. El propósito principal de este proyecto es realizar estos cálculos de manera eficiente, asegurando que los datos proporcionados sean correctos a través de excepciones personalizadas, las cuales validan los parámetros antes de proceder con el cálculo.

# ¿Cómo lo hago funcionar?

- Prerrequisitos: Antes de ejecutar este proyecto, debes asegurarte de tener instalado Python en tu máquina. Este proyecto no depende de bibliotecas externas, por lo que no se necesitan instalaciones adicionales fuera del entorno estándar de Python.
- Ejecucion: Pasos para Ejecutar el Programa:
  1. Descargar o Clonar el Proyecto: Si no tienes el proyecto, clónalo o descárgalo y descomprímelo en tu máquina local.
  2. Navegar a la Carpeta del Proyecto: Abre una terminal o línea de comandos y navega hasta la carpeta raíz del proyecto: "cd ruta/del/proyecto"
  3. Ejecutar el Programa: Para ejecutar el cálculo de impuestos, usa el siguiente comando: "py src/taxes.py"

# ¿Cómo está hecho?

- Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
- Carpeta tests: Pruebas Unitarias




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

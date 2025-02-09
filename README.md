# Calculadora-Impuestos

# Escenarios Específicos

# 1.	Factura estándar nacional con IVA, Impuesto Nacional al Consumo y retenciones nacionales:

-	Monto positivo.

-	IVA del 19%.

-	Impuesto Nacional al Consumo del 8%.
  
-	Retención del 3.5% que se resta del total.
  
# 2.	Factura internacional con retención externa:

-	Venta al extranjero.
  
-	IVA exento.
  
-	Retención del 2% que se suma al total.
  
# 3.	Nota crédito por devolución total:

-	Monto negativo equivalente al valor de una factura original.

-	IVA y retenciones aplicadas de forma inversa.

# 4.	Nota crédito por devolución parcial:

-	Monto negativo parcial.

-	Cálculo proporcional del IVA y retenciones.

# 5.	Factura sin impuestos:
   
-	Producto exento de IVA e Impuesto Nacional al Consumo.

-	Sin retenciones.

# 6.	Factura con error en el valor base:

-	Base imponible incorrecta para verificar validación de errores.
  
# 7.	Factura con múltiples productos con diferentes tasas de IVA:

-	Productos al 0%, 5% y 19%.
  
-	Validación del cálculo por separado y suma total.

# Casos de Prueba

# Casos Normales:

# 1.	Factura nacional estándar:
-	Valor base: $1,000,000.
-	IVA: $190,000.
-	Impuesto Nacional al Consumo: $80,000.
-	Retención nacional (3.5%): $35,000 (se resta).
-	Total esperado: $1,235,000.
  
# 2.	Factura internacional con retención externa:
-	Valor base: $500,000.
-	IVA: $0.
-	Retención internacional (2%): $10,000 (se suma).
-	Total esperado: $510,000.
  
# 3.	Factura sin impuestos:
-	Valor base: $300,000.
-	Sin IVA, sin Impuesto Nacional al Consumo, sin retenciones.
-	Total esperado: $300,000.

  
# Casos Extraordinarios:

# 1.	Nota crédito por devolución total:
-	Valor base: -$1,000,000.
-	IVA: -$190,000.
-	Retención: -$35,000.
-	Total esperado: -$1,235,000.
  
# 2.	Nota crédito por devolución parcial:
-	Valor base: -$400,000.
-	IVA: -$76,000.
-	Retención: -$14,000.
-	Total esperado: -$490,000.
  
# 3.	Factura con múltiples tasas de IVA:
-	Producto A: $200,000 al 0%.
-	Producto B: $300,000 al 5% ($15,000).
-	Producto C: $500,000 al 19% ($95,000).
-	Total esperado: $1,110,000.

  
# Casos de Error:

# 1.	Valor base negativo sin nota crédito:
-	Resultado esperado: Error de validación.
# 2.	Tasa de IVA no válida (ej. 25%):
-	Resultado esperado: Error de validación.
# 3.	Retención internacional marcada como nacional:
-	Resultado esperado: Error de configuración.
# 4.	Factura sin base imponible:
-	Resultado esperado: Error de cálculo, falta de datos obligatorios.


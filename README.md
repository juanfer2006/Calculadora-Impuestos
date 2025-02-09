# Calculadora-Impuestos

# Escenarios Específicos
# 1.	Factura estándar nacional con IVA, Impuesto Nacional al Consumo y retenciones nacionales:

o	Monto positivo.
o	IVA del 19%.
o	Impuesto Nacional al Consumo del 8%.
o	Retención del 3.5% que se resta del total.
2.	Factura internacional con retención externa:
o	Venta al extranjero.
o	IVA exento.
o	Retención del 2% que se suma al total.
3.	Nota crédito por devolución total:
o	Monto negativo equivalente al valor de una factura original.
o	IVA y retenciones aplicadas de forma inversa.
4.	Nota crédito por devolución parcial:
o	Monto negativo parcial.
o	Cálculo proporcional del IVA y retenciones.
5.	Factura sin impuestos:
o	Producto exento de IVA e Impuesto Nacional al Consumo.
o	Sin retenciones.
6.	Factura con error en el valor base:
o	Base imponible incorrecta para verificar validación de errores.
7.	Factura con múltiples productos con diferentes tasas de IVA:
o	Productos al 0%, 5% y 19%.
o	Validación del cálculo por separado y suma total.
Casos de Prueba
Casos Normales:
1.	Factura nacional estándar:
o	Valor base: $1,000,000.
o	IVA: $190,000.
o	Impuesto Nacional al Consumo: $80,000.
o	Retención nacional (3.5%): $35,000 (se resta).
o	Total esperado: $1,235,000.
2.	Factura internacional con retención externa:
o	Valor base: $500,000.
o	IVA: $0.
o	Retención internacional (2%): $10,000 (se suma).
o	Total esperado: $510,000.
3.	Factura sin impuestos:
o	Valor base: $300,000.
o	Sin IVA, sin Impuesto Nacional al Consumo, sin retenciones.
o	Total esperado: $300,000.
Casos Extraordinarios:
1.	Nota crédito por devolución total:
o	Valor base: -$1,000,000.
o	IVA: -$190,000.
o	Retención: -$35,000.
o	Total esperado: -$1,235,000.
2.	Nota crédito por devolución parcial:
o	Valor base: -$400,000.
o	IVA: -$76,000.
o	Retención: -$14,000.
o	Total esperado: -$490,000.
3.	Factura con múltiples tasas de IVA:
o	Producto A: $200,000 al 0%.
o	Producto B: $300,000 al 5% ($15,000).
o	Producto C: $500,000 al 19% ($95,000).
o	Total esperado: $1,110,000.
Casos de Error:
1.	Valor base negativo sin nota crédito:
o	Resultado esperado: Error de validación.
2.	Tasa de IVA no válida (ej. 25%):
o	Resultado esperado: Error de validación.
3.	Retención internacional marcada como nacional:
o	Resultado esperado: Error de configuración.
4.	Factura sin base imponible:
o	Resultado esperado: Error de cálculo, falta de datos obligatorios.


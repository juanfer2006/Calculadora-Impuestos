import logging
import traceback
from flask import Blueprint, render_template, request, redirect, url_for

# Configura logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),  # Logs a archivo
        logging.StreamHandler()  # Logs a consola
    ]
)
plano = Blueprint( "vista_usuarios", __name__, "templates" )
import sys
sys.path.append("src")
from controller.calculator_controller import CalculatorController
# Importa las clases desde su ubicación correcta
from src.model.calculator import TaxRecord, User, Taxes
# Otra forma de importar (dependiendo de tu estructura)
from src.model.calculator import (
    TaxRecord,
    User,
    ErrorValueNegative,
    ErrorIncorrectIVA,
    ErrorDiscount,
    ErrorStringIva,
    ErrorPorcentage
)

@plano.route("/")
def Home():
   return render_template("index.html")

@plano.route("/hola")
def hola():
    return render_template('hola.html')

@plano.errorhandler(Exception)
def controlar_errores(err):
    return "Ocurrió un error: "+ str(err)

@plano.route('/buscar', methods=["GET"])
def buscar():
    id = request.args.get('id')
    resultado = CalculatorController.search(id)

    if resultado:
        return render_template('buscar.html', user=resultado['user'], purchases=resultado['purchases'])
    else:
        return render_template('buscar.html', error="Usuario no encontrado")

@plano.route('/lista_de_compras')
def lista_de_compras():
    return render_template('lista_de_compras.html')

@plano.route('/insertar', methods=["GET"])
def mostrar_formulario_insertar():
    return render_template('insertar.html')

@plano.route('/insertar_usuario', methods=["POST"])
def insertar_usuario():
    try:
        user_id = request.form.get('user_id')
        user_name = request.form.get('user_name')
        
        # Aquí creas el objeto User (asegúrate de importar tu clase User)
        user = User(id=user_id, name=user_name)
        
        # Insertas el usuario
        CalculatorController.insert(user)
        
        return render_template('insertar.html', 
                            user_message="Usuario insertado correctamente", 
                            user_success=True)
    except Exception as e:
        return render_template('insertar.html', 
                            user_message=f"Error al insertar usuario: {str(e)}", 
                            user_success=False)

@plano.route('/insertar_compra', methods=["POST"])
def insertar_compra():
    try:
        # Obtener datos del formulario
        tax_record = TaxRecord(
            user_id=request.form.get('user_id'),
            purchase=float(request.form.get('purchase')),
            porcentage=float(request.form.get('porcentage')),
            discount=float(request.form.get('discount', 0)),
            plastic_bags=int(request.form.get('plastic_bags', 0)),
            currency=request.form.get('currency'),
            tax_value=0  # Se calculará automáticamente
        )
        
        # Verificar si el usuario existe
        if not CalculatorController.search(tax_record.user_id):
            return render_template('insertar.html', 
                                purchase_message="Error: El usuario no existe", 
                                purchase_success=False)
        
        # Insertar la compra (incluye validación y cálculo de impuestos)
        CalculatorController.insert_tax(tax_record)
        
        return render_template('insertar.html', 
                            purchase_message="Compra insertada correctamente. Impuesto calculado: " + str(tax_record.tax_value), 
                            purchase_success=True)
    
    except ErrorValueNegative as e:
        return render_template('insertar.html', 
                            purchase_message=f"Error: {str(e)}", 
                            purchase_success=False)
    
    except ErrorIncorrectIVA as e:
        return render_template('insertar.html', 
                            purchase_message=f"Error: {str(e)}", 
                            purchase_success=False)
    
    except ErrorDiscount as e:
        return render_template('insertar.html', 
                            purchase_message=f"Error: {str(e)}", 
                            purchase_success=False)
    
    except ErrorStringIva:
        return render_template('insertar.html', 
                            purchase_message="Error: El porcentaje debe ser un número", 
                            purchase_success=False)
    
    except ErrorPorcentage:
        return render_template('insertar.html', 
                            purchase_message="Error: El valor de compra debe ser un número", 
                            purchase_success=False)
    
    except Exception as e:
        return render_template('insertar.html', 
                            purchase_message=f"Error inesperado: {str(e)}", 
                            purchase_success=False)
    
@plano.route('/modificar')
def mostrar_modificar():
    return render_template('modificar.html')

@plano.route('/buscar_modificar', methods=["GET"])
def buscar_modificar():
    id = request.args.get('id')
    resultado = CalculatorController.search(id)
    
    if resultado:
        return render_template('modificar.html', 
                             user=resultado['user'], 
                             purchases=resultado['purchases'])
    else:
        return render_template('modificar.html', 
                             error="Usuario no encontrado")

@plano.route('/actualizar_compra', methods=["POST"])
def actualizar_compra():
    try:
        # 1. Depuración inicial
        print("\n=== DATOS RECIBIDOS ===")
        print(dict(request.form))

        # 2. Validación de campos requeridos
        required_fields = {
            'compra_id': int,
            'user_id': str,
            'purchase': float,
            'porcentage': float
        }
        
        # Verificar campos faltantes
        missing_fields = [field for field in required_fields if field not in request.form]
        if missing_fields:
            raise ValueError(f"Campos requeridos faltantes: {', '.join(missing_fields)}")

        # 3. Conversión y validación de datos
        try:
            compra_id = int(request.form['compra_id'])
            user_id = request.form['user_id']
            purchase = float(request.form['purchase'])
            porcentage = int(request.form['porcentage'])  # Cambiado a int para coincidir con los valores 0,5,19
            discount = float(request.form.get('discount', 0))
            plastic_bags = int(request.form.get('plastic_bags', 0))
            currency = request.form.get('currency', 'COP')
        except (ValueError, TypeError) as e:
            raise ValueError(f"Error en tipos de datos: {str(e)}")

        # 4. Validaciones de negocio
        if not user_id.strip():
            raise ValueError("ID de usuario no válido")
            
        if compra_id < 0:
            raise ValueError("ID de compra no válido")
            
        if purchase <= 0:
            raise ValueError("El valor de compra debe ser positivo")
            
        if porcentage not in [0, 5, 19]:
            raise ValueError("El porcentaje debe ser 0, 5 o 19")
            
        if discount < 0 or discount > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        # 5. Lógica de actualización
        new_data = {
            'purchase': purchase,
            'porcentage': porcentage,
            'discount': discount,
            'plastic_bags': plastic_bags,
            'currency': currency,
            'tax_value': Taxes.calculate(
                purchase=purchase,
                porcentage=porcentage,
                discount=discount,
                plastic_bag=plastic_bags,
                currency=currency
            )
        }

        # Debug: Mostrar datos que se actualizarán
        print("\n=== DATOS PARA ACTUALIZAR ===")
        print(f"ID Compra: {compra_id}")
        print("Nuevos valores:", new_data)

        # 6. Actualizar en base de datos
        CalculatorController.update_purchase(compra_id, new_data)
        
        # 7. Redirección exitosa con mensaje
        return redirect(url_for('vista_usuarios.buscar_modificar', 
                             id=user_id,
                             success="¡Compra actualizada correctamente!"))
        
    except ValueError as e:
        print(f"\n=== ERROR DE VALIDACIÓN ===")
        print(f"Error: {str(e)}")
        return render_template('modificar.html', 
                            error=f"Datos inválidos: {str(e)}",
                            form_data=request.form)
    except Exception as e:
        print(f"\n=== ERROR INESPERADO ===")
        print(f"Tipo: {type(e).__name__}")
        print(f"Mensaje: {str(e)}")
        print(f"Traceback: {traceback.format_exc()}")
        return render_template('modificar.html', 
                            error="Error interno al procesar la solicitud",
                            form_data=request.form)
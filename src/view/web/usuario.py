import logging
import traceback
from flask import Blueprint, render_template, request, redirect, url_for
from model import db  

# Configura logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

plano = Blueprint("vista_usuarios", __name__, "templates")

import sys
sys.path.append("src")

from controller.calculator_controller import CalculatorController

from src.model.calculator import (
    TaxRecord,
    User,
    ErrorValueNegative,
    ErrorIncorrectIVA,
    ErrorDiscount,
    ErrorStringIva,
    ErrorPorcentage,
    Taxes
)

@plano.route("/")
def Home():
    return render_template("index.html")

@plano.route("/hola")
def hola():
    return render_template('hola.html')

@plano.errorhandler(Exception)
def controlar_errores(err):
    return "Ocurrió un error: " + str(err)

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

        user = User(id=user_id, name=user_name)
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
        tax_record = TaxRecord(
            user_id=request.form.get('user_id'),
            purchase=float(request.form.get('purchase')),
            porcentage=float(request.form.get('porcentage')),
            discount=float(request.form.get('discount', 0)),
            plastic_bags=int(request.form.get('plastic_bags', 0)),
            currency=request.form.get('currency'),
            tax_value=0
        )

        if not CalculatorController.search(tax_record.user_id):
            return render_template('insertar.html',
                                   purchase_message="Error: El usuario no existe",
                                   purchase_success=False)

        # Calcular impuesto antes de insertar
        tax_record.tax_value = Taxes.calculate(
            purchase=tax_record.purchase,
            porcentage=tax_record.porcentage,
            discount=tax_record.discount,
            plastic_bag=tax_record.plastic_bags,
            currency=tax_record.currency
        )

        # 1. Guardar en la lógica interna
        CalculatorController.insert_tax(tax_record)

        # 2. Guardar en la base de datos real
        from model.db_models import TaxRecord as DBTaxRecord
        new_tax = DBTaxRecord(
            user_id=tax_record.user_id,
            purchase=tax_record.purchase,
            porcentage=tax_record.porcentage,
            discount=tax_record.discount,
            plastic_bags=tax_record.plastic_bags,
            currency=tax_record.currency,
            tax_value=tax_record.tax_value
        )
        db.session.add(new_tax)
        db.session.commit()

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
        db.session.rollback()
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

@plano.route('/actualizar_usuario', methods=['POST'])
def actualizar_usuario():
    try:
        original_id = request.form.get('original_id')
        new_id = request.form.get('user_id')
        new_name = request.form.get('user_name')

        if not original_id or not new_id or not new_name:
            raise ValueError("Todos los campos son obligatorios.")

        CalculatorController.update_user(original_id, new_id, new_name)

        return redirect(url_for('vista_usuarios.buscar_modificar', id=new_id, success="¡Usuario actualizado correctamente!"))

    except Exception as e:
        return render_template('modificar.html', error=f"Error al actualizar usuario: {str(e)}")

@plano.route('/actualizar_compra', methods=["POST"])
def actualizar_compra():
    try:
        required_fields = {
            'compra_id': int,
            'user_id': str,
            'purchase': float,
            'porcentage': float
        }

        missing_fields = [field for field in required_fields if field not in request.form]
        if missing_fields:
            raise ValueError(f"Campos requeridos faltantes: {', '.join(missing_fields)}")

        compra_id = int(request.form['compra_id'])
        user_id = request.form['user_id']
        purchase = float(request.form['purchase'])
        porcentage = int(request.form['porcentage'])
        discount = float(request.form.get('discount', 0))
        plastic_bags = int(request.form.get('plastic_bags', 0))
        currency = request.form.get('currency', 'COP')

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

        CalculatorController.update_purchase(compra_id, new_data)

        return redirect(url_for('vista_usuarios.buscar_modificar',
                                id=user_id,
                                success="¡Compra actualizada correctamente!"))

    except ValueError as e:
        return render_template('modificar.html',
                               error=f"Datos inválidos: {str(e)}",
                               form_data=request.form)
    except Exception as e:
        return render_template('modificar.html',
                               error="Error interno al procesar la solicitud",
                               form_data=request.form)

@plano.route('/crear_tablas')
def crear_tablas():
    try:
        from model import db
        from src.model.calculator import User, TaxRecord

        db.create_all()
        return render_template('crear_tablas.html', mensaje="✅ Tablas creadas correctamente en PostgreSQL")
    except Exception as e:
        return render_template('crear_tablas.html', mensaje=f"❌ Error al crear tablas: {str(e)}")
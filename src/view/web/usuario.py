from flask import Blueprint, render_template, request

plano = Blueprint( "vista_usuarios", __name__, "templates" )
import sys
sys.path.append("src")
from controller.calculator_controller import CalculatorController

@plano.route("/")
def Home():
   return render_template("index.html")

@plano.route("/hola")
def hola():
    return render_template('hola.html')

@plano.errorhandler(Exception)
def controlar_errores(err):
    return "Ocurrió un error: "+ str(err)

@plano.route('/buscar')
def buscar():
    return render_template('buscar.html')

@plano.route('/lista_de_compras')
def lista_de_compras():
    return render_template('lista_de_compras.html')
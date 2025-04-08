from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

# Asegúrate de que Taxes y calc_payment estén correctamente definidos en model/calculator.py
from model.calculator import Taxes

class PaymentApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, row_force_default=True, row_default_height=100)

        contenedor.add_widget(Label(text="Ingresar valor de la compra"))
        self.compra = TextInput(font_size=40)
        contenedor.add_widget(self.compra)

        contenedor.add_widget(Label(text="Ingresar porcentaje de IVA"))
        self.cuotas = TextInput(font_size=40)
        contenedor.add_widget(self.cuotas)

        contenedor.add_widget(Label(text="Ingresar descuento"))
        self.tasa = TextInput(font_size=40)
        contenedor.add_widget(self.tasa)
        
        contenedor.add_widget(Label(text="Ingresar cantidad de bolsas plasticas"))
        self.tasa = TextInput(font_size=40)
        contenedor.add_widget(self.tasa)
        
        contenedor.add_widget(Label(text="Ingresar moneda: US o COP"))
        self.tasa = TextInput(font_size=30)
        contenedor.add_widget(self.tasa)

        self.resultado = Label()
        contenedor.add_widget(self.resultado)

        calcular = Button(text="Calcular", font_size=30)
        contenedor.add_widget(calcular)

        # Conectar el callback con el evento press del botón
        calcular.bind(on_press=self.calcular_cuota)

        # Siempre se retorna el widget que contiene a todos los demás
        return contenedor
    
    def calcular_cuota(self, instance):
        try:
            self.validar()
            cuota = Taxes.calc_payment(amount=float(self.compra.text), number_of_payments=int(self.cuotas.text), interest=float(self.tasa.text))
            self.resultado.text = str(round(cuota, 2))

        except ValueError as err:
            self.resultado.text = "El valor ingresado no es un número válido. Ingrese un número correcto, por ejemplo 500000.00"
        except Exception as err:
            self.mostrar_error(err)
        
    def mostrar_error(self, err):
        """ 
        Abre una ventana emergente, con un texto y un botón para cerrar 
        Parámetros: 
        err: Mensaje de error que queremos mostrar en la ventana        
        """
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
        popup = Popup(title="Error", content=contenido)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

    def validar(self):
        """
        Verifica que todos los datos ingresados por el usuario sean correctos
        """
        try:
            float(self.compra.text)  # Verifica que sea un número
        except ValueError:
            raise Exception("El Valor de la compra debe ser un número válido")

        try:
            int(self.cuotas.text)  # Verifica que sea un número entero
        except ValueError:
            raise Exception("El Número de Cuotas debe ser un número válido")

        try:
            float(self.tasa.text)  # Verifica que sea un número
        except ValueError:
            raise Exception("La tasa de interés debe ser un número válido, sin signo de porcentaje")

if __name__ == "__main__":
    PaymentApp().run()
    
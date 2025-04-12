import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

import sys
sys.path.append("src")


from model.calculator import Taxes

# Asegúrate de que el path esté bien si estás ejecutando desde otra carpeta
from model.calculator import Taxes, ErrorValueNegative, ErrorIncorrectIVA, ErrorDiscount, ErrorPorcentage, ErrorStringIva

class TaxCalculatorForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text='Valor de la compra:'))
        self.purchase_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.purchase_input)

        self.add_widget(Label(text='Porcentaje de IVA:'))
        self.iva_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.iva_input)

        self.add_widget(Label(text='Descuento (%):'))
        self.discount_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.discount_input)

        self.add_widget(Label(text='Cantidad de bolsas plásticas:'))
        self.bags_input = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.bags_input)

        self.add_widget(Label(text='Moneda (COP o USD):'))
        self.currency_input = TextInput(multiline=False)
        self.add_widget(self.currency_input)

        self.result_label = Label(text='Resultado:')
        self.add_widget(self.result_label)

        self.calc_button = Button(text='Calcular IVA')
        self.calc_button.bind(on_press=self.calculate_tax)
        self.add_widget(self.calc_button)

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def calculate_tax(self, instance):
        try:
            purchase = float(self.purchase_input.text)
            porcentage = float(self.iva_input.text)
            discount = float(self.discount_input.text) if self.discount_input.text else 0
            plastic_bag = int(self.bags_input.text) if self.bags_input.text else 0
            currency = self.currency_input.text.upper().strip()

            result = Taxes.calculate(purchase, porcentage, discount, plastic_bag, currency)
            self.result_label.text = f'Valor de la cuota: {result:.2f}'

        except ValueError:
            self.show_popup("Error", "Entrada inválida. Asegúrese de usar números válidos.")
        except (ErrorValueNegative, ErrorIncorrectIVA, ErrorDiscount, ErrorPorcentage, ErrorStringIva) as e:
            self.show_popup("Error de cálculo", str(e))
        except Exception as e:
            self.show_popup("Error inesperado", str(e))


class TaxCalculatorApp(App):
    def build(self):
        return TaxCalculatorForm()

if __name__ == '__main__':
    TaxCalculatorApp().run()

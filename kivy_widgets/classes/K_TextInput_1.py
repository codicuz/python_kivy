# Виджет TextInput имеет ряд свойств, которые позволяют задать вводимому тексту параметры шрифта:
# – text – текст (текстовое содержимое поля ввода.);
# – font_size – размер шрифта;
# – color – цвет шрифта;
# – font_name – имя файла с пользовательским шрифтом (.ttf);
# – password – скрывать вводимые символы (при значении свойства True);
# – password_mask – маска символа (символ, который скрывает вводимый текст)

from kivy.app import App
from kivy.uix.textinput import TextInput

class MainApp(App):
	def build (self):
		my_text = TextInput (font_size=30)
		return my_text
		
MainApp().run()
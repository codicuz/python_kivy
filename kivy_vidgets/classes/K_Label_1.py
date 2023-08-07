# Метка Label имеет ряд свойств, которые позволяют задать выводимый текст и параметры шрифта:
# – text – текст, выводимый в видимую часть виджета (текстовое содержимое метки, надпись на кнопке и т.п.);
# – font_size – размер шрифта;
# – color – цвет шрифта;
# – font_name – имя файла с пользовательским шрифтом (.ttf)'''

from kivy.app import App
from kivy.uix.label import Label

class MainApp (App):
	def build (self):
		L = Label (text='Это текст', font_size=50)
		return L

MainApp().run()
# Флажок CheckBox имеет ряд свойств, которые позволяют задать цвет и запустить реакцию на изменение состояния:
# – color – цвет флажка (в формате r, g,b,a);
# – active – состояние в виде логического значения (True – когда флажок поставлен, False – когда флажок снят).

from kivy.app import App
from kivy.uix.checkbox import CheckBox

class MainApp (App):
	def build(self):
		checkbox = CheckBox()
		return checkbox

MainApp().run()
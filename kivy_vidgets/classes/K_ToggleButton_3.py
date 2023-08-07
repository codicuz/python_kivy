# Кнопки ToggleButton могут быть сгруппированы для создания группы переключателей. В этом случае только одна кнопка в группе может находиться в «нажатом» состоянии. Имя группы может быть строкой с произвольным содержанием.

from kivy.app import App
from kivy.lang import Builder
KV = '''
BoxLayout:
	orientation: 'vertical'
	ToggleButton:
		text: 'Москва'
		group: 'city'
		state: 'down'
	ToggleButton:
		text: 'Воронеж'
		group: 'city'
	ToggleButton:
		text: 'Сочи'
		group: 'city'
'''

class MainApp(App):
	def build (self):
		return Builder.load_string(KV)

MainApp().run()
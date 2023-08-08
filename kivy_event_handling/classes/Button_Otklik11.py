# Явное связывание визуального элемента с функцией отклика на действия пользователя

from kivy.app import App
from kivy.lang import Builder

KV = '''
Button:
	text: 'Кнопка'
	size_hint: .5, .5
	pos_hint: {'center_x': .5, 'center_y': .5}
	on_press: app.press_button(root)
'''

class MainApp(App):
	def build(self):
		return Builder.load_string(KV)
	
	def press_button(self, instance):
		print ('Вы нажали на кнопку!')

MainApp().run()
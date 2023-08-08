# Явное связывание визуального элемента с функцией отклика на действия пользователя

from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
	def build(self):
		button = Button(
			text='Кнопка',
			size_hint = (.5, .5),
			pos_hint= {'center_x': .5, 'center_y': .5}
		)
		
		button.bind(on_press=self.press_button)
		
		return button

	def press_button (self, instance):
		print('Вы нажали на кнопку!')
		
MainApp().run()
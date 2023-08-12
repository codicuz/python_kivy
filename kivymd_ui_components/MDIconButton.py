from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
	MDIconButton:
		#icon: 'language-python'
		icon: '../resources/images/main_icon.png'
		user_font_size: '64sp'
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_color
		pos_hint: {'center_x': .5, 'center_y': .5}
		on_press: print('Кнопка нажата')
		on_release: print('Кнопка отпущена')
'''


class MainApp(MDApp):
 	def build(self):
 		return Builder.load_string(KV)

MainApp().run()
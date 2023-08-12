from kivy.app import App
from kivy.lang import Builder 

my_str = '''
Label:
	text: ('Загрузка метки из текстовой строки')
	font_size: '16pt'
	'''

kv_str = Builder.load_string(my_str)

class Basic_Class (App):
	def build (self):
		return kv_str

My_App = Basic_Class()
My_App.run()
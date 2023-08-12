from kivy.app import App
from kivy.lang import Builder

kv_file = Builder. load_file ('KV_file/main_screen.kv')

class Basic_Class (App):
	def build (self):
		return kv_file

My_App = Basic_Class()
My_App.run()
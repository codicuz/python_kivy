from kivy.app import App
from kivy.lang import Builder

KV = '''
Image:
	source: '../../resources/images/devops.png'
'''

class MainApp(App):
	def build(self):
			return Builder.load_string(KV)

MainApp().run()
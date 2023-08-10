from kivy.app import App
from kivy.lang import Builder

KV = '''
RelativeLayout:
	canvas:
		Rectangle:
			source: '../../resources/background.jpg'
			size: self.size
			pos: self.pos
	Scatter:
		Image:
			source: '../../resources/devops.png'
'''

class MainApp(App):
	def build(self):
		return Builder.load_string(KV)

MainApp().run()
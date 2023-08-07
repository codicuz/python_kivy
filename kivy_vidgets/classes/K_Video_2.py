from kivy.app import App
from kivy.lang import Builder

KV = '''
Video:
	source: '../resources/video.mp4'
	play: True
'''

class MainApp(App):
	def build(self):
		return Builder.load_string(KV)
		
MainApp().run()
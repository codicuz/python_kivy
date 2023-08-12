from kivy.app import App
from kivy.lang import Builder

KV = '''
<Picture@ScatterLayout>:
	source: None
	size: image.size
	size_hint: None, None
	
	Image:
		id: image
		source: root.source

RelativeLayout:
	canvas:
		Rectangle:
			source: '../resources/images/background.jpg'
			size: self.size
			pos: self.pos
	Picture:
		source: '../resources/images/dog.png'
	Picture:
		source: '../resources/images/cat.png'
	Picture:
		source: '../resources/images/bird.png'
'''

class MyApp(App):
	def build(self):
		return Builder.load_string(KV)

MyApp().run()
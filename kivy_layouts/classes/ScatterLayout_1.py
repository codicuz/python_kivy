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
			source: '../../resources/background.jpg'
			size: self.size
			pos: self.pos
	Picture:
		source: '../../resources/dog.png'
	Picture:
		source: '../../resources/cat.png'
	Picture:
		source: '../../resources/bird.png'
'''

class MyApp(App):
	def build(self):
		return Builder.load_string(KV)

MyApp().run()
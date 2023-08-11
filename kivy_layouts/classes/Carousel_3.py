from kivy.app import App
from kivy.lang import Builder

KV = '''
Carousel:
    direction: 'right'
    canvas:
        Rectangle:
            source: '../../resources/background.jpg'
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: '../../resources/dog.png'
    BoxLayout:
        Image:
            source: '../../resources/cat.png'
    BoxLayout:
        Image:
            source: '../../resources/bird.png'
    BoxLayout:
        Image:
            source: '../../resources/devops.png'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
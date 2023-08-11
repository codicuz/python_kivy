from kivy.app import App
from kivy.lang import Builder

KV = '''
Carousel:
    direction: 'right'
    canvas:
        Rectangle:
            source: '../../resources/images/background.jpg'
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: '../../resources/images/dog.png'
    BoxLayout:
        Image:
            source: '../../resources/images/cat.png'
    BoxLayout:
        Image:
            source: '../../resources/images/bird.png'
    BoxLayout:
        Image:
            source: '../../resources/images/devops.png'
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
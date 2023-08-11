from kivy.lang import Builder
from kivy.app import App

KV = '''
Carousel:
    direction: 'right'
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
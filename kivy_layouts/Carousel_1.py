from kivy.lang import Builder
from kivy.app import App

KV = '''
Carousel:
    direction: 'right'
    BoxLayout:
        Image:
            source: '../resources/images/dog.png'
    BoxLayout:
        Image:
            source: '../resources/images/cat.png'
    BoxLayout:
        Image:
            source: '../resources/images/bird.png'
    BoxLayout:
        Image:
            source: '../resources/images/devops.png'
'''


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

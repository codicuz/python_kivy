from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDCarousel:
    direction: 'right'
    loop: True
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

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
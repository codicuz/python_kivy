from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Стили надписей'
        MDLabel:
            text: 'Текст 1'
            font_style: 'H1'
        MDLabel:
            text: 'Текст 2'
            font_style: 'H2'
        MDLabel:
            text: 'Текст 64'
            font_size: 64
            font_name: '../resources/fonts/1-cataneo-bt.ttf'
        MDLabel:
            text: 'Текст 32'
            font_size: 32
            font_name: '../resources/fonts/1-cataneo-bt.ttf'
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
from kivy. app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = """
MyBox:
    Button:
        text: "Кнопка 2"
"""

class MyBox(BoxLayout):...

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

def run_k_my_class2():
    MainApp().run()
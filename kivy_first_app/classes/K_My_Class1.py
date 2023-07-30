from kivy. app import App
from kivy.lang import Builder

KV = """
BoxLayout:
    Button:
        text: "Кнопка 1"
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

def run_k_my_class1():
    MainApp().run()
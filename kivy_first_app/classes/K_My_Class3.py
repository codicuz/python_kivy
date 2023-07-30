from kivy. app import App
from kivy.lang import Builder

KV = """
<MyBox@BoxLayout>

MyBox:
    Button:
        text: "Кнопка 3"
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

def run_k_my_class3():
    MainApp().run()
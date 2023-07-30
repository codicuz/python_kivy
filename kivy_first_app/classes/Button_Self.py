from kivy. app import App
from kivy.lang import Builder

KV = """
BoxLayout:
    Button:
        text: "Состояние кнопки - %s"% self.state
"""

class MainApp(App):
    def build(self):
            return Builder.load_string(KV)

def run_button_self():
      MainApp().run()
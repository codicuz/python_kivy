from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainAppMD(MDApp):
    def build(self):
        self.icon = 'kivy_first_app/resources/icons/main_icon.png'
        self.title = 'Приложение на KivyMD'
        label = MDLabel(text="Привет от KivyMD и Python!", halign="center")
        return label

def runMainAppMD():
    app = MainAppMD()
    app.run()

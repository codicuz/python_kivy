from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainAppMD(MDApp):
    def build(self):
        self.icon = "../resources/images/main_icon.png"
        self.title = 'Приложение на KivyMD'
        label = MDLabel(text="Привет от KivyMD и Python!", halign="center")
        return label


app = MainAppMD()
app.run()

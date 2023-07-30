from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.icon = "kivy_first_app/resources/icons/main_icon.png"
        self.title = "Приложение на Kivy"
        label = Label(text="Привет от Kivy и Python!")
        
        return label

def runMainApp():
    app = MainApp()
    app.run()

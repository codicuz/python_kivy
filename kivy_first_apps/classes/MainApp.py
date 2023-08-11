from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.icon = "../../resources/images/main_icon.png"
        self.title = "Приложение на Kivy"
        label = Label(text="Привет от Kivy и Python!")
        
        return label

app = MainApp()
app.run()

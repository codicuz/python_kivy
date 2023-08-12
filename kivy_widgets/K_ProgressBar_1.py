# Индикатор ProgressBar имеет ряд свойств, которые позволяют задать и получить некоторые параметры:
# – max – максимальное значение;
# – value – текущее значение

from kivy.app import App
from kivy.uix.progressbar import ProgressBar


class MainApp(App):
    def build(self):
        Progress = ProgressBar(max=1000)
        Progress.value = 650
        return Progress


MainApp().run()

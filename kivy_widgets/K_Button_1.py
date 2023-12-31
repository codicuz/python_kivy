# Кнопка Button имеет ряд свойств, которые позволяют задать надпись на кнопке, параметры шрифта, и запустить реакцию на события или изменение состояния:
# – text – надпись на кнопке;
# – font_size – размер шрифта;
# – color – цвет шрифта;
# – font_name – имя файла с пользовательским шрифтом (.ttf).
# – on_press – событие, возникает, когда кнопка нажата;
# – on_release – событие, возникает, когда кнопка отпущена;
# – on_state – состояние (изменяется тогда, когда кнопка нажата или отпущена).

from kivy.app import App
from kivy.uix.button import Button


class MainApp (App):
    def build(self):
        btn = Button(text='Это кнопка', font_size=50)
        return btn


MainApp().run()

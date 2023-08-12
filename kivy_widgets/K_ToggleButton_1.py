# Кнопка ToggleButton имеет ряд свойств, которые позволяют задать надпись на кнопке, параметры шрифта, и запустить реакцию на события или изменение состояния:
# – text – надпись на кнопке;
# – font_size – размер шрифта;
# – color – цвет шрифта;
# – font_name – имя файла с пользовательским шрифтом (.ttf).
# – on_press – событие, возникает, когда кнопка нажата;
# – on_release – событие, возникает, когда кнопка отпущена;
# – on_state – состояние (изменяется тогда, когда кнопка нажата или отпущена);
# – group – задание имени группы (текстовая строка, например ’city’);
# – state – задание состояние кнопки (’down’ – нажата).

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton


class MainApp(App):
    def build(self):
        t_but = ToggleButton(text='Кнопка', font_size=50)
        return t_but


MainApp().run()

# виджет GridLayout имеет следующий набор свойств:
# – cols – количество колонок (столбцов);
# – rows – количество строк;
# – col_default_width – минимальная ширина столбца;
# – row_default_height – минимальная высота строки.
# – size_hint_x – относительный размер дочернего элемента по горизонтали;
# – size_hint_y – относительный размер дочернего элемента по вертикали;
# – size_hint – относительный размер дочернего элемента по горизонтали и по вертикали (например, size_hint: 0.5, 0.3);
# – col_force_default – если свойство имеет значение True, то будет проигнорирована ширина (size_hint_x) дочернего элемента и использована ширину столбца по умолчанию.
# – row_force_default: если свойство имеет значение True, то будет проигнорирована высота (size_hint_y) дочернего элемента и использована высота строки, заданная по умолчанию;
# – padding (отступ) – задает величину отступа виджета от границ его родительского контейнера (в пикселах).
# – spacing (интервал) – расстояние между дочерними элементами, находящимися внутри контейнера (в пикселях).
# – Orientation (ориентация) – порядок заполнения ячеек таблицы (допустимые значения «lr-tb’, «tb-lr’, «rl-tb’, «tb-rl’, «lr-bt’, «bt-lr’, «rl-bt’ and «bt-rl’, по умолчанию «lr-tb’).
# Примечание.
# ’lr’ означает слева направо. ’rl’ означает справа налево. «tb» означает «сверху вниз». «bt» означает «снизу вверх».

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    def build(self):
        grid = GridLayout(cols=2, rows=2)
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        btn3 = Button(text='Кнопка 3')
        btn4 = Button(text='Кнопка 4')
        grid.add_widget(btn1)
        grid.add_widget(btn2)
        grid.add_widget(btn3)
        grid.add_widget(btn4)
        return grid


MyApp().run()

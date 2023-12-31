# виждет BoxLayout имеет следующие свойства:
# – orientation: – ориентация, или порядок расположения дочерних элементов (’vertical’ – вертикальное, ’horizontal’ – горизонтальное);
# – padding (отступ) – задает величину отступа виджета от границ его родительского контейнера (в пикселах).
# – spacing (интервал) – расстояние между дочерними элементами, находящимися внутри контейнера (в пикселях).

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp (App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        # layout = BoxLayout(orientation='horizontal')
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout


MyApp().run()

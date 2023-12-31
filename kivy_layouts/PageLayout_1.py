# виджет PageLayout имеет следующий набор свойств и событий:
# – Page – текущая (отображаемая) страница;
# – Border – ширина границы вокруг текущей страницы, используемая для отображения областей пролистывания (предыдущей/следующей страницы);
# – on_touch_down – событие (касание страницы);
# – on_touch_move – событие (касание с перемещением);
# – on_touch_up – событие (завершение касания страницы).

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class MyApp (App):
    def build(self):
        pg = PageLayout()
        box1 = BoxLayout()
        box2 = BoxLayout()
        box3 = BoxLayout()
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        btn3 = Button(text='Кнопка 3')
        box1.add_widget(btn1)
        box2.add_widget(btn2)
        box3.add_widget(btn3)
        pg.add_widget(box1)
        pg.add_widget(box2)
        pg.add_widget(box3)

        return pg


MyApp().run()

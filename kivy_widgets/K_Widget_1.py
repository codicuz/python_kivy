# Объект Widget имеет ряд свойств, которые позволяют задать и получить некоторые параметры:
# – canvas – встроенный объект, имеющий инструкции (важно – пишется с маленькой буквы);
# – Color – инструкция для задания цвета виджета (важно – пишется с большой буквы);
# – rgba – свойство (цвет виджета), задается в формате r, g, b, a;
# – Rectangle – инструкция для задания свойств рамки виджета (важно – пишется с большой буквы);
# – source – источник (путь и имя файла с изображением, которое можно поместить в рамку);
# – size – размер (указывается – self.size, иметь размер рамки, как у родительского виджета);
# – pos – положение (указывается – self. pos, иметь положение рамки, как у родительского виджета).

from kivy.app import App
from kivy.uix.widget import Widget


class MainApp(App):
    def build(self):
        wid = Widget()
        return wid


MainApp().run()

# Виджет ScatterLayout имеет тот же набор свойств, что и Scatter:
# – do_rotation – выполнять вращение (True – разрешить, False – запретить);
# – do_translation – выполнять перемещение (True – разрешить, False – запретить);
# – do_scale – выполнять масштабирование (True – разрешить, False – запретить);
# – bring_to_front – сделать дочерний элемент активным и выдвинуть его на передний план.

from kivy.app import App
from kivy.lang import Builder

KV = '''
RelativeLayout:
	canvas:
		Rectangle:
			source: '../resources/images/background.jpg'
			size: self.size
			pos: self.pos
	ScatterLayout:
		Image:
			source: '../resources/images/devops.png'
'''


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

# виджет Scatter имеет следующие свойства:
# – do_rotation – выполнять вращение (True – разрешить, False – запретить);
# – do_translation – выполнять перемещение (True – разрешить, False – запретить);
# – do_scale – выполнять масштабирование (True – разрешить, False – запретить);
# – bring_to_front – сделать дочерний элемент активным и выдвинуть его на передний план.

from kivy. app import App
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter 

class MainApp(App):
	def build(self):
		rl = RelativeLayout()
		sct = Scatter()
		img = Image(source='../../resources/devops.png')
		sct.add_widget(img)
		rl.add_widget(sct)
		return rl

MainApp().run()
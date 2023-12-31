# Относительные величины
# Свойства используются для задания размеров и положения виджетов:
# – text – надпись на элементе;
# – size_hint – относительный размер элемента (например, size_hint:.5,.5);
# – pos_hint – относительное положение элемента в окне приложения (например, центра – pos_hint: {’center_x’:.5, ’center_y’:.5} или левого нижнего угла
# – pos_hint: {’x’:.5, ’y’:.5}).
# – size_hint: None, None – отменить использование автоматической перерисовки элемента (подгонку под размер родительского виджета);
# – size – абсолютный размер элемента в пикселах, например, size:
# 150, 50 (150 – ширина элемента, 50 – высота элемента);
# – pos – абсолютная позиция элемента в окне приложения в пикселах, например, pos: 140, 40 (140 – координата по оси x, 40 – координата по оси y).

from kivy.app import App
from kivy.lang import Builder

KV = '''
Button:
	text: 'Это кнопка'
	#size_hint: .5, .5
	#size_hint: .8, .5 
	#size_hint: .5, .8
	#pos_hint: {'center_x': .5, 'center_y': .5}
	size_hint: .2, .1
	#pos_hint: {'center_x': .15, 'center_y': .5}
	#pos_hint: {'center_x': .85, 'center_y': .5}
	#pos_hint: {'center_x': .5, 'center_y': .15}
	pos_hint: {'center_x': .5, 'center_y': .85}
'''


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

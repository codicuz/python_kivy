# виджет имеет следующие свойства:
# – current_slide – текущий слайд:
# – direction – направление пролистывания;
# – loop – организовать пролистывание в цикле;
# – on_touch_down – возникает при касании виджета
# – on_touch_up – возникает, когда касание исчезает
# – on_touch_move возникает при касании с перемещением.
# – scroll_distance – расстояние прокрутки;
# – scroll_timeout – таймаут (время ожидания прокрутки).

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # создать объект
        carousel = Carousel(direction='right')
        img = Image(source='../resources/images/cat.png')
        carousel.add_widget(img)
        img = Image(source='../resources/images/dog.png')
        carousel.add_widget(img)
        img = Image(source='../resources/images/bird.png')
        carousel.add_widget(img)
        img = Image(source='../resources/images/devops.png')
        carousel.add_widget(img)
        return carousel

MainApp().run()
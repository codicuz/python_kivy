from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.carousel import MDCarousel

class MainApp(MDApp):
    def build(self):
        # создать объект
        carousel = MDCarousel(direction='right')
        img = Image(source='../../resources/images/dog.png')
        carousel.add_widget(img)
        img = Image(source='../../resources/images/cat.png')
        carousel.add_widget(img)
        img = Image(source='../../resources/images/bird.png')
        carousel.add_widget(img)
        img = Image(source='../../resources/images/devops.png')
        carousel.add_widget(img)
        return carousel

MainApp().run()
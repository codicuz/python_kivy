from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDRectangleFlatButton:
        text: 'КНОПКА'
        font_size: '25sp'
        theme_text_color: 'Custom'
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 0
        pos_hint: {'center_x':.5, 'center_y':.5}
        on_press: print('Кнопка нажата')
        on_release: print('Кнопка отпущена')
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

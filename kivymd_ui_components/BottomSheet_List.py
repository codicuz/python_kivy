from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.app import MDApp

KV = '''
Screen:
    MDTopAppBar:
        title: 'Пример BottomSheet'
        pos_hint: {'top': 1}
        elevation: 10
    MDRaisedButton:
        text: 'Открыть в виде списка'
        on_release: app.show_example_list_bottom_sheet()
        pos_hint: {'center_x':.5, 'center_y':.5}
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet()
        for i in range(1, 11):
            bottom_sheet_menu.add_item(f'Элемент списка {i}', lambda x, y=i: self.callback_for_menu_items(
                f'Выбран элемент списка {y}'),)

        bottom_sheet_menu.open()


MainApp().run()

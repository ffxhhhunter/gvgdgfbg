from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder
from pyrogram import Client

Builder.load_string('''
<ErrorPopup>:
    size_hint: 0.6, 0.3
    title: "Ошибка"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: error_label
            color: 1, 0, 0, 1
            halign: 'center'
            text_size: self.width, None
            size: self.texture_size
''')

class ErrorPopup(Popup):
    pass

class JoinApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.url_input = TextInput(hint_text="Введите текст", multiline=False)
        join_button = Button(text="Присоединиться", on_press=self.join_button_pressed)
        layout.add_widget(self.url_input)
        layout.add_widget(join_button)
        return layout
    
    def join_button_pressed(self, instance):
        url = self.url_input.text

        try:
            app = Client("my_account", api_id=24443601, api_hash="2e7b8af649b6d4c27bae489b01f92899")
            app.start()
            app.join_chat(url)
            app.stop()
        except Exception as e:
            error_popup = ErrorPopup()
            error_label = error_popup.ids.error_label
            error_label.text = str(e)
            error_popup.open()

            # Очистить поле ввода
            self.url_input.text = ''

JoinApp().run()

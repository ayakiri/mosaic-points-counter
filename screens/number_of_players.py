from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class NumberOfPlayers(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text='Wpisz ilość graczy')
        self.text_input = TextInput(hint_text='Ilość graczy')
        button = Button(text='Potwierdź', on_press=self.switch_to_players_registration)

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)

        self.add_widget(layout)

    def switch_to_players_registration(self, instance):
        self.manager.current = 'players_registration'

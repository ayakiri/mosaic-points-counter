from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class Logo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text='Mosaic - Punktacja Gry')
        layout.add_widget(label)
        self.add_widget(layout)

    def on_enter(self):
        Clock.schedule_once(self.switch_to_number_of_players_declaration, 2)

    def switch_to_number_of_players_declaration(self, dt):
        self.manager.current = 'number_of_players_declaration'

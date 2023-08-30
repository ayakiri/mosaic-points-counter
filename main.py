from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from game import Game
from screens.logo_screen import Logo
from screens.number_of_players import NumberOfPlayers

game = Game()


class PlayersRegistration(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text='Proszę wpisz imiona graczy')
        button = Button(text='Potwierdź')
        button.bind(on_press=self.switch_to_game)

        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)

    def switch_to_game(self, instance):
        self.manager.current = 'game'


class MosaicApp(App):
    def build(self):
        screen_manager = ScreenManager()
        print(game.number_of_players)

        logo = Logo(name='logo')
        screen_manager.add_widget(logo)

        number_of_players = NumberOfPlayers(name='number_of_players_declaration')
        screen_manager.add_widget(number_of_players)

        players_registration = PlayersRegistration(name='players_registration')
        screen_manager.add_widget(players_registration)

        return screen_manager


if __name__ == '__main__':
    my_app = MosaicApp()
    my_app.run()

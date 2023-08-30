class Game:
    def __init__(self):
        self.number_of_players = 0

    def verify_players_number(self, num_players):
        try:
            if num_players > 0:
                self.number_of_players = num_players
                return 1
        except ValueError:
            pass

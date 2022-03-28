# Used to keep record of the points in a game of scrabble. Just a bit more convenient than pen and paper.


class Player:
    def __init__(self, name):
        self.points = 0
        self.scores = []
        self.name = name

    def add_points(self, points):
        self.points += points
        self.scores.append(points)

    def show_score(self):
        print('{}: \n Word Scores: {} \n Total Score: {}'.format(self.name,
                                                                 self.scores,
                                                                 self.points))


class Game:
    def __init__(self, players):
        self.players = players

    def end_game(self):
        print('*' * 30)
        print('Game finished with scores:')
        for player in self.players:
            player.show_score()
        print('*' * 30)

    def player_move(self, player):
        points = int(input('Enter {}\'s points: '.format(player.name)))
        player.add_points(points)
        player.show_score()

    def play(self):
        while True:
            for player in self.players:
                try:
                    self.player_move(player)
                except ValueError:
                    option = input('Exit? y/n: ')
                    if option == 'n':
                        continue
                    else:
                        self.end_game()
                        return


if __name__ == "__main__":
    players_list = []
    while True:
        player_name = input('Add a player name or continue(c):')
        if player_name == 'c':
            break
        else:
            players_list.append(Player(player_name))

    game = Game(players_list)
    game.play()
    _ = input('Press enter to exit')
    exit()

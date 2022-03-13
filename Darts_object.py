import Ascii_art as aa
class Player:
    def __init__(self, name, game):
        self.name = name
        self.score = game

    def play(self, score_str):
        def parse_leg(n: str) -> int:
            n = n.upper()
            if n == "BULL":
                return 25
            if n == "EYE":
                return 50
            if 'D' in n:
                n = n.strip('D')
                n = int(n)
                n = 2 * n
                return n
            elif 'T' in n:
                n = n.strip('T')
                n = int(n)
                n = 3 * n
                return n
            return int(n)

        list_scores = score_str.strip(" ").split(" ")
        list_scores = list(filter(lambda x: x != '', list_scores))
        list_scores = list(map(parse_leg, list_scores))
        leg_score = sum(list_scores)
        if leg_score <= self.score:
            self.score -= leg_score

    def has_won(self):
        return self.score == 0

    def prompt_score(self):
        inp = input("score: ")
        while True:
            try:
                self.play(inp)
                break
            except ValueError:
                inp = input("I didnt get it can you repeat ? ")

    @classmethod
    def initiate(cls, i, score):
        while True:
            name = input(f'What is the name of the player {i + 1} ? (max 12 characters) ')
            name = str(name).strip(" ")
            if len(str(name)) <= 12:
                player = cls(name, score)
                return player
            else:
                print("maximum 12 character please!")

    def print_line(self):
        return f'{self.name:<12.12} : {self.score:>4.0f}'

    def gloat(self):
        return f'{self.name} has won!!!!!    Congratulations'


def ask_game():
    while True:
        objective = input("what game are you playing (Which score do you need to get to finish) ? ")
        try:
            objective = int(objective)
        except ValueError:
            print("I didn't understand!")
        else:
            if objective < 10000:
                return objective
            else:
                print("A game of 10000 or more will be too long!")


def ask_players():
    while True:
        num_players = input("How many players are you (1-5)? :")
        try:
            num_players = int(num_players)
        except ValueError:
            print("I didn't understand!")
        else:
            if num_players > 5:
                print("sorry max 5 players!")
            else:
                return num_players


def print_board(nround, players):
    print((12 + 4 + 3 + 2) * '_')  # 12 chars for name, 4 for score, 3 for " : " 2 for the pointer ("> "
    for i in range(len(players)):
        print('>' if i == nround else ' ', players[i].print_line())
    print((12 + 4 + 3 + 2) * '=')


def clean_terminal():
    print("\033[H\033[J")  # clean screen


def intro():
    print(aa.dart)
    print("Welcome to the dart Calculator")
    print("               By Julien Denos")
    input('press enter to continue')
    clean_terminal()


if __name__ == '__main__':
    intro()
    game = ask_game()
    number_players = ask_players()
    players = []

    for i in range(number_players):
        players.append(Player.initiate(i, game))

    nround = 0
    while True:
        clean_terminal()
        print_board(nround,players)
        players[nround].prompt_score()
        if players[nround].has_won():
            clean_terminal()
            print(players[nround].gloat())
            input("press enter to quit")
            clean_terminal()
            break
        nround = (nround + 1) % number_players

def parse_score(s: str) -> int:
    '''
    Calculate a score based on input! Separate each leg by a space you can double a leg by adding D to the score and triple it by adding T!
    :param s: The string to interpret
    :return: the calculated score
    '''
    def parse_leg(n: str) -> int:
        '''
        Interpret the leg
        :param n: leg to interpret
        :return: score of the leg
        '''
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

    list_scores = s.strip(" ").split(" ")
    list_scores = list(filter(lambda x: x != '', list_scores))
    list_scores = list(map(parse_leg, list_scores))
    return sum(list_scores)


def ask_score() -> int:
    '''
    Ask for the score and interpret it
    :return: the score of the 3 darts
    '''
    inp = input("score: ")
    while True:
        try:
            score = parse_score(inp)
            break
        except ValueError:
            inp = input("I didnt get it can you repeat ? ")
    return score


if __name__ == "__main__":
    objective = input("what game are you playing (Which score do you need to get to finish) ? ")
    while True:
        try:
            objective = int(objective)
            break
        except ValueError:
            print("I didn't understand!")
            objective = input("what game are you playing (Which score do you need to get to finish) ? ")

    while True:
        num_players = input("How many players are you (1-5)? :")
        try:
            num_players = int(num_players)
            if num_players > 5:
                print("sorry max 5 players!")
            else:
                break
        except ValueError:
            print("I didn't understand!")

    players = []
    scores = []
    for i in range(num_players):
        players.append(input(f"What is the name of player {i + 1} ?: "))
        scores.append(objective)
    player = 0 #index to know whick player is playing
    while True:
        print("\033[H\033[J") #Clean screen
        print("-----------------")
        for i in range(num_players):
            print(f"{'> ' if player == i else '  '}{players[i]}:\t{scores[i]}")
        score = ask_score()
        if score <= scores[player]: #make sur you cannot score more than needed
            scores[player] -= score
        if scores[player] == 0: #finally someone won
            print("\033[H\033[J") #cleen screen
            print(f"Congratulation {players[player]} you won!!!")
            break
        print("\033[H\033[J") #clean screen
        player = (player + 1) % num_players # to start back to 0

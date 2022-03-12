#TODO Create an object version
class Player():
    def __init__(self,name,game):
        self.name = name
        self.score = game

    def play(self,score_str):
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
        self.score -= leg_score




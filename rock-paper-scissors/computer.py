class Computer:

    def __init__(self, choose):
        self.choose = choose

    def rock(self):
        if self.choose == "rock":
            return "draw"
        elif self.choose == "paper":
            return "you won"
        else:
            return "you lose"

    def paper(self):
        if self.choose == "paper":
            return "draw"
        elif self.choose == "scissors":
            return "you won"
        else:
            return "you lose"

    def scissors(self):
        if self.choose == "scissors":
            return "draw"
        elif self.choose == "rock":
            return "you won"
        else:
            return "you lose"


class Result:

    def __init__(self, computer, player):
        self.computer = computer
        self.player = player

    def score_result(self):
        if self.player > self.computer:
            return "Nice, you beat this stupid machine up!"
        elif self.player == self.computer:
            return "You're as dumb as this machine"
        else:
            return "Computer beat you up! You suck!"

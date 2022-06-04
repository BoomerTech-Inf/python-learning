class Computer:

    def __init__(self, choose):
        self.choose = choose

    def rock(self):
        if self.choose == "rock":
            return "Remis"
        elif self.choose == "paper":
            return "you won"
        else:
            return "you lose"

    def paper(self):
        if self.choose == "paper":
            return "Remis"
        elif self.choose == "scissors":
            return "you won"
        else:
            return "you lose"

    def scissors(self):
        if self.choose == "scissors":
            return "Remis"
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
            return "Nice, you beated up this stupid machine!"
        elif self.player == self.computer:
            return "You're as dumb as this machine"
        else:
            return "Computer beated you! You suck!"



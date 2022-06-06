from random import choice


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


def game():

    rock = {
        "rock": "Draw",
        "paper": "You won",
        "scissors": "You lose"
    }
    paper = {
        "rock": "You lose",
        "paper": "Draw",
        "scissors": "You won"
    }
    scissors = {
        "rock": "You won",
        "paper": "You lose",
        "scissors": "Draw"
    }

    player_score = 0
    computer_score = 0

    available_choices = ["rock", "paper", "scissors"]
    available_dec = ["yes", "no"]
    tbbt = ["lizard", "spock"]

    while True:
        my_choice = str(input("Choose rock, paper or scissors: ")).lower()

        while my_choice not in available_choices:
            if my_choice in tbbt:
                print("It ain't The Big Bang Theory")
            else:
                print("I'm stupid and I don't understand what you are talking to me")
            my_choice = str(input("Select the right option: ")).lower()

        comp = choice([rock, paper, scissors])

        result = comp[my_choice]
        if comp[my_choice] == "You won":
            player_score += 2
        elif comp[my_choice] == "Draw":
            player_score += 1
            computer_score += 1
        else:
            computer_score += 2

        print(result)

        final_result = Result(computer_score, player_score)
        dec = str(input("Wanna play again? (yes/no): ")).lower()
        while dec not in available_dec:
            print("I'm stupid and I don't understand what you are talking to me")
            dec = str(input("Select the right option: ")).lower()

        if dec == "no":
            print(final_result.score_result())
            print("Bye!")
            break


if __name__ == '__main__':
    game()

from random import choice
from computer import Computer, Result


def game():

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
            my_choice = str(input("Select right option: ")).lower()

        computer = Computer(my_choice)
        rock = computer.rock()
        paper = computer.paper()
        scissors = computer.scissors()

        comp = choice([rock, paper, scissors])

        result = comp
        if result == "you won":
            player_score += 2
        elif result == "draw":
            player_score += 1
            computer_score += 1
        else:
            computer_score += 2

        print(result)

        final_result = Result(computer_score, player_score)
        dec = str(input("Wanna play again? (yes/no): ")).lower()
        while dec not in available_dec:
            print("I'm stupid and I don't understand what you are talking to me")
            dec = str(input("Select right option: ")).lower()

        if dec == "no":
            print(final_result.score_result())
            print("Bye!")
            break


if __name__ == '__main__':
    game()

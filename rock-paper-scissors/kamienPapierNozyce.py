from random import choice
from computer import Computer, Result

def game():

    player_score = 0
    computer_score = 0

    while True:
        my_choice = input("Choose rock, paper or scissors: ")

        computer = Computer(my_choice)
        rock = computer.rock()
        paper = computer.paper()
        scissors = computer.scissors()

        comp = choice([rock, paper, scissors])

        result = comp
        if result == "you won":
            player_score += 2
        elif result == "Remis":
            player_score += 1
            computer_score += 1
        else:
            computer_score += 2

        print(result)

        final_result = Result(computer_score, player_score)
        dec = input("Wanna play again? (yes/no): ")
        if dec != "yes":
            print(final_result.score_result())
            print("Bye!")
            break


if __name__ == '__main__':
    game()

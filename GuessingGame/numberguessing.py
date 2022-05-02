import random
attempts_list = []
Answers_for_each_stage_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

def end_score():
    stage_num=1
    print("\n")
    print("__RESULT__")
    for i in range(len(attempts_list)):
        print("{} stage = {} attempts | answer = {}".format(stage_num,attempts_list[i],Answers_for_each_stage_list[i]))
        stage_num+=1
    print("High score = {} attempts".format(min(attempts_list)))
    print("Lower score = {} attempts".format(max(attempts_list)))

def start_game():
    print("Hi there! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))

    if wanna_play.lower() == "no":
        print("see you again!")
        return 0
    else:
        game_range = int(input("Please enter the range of numbers to use : "))
        random_number = int(random.randint(1, game_range))

    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":

        try:
            guess = input("Pick a number between 1 and {} ".format(game_range))
            if int(guess) < 1 or int(guess) > game_range:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                Answers_for_each_stage_list.append(guess)
                random_number = int(random.randint(1, game_range))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    end_score()
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")

if __name__ == '__main__':
    start_game()
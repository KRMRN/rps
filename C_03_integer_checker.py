def int_check():

    error = "Please enter an integer checker more than / equal to 13. "

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                print(f"Game Goal: {response}")

        except ValueError:
            print(error)


# main routine
game_goal=int_check()
print(game_goal)

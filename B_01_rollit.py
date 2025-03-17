

def yes_no(question):

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("please enter yes/no")
            continue

def instructions():
    '''Prints instructions'''

    print('''
 *** Instructions ***   
    
 Roll the dice and try to win!   
    ''')


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


# Main routine

# ask the user if they want instructions
want_instructions = yes_no("Do you want to see the instructions? ")

# display instuctiosn
if want_instructions == "yes":
    instructions()

print()
game_goal=int_check()
print(game_goal)
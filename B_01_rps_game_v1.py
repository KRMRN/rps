


def string_checker(question, vaild_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {vaild_ans}"

    while True:

        # Get user response make sure its lowercase
        user_response = input(question).lower()

        for item in vaild_ans:
            # check if the user response is in the word list
            if item == user_response:
                return item

            # check if the user response is the same
            # the first letter of an item
            elif user_response == item[0]:
                return item

        # print error if user didnt choose an option
        print(error)
        print()


def instructions():
    '''Prints instructions'''

    print('''
 *** Instructions ***   

 To begin choose the number of rounds (or press <enter> for infinte rounds)

 Then play against the computer. You need to choose R (rock)
 P (paper) or S (scissors)

 The rules are as follows:
 o Paper beats rock
 o Rock beats scissors
 o Scissors beats rock

 press <xxx> to end the game anytime

 Good luck!
    ''')

def int_check(question):

    while True:
        error = "Please enter an integer that is more than 1"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
              print(error)


# main routine


# initalise variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📄✂️ Rock / Paper / Scissors 💎📄✂️")
print()

#instructions

want_instructions = string_checker("Do you want to see the instructions? ")

# display instuctiosn
if want_instructions == "yes":
    instructions()


# ask user for number of rounds
num_rounds = int_check("How many rounds would you like? Push <enter> for infinte mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # Round headings
    if mode == "infinite":
        round_headings = f"\n Round {rounds_played + 1} (infinite mode)"
    else:
        round_headings = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(round_headings)
    print()

    user_choice =  string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history

# automated testing is below in the form (test_case, expected_value)
to_test = [
    ("xlii", "invalid"),
    ("0.5", "invalid"),
    ("0", "invalid"),
    (1, 1),
    (2, 2),
    ("", "infinite")

]




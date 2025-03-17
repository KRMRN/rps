
# check that users have entered a vaild
# option based on a list



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


# Main routine
print()
print("💎📄✂️ Rock / Paper / Scissors Game💎📄✂️")


# ask the user if they want instructions
want_instructions = string_checker("Do you want to see the instructions? ")

# display instuctiosn
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
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

# main routine


rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions?  ",)


print("You chose", want_instructions)

user_choice = string_checker("Choose:", rps_list)
print("You chose", user_choice)
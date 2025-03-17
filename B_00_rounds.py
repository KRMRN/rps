from C_02_String_checker_v3 import rps_list


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


print("💎📄✂️ Rock / Paper / Scissors 💎📄✂️")
print()

#instructions

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

    user_choice =  input("Choose: ")

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

# run test!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    excepted = item[1]

    # get actual value
    actual = int_check(case)

    # compare actual and expected output
    if actual == excepted:
        print(f"✔️✔️✔️ Passed! Case: {case}, expected: {excepted}, recieved: {actual} ✔️✔️✔️")
    else:
        print(f"❌❌❌Failed! Case: {case}, expected: {excepted}, recieved: {actual}❌❌❌ ️")

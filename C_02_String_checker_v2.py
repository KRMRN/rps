# check that users have entered a vaild
# option based on a list

def string_checker(user_response, vaild_ans):
    while True:

        # Get user response make sure its lowercase
        user_response = user_response.lower()

        for item in vaild_ans:
            # check if the user response is in the word list
            if item == user_response:
                return item

            # check if the user response is the same
            # the first letter of an item
            elif user_response == item[0]:
                return item

        return "invalid"



# automated testing is below in the form (test_case, expected_value)
to_test = [
    ("Rock", "rock"),
    ("PAPER", "paper"),
    ("scissors", "scissors"),
    ("R", "rock"),
    ("P", "paper"),
    ("S", "scissors"),
    ("XXX", "xxx"),
    ("x", "xxx"),
    ("random", "invalid"),

]

# run test!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    excepted = item[1]

    # get actual value
    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    # compare actual and expected output
    if actual == excepted:
        print(f"✔️✔️✔️ Passed! Case: {case}, expected: {excepted}, recieved: {actual} ✔️✔️✔️")
    else:
        print(f"❌❌❌Failed! Case: {case}, expected: {excepted}, recieved: {actual}❌❌❌ ️")

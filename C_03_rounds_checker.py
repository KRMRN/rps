def int_check(to_check):

    while True:
        error = "Please enter an integer that is more than 1"

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"


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

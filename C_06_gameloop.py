# at the start both the comp/user score is zero
comp_score= 0
user_score= 0

game_goal = int(input("GAME GOAL"))

# play until a winner is found
while comp_score < game_goal and user_score < game_goal:

    # start loop
    # ask user for comp/user score
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    # Update points each round
    comp_score += comp_points
    user_score +=user_points

    # show overall score
    print("*** Game update ***")
    print(f"User score: {user_score} | Computer score: {comp_score}")

# end of game show final score
print()
if user_score > comp_score:
    print("The user has won")
else:
    print("The computer")
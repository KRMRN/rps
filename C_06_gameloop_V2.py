
import random



def inital_points(which_player):
    """Roll the dice twice and return the total"""

    double = "no"

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double


def make__statment(statement, decoration):
    """adds emoji and to the headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


# at the start both the comp/user score is zero
comp_score= 0
user_score= 0
rounds_played = 0

game_goal = int(input("GAME GOAL: "))

# play until a winner is found
while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    # start loop
    make__statment(f"Round {rounds_played}", "🎲")
    # ask user for comp/user score

    # main routine

    # roll the dice and note if they got a double
    intital_user = inital_points("User")
    intital_comp = inital_points("Comp")

    # Retrieve user points
    user_points = intital_user[0]
    comp_points = intital_comp[0]

    double_user = intital_user[1]

    # Let the user know if they can get double points
    if double_user == "yes":
        print()
        print("Great news - if you win you can get double points")

    # assume user goes first
    first = "user"
    second = "comp"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less than the computers\n")

    # if the user and computer roll the same points
    elif user_points == comp_points:
        print("The initial rolls were the same the user starts")

    # if the computer has fewer points, switch the computer to player 1
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # Loop until we have a winner
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        # first person rolls the dice and the score updates
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_points} - has {player_1_points} points")

        # if the first player score is over 13 end round
        if player_1_points >= 13:
            break

        # second person rolls the dice
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: Rolled a {player_1_points} - has {player_1_points} points")

    # end of round

    # associate player points with user or comp
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and comp if comp went first
    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # work out who won
    if user_points > comp_points:
        winner = "user"
    else:
        winner = "computer"

    round_feedback = f"The {winner} won"

    # work out who won and set losers points to zero
    if user_points>comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s points have been reset"


    # double points if it works
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # output round results
    make__statment("Round Results", "💔")
    print(f"User points :{user_points} | Computer points: {comp_points}")
    print(round_feedback)
    print()



    # Update points each round
    comp_score += comp_points
    user_score +=user_points

    # show overall score
    print("*** Game update ***")
    print(f"User score: {user_score} | Computer score: {comp_score}")

# end of game show final score

make__statment("Game over", "🕊️")

print()
if user_score > comp_score:
    print("The user has won")
else:
    print("The computer")

# initialise list to hold game history
game_history = []

# get the data

while True:
    rounds_played = input("Rounds? ")
    if rounds_played == "3":
        break

    user_points = int(input("User Points? "))
    comp_points = int(input("Computer Points? "))
    winner = input("Who won? ")
    user_score = int(input("User score: "))
    comp_score = int(input("Comp score: "))

    game_results = (f"Round {rounds_played}: User points {user_points } | "
                    f"Computer points {comp_points}, {winner} wins "
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)
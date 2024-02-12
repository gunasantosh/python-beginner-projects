import random


def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll, max_roll)

    return roll


while True:
    num_of_players = input("Enter number of players [2 - 4]: ")
    if num_of_players.isdigit():
        num_of_players = int(num_of_players)
        if 2 <= num_of_players <= 4:
            break
        else:
            print("Number of players should be between 2 and 4 only!")
    else:
        print("Invalid choice ")

max_score = 50
player_scores = [0 for _ in range(num_of_players)]

while max(player_scores) < max_score:
    for player_idx in range(num_of_players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)

print("================================================")
print("           Welcome to your Adventure            ")
print("================================================")

user_name = input("Enter your name to start or 'q' to Quit: ")
quit() if user_name.lower() == "q" else print(f"Welcome {user_name}!!")


q1 = input(
    "You have entered a forest and there are two ways to continue (left/right).Chosse one: "
).lower()
if q1 == "right":
    q2 = input(
        "You have chosen right and found a chest on the path. What will you do (open/ignore): "
    ).lower()

    if q2 == "open":
        print("You have found the treasure!!. You WON")
    elif q2 == "ignore":
        print(
            "You ignored the chest and you will travel until the end of time. You LOSE!!"
        )
    else:
        print("Invalid choice! you die")
        quit()
elif q1 == "left":
    q3 = input(
        "You have chosen left. You are walking and found a stranger. What will you do (interact/ignore): "
    ).lower()
    if q3 == "interact":
        print("The stranger is a killer and you have been killed.\n GAME OVER!!")
    elif q3 == "ignore":
        print("you ignored and continued the quest and found the treasure. YOU WON!!!")
    else:
        print("Invalid choice! you die")
        quit()
else:
    print("Invalid choice! you die")
    quit()

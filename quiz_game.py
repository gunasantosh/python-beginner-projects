print("Welcome to my quizz!!")

playing = input("Do you want to play(y/n): ")

if playing.lower() != "y":
    quit()

print("Okay! let's play")

score = 0
total_que = 3

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! (Correct : central processing unit)")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! (Correct : graphical processing unit)")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! (Correct : random access memory)")

print(f"Your score is : {score} ")
print(f"Your percentage is: {round(((score/total_que)*100), 2)}%")

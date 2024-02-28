from concurrent.futures.process import _chain_from_iterable_of_lists
import turtle
import random

WIDTH, HEIGHT = 700, 600
COLORS = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "black",
    "purple",
    "pink",
    "brown",
    "cyan",
]


def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number out of range!!")
        else:
            print("Please enter a valid number !")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    dist = 0
    for i, color in enumerate(colors):
        dist += spacingx
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + dist, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 5)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner of the race is color {winner}")

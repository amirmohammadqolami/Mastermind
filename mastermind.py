import random

# Mastermind Game

# 1: Define Colors
# 2: Define Variables
# 3: Random Colors
# 4: Receive user input
# 5: Check User's input Correctness
# 6: Print black and white value and user winning status


# ----- Define Colors ---------#

Colors = {
    1: "Yellow",
    2: "Red",
    3: "Blue"
}


# ----- Define Variables ---------#

black = 0
white = 0
GAME_LEN = 3
initial = []
WIN = False
ChanceTimes = 2

# ----- Random Color ---------#

while len(initial) < GAME_LEN:
    r = random.randint(1,3)
    if r not in initial:
        initial.append(r)

initial = [Colors[i] for i in initial]


# ----- Receive user input ---------#

for turn in range(ChanceTimes):
    guess = input()
    guess = guess.split(",")

    black = 0
    white = 0

    for i in range(GAME_LEN):
        if guess[i] == initial[i]:
            black += 1
        elif guess[i] in initial:
            white += 1

    if black == GAME_LEN :
        WIN = True
        break

if WIN:
    print("Congratulation , You won .")
else:
    print("I'm so sorry , you lose , try again")

print("your black score:{} and white score:{}".format(black,white))

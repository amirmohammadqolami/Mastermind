from constants import *
import random


class Game(object):

    def __init__(self, length=GAME_LENGTH):
        self.length = length
        self.initial_state = self.new_game()
        self.turns = 0
        self.is_won = False
        self.is_ended = False

    def new_game(self):
        initial = []
        while len(initial) < self.length:
            r = random.randint(1, 3)
            if r not in initial:
                initial.append(r)
        initial = [COLOR[i] for i in initial]
        return initial

    def turn(self):
        if self.is_ended:
            print(GAMEOVER_MESSAGE)
            return

        guess = input()
        guess = guess.split(SPLIT_CHAR)

        black = 0
        white = 0

        for i in range(self.length):
            if guess[i] == self.initial_state[i]:
                black += 1
            elif guess[i] in self.initial_state:
                white += 1

        print(GUESS_RESULT_MESSAGE.format(black, white))

        self.turns += 1
        self.check_state(black)

    def to_str(self):
        return ",".join(self.initial_state)

    def check_state(self, black):
        if self.check_win(black):
            print(WIN_MESSAGE)
            self.end()
        if self.check_lose():
            print(LOSE_MESSAGE.format(self.to_str()))
            self.end()

    def check_win(self, black):
        return black == self.length

    def check_lose(self):
        return (self.turns == MAX_TURN) and not self.is_won

    def end(self):
        self.is_ended = True

    def start(self):
        for turn in range(MAX_TURN):
            game.turn()


game = Game()
game.start()

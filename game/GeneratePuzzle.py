

import random
import pygame
from game.digit_sqr import DigitSqr


class GeneratePuzzle:
    def __init__(self, screen):
        self.screen = screen
        self.digits = []
        self.generate_puzzle()
        self.digit_sqr = DigitSqr(self.screen)


    def generate_puzzle(self):
        puzzle = [0,1,2,3,4,5,6,7,8]
        del self.digits[:]
        possible_moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
        for i in range(0, 5):
            for j in range(0, 9):
                if (puzzle[j] == 8):
                    pos = j
            new_pos = random.choice(possible_moves[pos])
            temp = puzzle[pos]
            puzzle[pos] = puzzle[new_pos]
            puzzle[new_pos] = temp


        return puzzle

    def draw_puzzle(self, digits):
        counter_x = 1
        counter_y = 1
        puzzle = []
        for digit in digits:
            puzzle.append(self.digit_sqr.design( digit, 100 * counter_x, 100 * counter_y))

            counter_x += 1
            if counter_x % 4 == 0:
                counter_x = 1
                counter_y += 1

        return puzzle
    def draw_puzzle_animate(self,digits,index1,index2,Key):
        counter_x = 1
        counter_y = 1
        puzzle = []
        for digit in digits:
            if(digit != digits[index1] and digit != digits[index2]):
                self.digit_sqr.design(digit, 100 * counter_x, 100 * counter_y)
            counter_x += 1
            if counter_x % 4 == 0:
                counter_x = 1
                counter_y += 1
        if(digits[index2]==8):
            self.digit_sqr.animation(digits[index1],Key,index1,index2)
        else:
            counter_x = 1
            counter_y = 1
            puzzle = []
            for digit in digits:
                puzzle.append(self.digit_sqr.design( digit, 100 * counter_x, 100 * counter_y))

                counter_x += 1
                if counter_x % 4 == 0:
                    counter_x = 1
                    counter_y += 1








        return puzzle




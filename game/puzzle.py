import sys
sys.path.insert(0,'/Users/mikechase3/Dropbox/000-025 Educational Years/024 ITAndGradSchool/Career/Education/CPS 580 AI/HW1 PyGameModule/PuzzleGame Framework')
import time
from copy import deepcopy

import pygame

from game.GeneratePuzzle import GeneratePuzzle
from game.button import Button
from game.highlight_digit import HighlightDigit
from sol import solution


class Puzzle:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.dist = 200

        pygame.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('### 8 numbers sorting Puzzle ###')
        self.screen.fill(self.black)

        self.generate_puzzle = GeneratePuzzle(self.screen)
        self.highlight = HighlightDigit(self.screen)

    def initialization(self):

        self.puzzle_numbers = self.generate_puzzle.generate_puzzle()
        self.generate_puzzle.draw_puzzle(self.puzzle_numbers)
        solve_button = Button(self.screen, (255, 255, 153), 450, 100, 100, 50, "IDeep")
        solve_button2 = Button(self.screen, (255, 255, 153), 450, 200, 100, 50, "A Star")
        solve_button.draw((255, 255, 0))
        solve_button2.draw((255, 255, 0))
        self.finish = False
        self.you_win = False

        while not self.finish:
            self.highlight.move_count("Puzzle Search Game ", 130, 10)
            solve_button.draw((255, 255, 0))
            solve_button2.draw((255, 255, 0))
            puzzle_prev = []
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()
                # print(event)
                if event.type == pygame.QUIT:
                    self.finish = True

                if (event.type == pygame.KEYDOWN ):
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        # print "*** RIGHT ***"
                        puzzle_prev = self.puzzle_numbers
                        self.you_win,index1,index2 = self.highlight.highlight_digit_to_be_swapped(100, 0, "RIGHT",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers,index1,index2,"Right")
                        if (self.puzzle_numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                            self.you_win = True
                        else:
                            self.you_win = False



                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        # print "*** LEFT ***"
                        self.you_win,index1,index2 = self.highlight.highlight_digit_to_be_swapped(-100, 0, "LEFT",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers,index1,index2,"Left")
                        if (self.puzzle_numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                            self.you_win = True
                        else:
                            self.you_win = False

                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                        # print "*** DOWN ***"
                        self.you_win,index1,index2 = self.highlight.highlight_digit_to_be_swapped(0, 100, "DOWN",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers,index1,index2,"Down")
                        if (self.puzzle_numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                            self.you_win = True
                        else:
                            self.you_win = False

                    if (event.key == pygame.K_UP or event.key == pygame.K_w):
                        # print "*** UP ***"
                        self.you_win,index1,index2 = self.highlight.highlight_digit_to_be_swapped(0, -100, "UP",
                                                                                    self.puzzle_numbers)
                        self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers,index1,index2,"Up")
                        if (self.puzzle_numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                            self.you_win = True
                        else:
                            self.you_win = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx,posy=pygame.mouse.get_pos()
                    if solve_button.isOver(pos):
                        print("Iterative deepening button")

                        list = self.get_sol(1)

                        for i in range(len(list)):
                            a = list[i]

                            for j in range(0, 9):
                                if (self.puzzle_numbers[j] == 8):
                                    pos_eight = j

                            temp = self.puzzle_numbers[pos_eight]
                            self.puzzle_numbers[pos_eight] = self.puzzle_numbers[a]
                            self.puzzle_numbers[a] = temp
                            index2 = pos_eight
                            index1 = a
                            list_find = [["None","Left","None","Up","None","None","None","None","None"],
                                         ["Right","None","Left","None","Up","None","None","None","None"],
                                         ["None","Right","None","None","None","Up","None","None","None"],
                                         ["Down","None","None","None","Left","None","Up","None","None"],
                                         ["None","Down","None","Right","None","Left","None","Up","None"],
                                         ["None","None","Down","None","Right","None","None","None","Up"],
                                         ["None","None","None","Down","None","None","None","Left","None"],
                                         ["None","None","None","None","Down","None","Right","None","Left"],
                                         ["None","None","None","None","None","Down","None","Right","None"]
                                         ]

                            Key=list_find[int(pos_eight)][int(a)]
                            self.screen.fill(self.black)
                            self.highlight.move_count("Puzzle Search Game ", 130, 10)
                            solve_button.draw((255, 255, 0))
                            solve_button2.draw((255, 255, 0))
                            self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers,index2,index1,Key)
                            self.highlight.move_count("Moves: %s" % str(i))
                            pygame.display.update()
                            time.sleep(1)
                        if(self.puzzle_numbers == [0,1,2,3,4,5,6,7,8]):
                            self.you_win = True
                        else:
                            self.you_win = False


                    elif solve_button2.isOver(pos):
                        print("A Star button")


                        list = self.get_sol(2)

                        for i in range(len(list)):
                            a = list[i]

                            for j in range(0, 9):
                                if (self.puzzle_numbers[j] == 8):
                                    pos_eight = j

                            temp = self.puzzle_numbers[pos_eight]
                            self.puzzle_numbers[pos_eight] = self.puzzle_numbers[a]
                            self.puzzle_numbers[a] = temp

                            index2 = pos_eight
                            index1 = a
                            list_find = [["None", "Left", "None", "Up", "None", "None", "None", "None", "None"],
                                         ["Right", "None", "Left", "None", "Up", "None", "None", "None", "None"],
                                         ["None", "Right", "None", "None", "None", "Up", "None", "None", "None"],
                                         ["Down", "None", "None", "None", "Left", "None", "Up", "None", "None"],
                                         ["None", "Down", "None", "Right", "None", "Left", "None", "Up", "None"],
                                         ["None", "None", "Down", "None", "Right", "None", "None", "None", "Up"],
                                         ["None", "None", "None", "Down", "None", "None", "None", "Left", "None"],
                                         ["None", "None", "None", "None", "Down", "None", "Right", "None", "Left"],
                                         ["None", "None", "None", "None", "None", "Down", "None", "Right", "None"]
                                         ]

                            Key = list_find[int(pos_eight)][int(a)]
                            self.screen.fill(self.black)
                            self.highlight.move_count("Puzzle Search Game ", 130, 10)
                            solve_button.draw((255, 255, 0))
                            solve_button2.draw((255, 255, 0))
                            self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers, index2, index1, Key)
                            self.highlight.move_count("Moves: %s" % str(i))
                            pygame.display.update()
                            time.sleep(1)
                        if (self.puzzle_numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                            self.you_win = True
                        else:
                            self.you_win = False




                    elif posx > 100 and posx < 400 and posy >98 and posy < 400:
                        posx,poy = pygame.mouse.get_pos()

                        self.you_win,index1,index2,Key = self.highlight.highlight_digit_to_be_swapped_click(posx,poy,self.puzzle_numbers)

                        self.generate_puzzle.draw_puzzle_animate(self.puzzle_numbers,index1,index2,Key)

                        if(self.puzzle_numbers==[0,1,2,3,4,5,6,7,8]):
                            self.you_win = True
                        else:
                            self.you_win = False



                if event.type == pygame.MOUSEMOTION:
                    if solve_button.isOver(pos):
                        solve_button.color = (0, 204, 0)
                    elif solve_button2.isOver(pos):
                        solve_button2.color=(0,204,0)
                   
                    else:
                        solve_button.color = (255, 255, 0)
                        solve_button2.color = (255, 255, 0)

                if self.you_win:
                    # self.highlight.move_count("8 Puzzle Puzzle", 130, 10)
                    self.highlight.move_count("You Win !!!", 130, 450)
                    pygame.display.update()
                    self.clock.tick(30)
                    time.sleep(2)
                    self.screen.fill(self.black)
                    self.puzzle_numbers = [0,1,2,3,4,5,6,7,8]
                    self.highlight.m_count = 0
                    self.you_win = self.highlight.highlight_digit_to_be_swapped(0, -100, "UP",
                                                                                self.puzzle_numbers)
                    self.generate_puzzle.draw_puzzle(self.puzzle_numbers)

                    self.you_win = False
                    self.finish = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()

    def get_sol(self,button):
        counter = 0
        if (button == 1):
            list = solution.iterativeDeepening(self.puzzle_numbers)

            return list
        if (button == 2):
            list = solution.astar(self.puzzle_numbers)
            return list

    def swap(self, board_path, index2):
        pos_missing = 0

        for i in range(len(board_path)):
            for j in range(len(self.puzzle_numbers)):
                if self.puzzle_numbers[j]==9:
                    pos_missing = j
            a = board_path[i]
            temp = self.puzzle_numbers[board_path[i]]
            self.puzzle_numbers[board_path[i]] = self.puzzle_numbers[pos_missing]
            self.puzzle_numbers[pos_missing] = temp
            self.generate_puzzle.draw_puzzle(self.puzzle_numbers)
            pygame.display.update()


        return False


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.initialization()

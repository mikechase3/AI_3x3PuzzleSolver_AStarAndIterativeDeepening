

import pygame
from game.button import Button
from game.highlight_digit import HighlightDigit


TIME = 5

class DigitSqr():
    def __init__(self, screen):
        self.screen = screen
        self.green = (100, 100, 100)
        self.dark_green = (0, 255, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.digit = -1
        self.sqr_side = 98
        self.highlight = HighlightDigit(self.screen)

    def design(self,digit, sqr_x, sqr_y ):
        self.digit = digit
        self.rect = pygame.draw.rect(self.screen, self.green, (sqr_x, sqr_y, self.sqr_side, self.sqr_side))
        if self.digit != 8:
            self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)
        if self.digit == 8 :
            self.rect = pygame.draw.rect(self.screen, self.black, (sqr_x, sqr_y, self.sqr_side, self.sqr_side))

    def animation(self,digit,key,index1,index2):
        self.digit = digit
        list_sqr = [[100,100],[200,100],[300,100],[100,200],[200,200],[300,200],[100,300],[200,300],[300,300]]
        index_variable_x = list_sqr[index2][0]
        index_variable_y = list_sqr[index2][1]
        self.highlight.move_count("Puzzle Search Game ", 130, 10)
        solve_button = Button(self.screen, (255, 255, 153), 450, 100, 100, 50, "IDeep")
        solve_button2 = Button(self.screen, (255, 255, 153), 450, 200, 100, 50, "A Star")
        solve_button.draw((255, 255, 0))
        solve_button2.draw((255, 255, 0))

        i=0
        counter = 0
        for i in range(0,101,TIME):
            if(key=="Right"):
                self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x, index_variable_y, self.sqr_side, self.sqr_side))
                self.rect = pygame.draw.rect(self.screen, self.green, (index_variable_x + i, index_variable_y, self.sqr_side, self.sqr_side))
                if self.digit != 8:
                    self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)
                if self.digit == 8:
                    self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x + i, index_variable_y, self.sqr_side, self.sqr_side))
                pygame.display.update()
            elif(key=="Left"):
                self.rect = pygame.draw.rect(self.screen, self.black,
                                             (index_variable_x, index_variable_y, self.sqr_side, self.sqr_side))
                self.rect = pygame.draw.rect(self.screen, self.green, (index_variable_x - i, index_variable_y, self.sqr_side, self.sqr_side))
                if self.digit != 8:
                    self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)
                if self.digit == 8:
                    self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x - i, index_variable_y, self.sqr_side, self.sqr_side))

                pygame.display.update()
            elif(key=="Up"):

                self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x, index_variable_y, self.sqr_side, self.sqr_side))
                self.rect = pygame.draw.rect(self.screen, self.green, (index_variable_x, index_variable_y - i, self.sqr_side, self.sqr_side))
                if self.digit != 8:
                    self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)
                if self.digit == 8:
                    self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x , index_variable_y+1, self.sqr_side, self.sqr_side))


                pygame.display.update()
            elif(key=="Down"):

                self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x, index_variable_y, self.sqr_side, self.sqr_side))
                self.rect = pygame.draw.rect(self.screen, self.green, (index_variable_x , index_variable_y + i, self.sqr_side, self.sqr_side))

                if self.digit != 8:
                    self.text_to_screen(self.digit, self.rect.x + 40, self.rect.y + 25)
                if self.digit == 8:
                    self.rect = pygame.draw.rect(self.screen, self.black, (index_variable_x , index_variable_y+i, self.sqr_side, self.sqr_side))

                pygame.display.update()



            counter +=1





    def text_to_screen(self, text, x, y):
        try:
            text = str(text)
            self.textsurface = self.myfont.render(text, True, self.dark_green)
            self.screen.blit(self.textsurface, (x, y))

        except Exception as e:

            raise e



import pygame
import time


class HighlightDigit:
    def __init__(self, screen):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.screen = screen

        self.highlight_x = 200
        self.highlight_y = 200
        self.highlight_side = 100

        self.hfont = pygame.font.SysFont('Segoe Print', 30)
        self.highlight_digit = pygame.draw.rect(self.screen, self.white,
                                                [self.highlight_x, self.highlight_y, self.highlight_side,
                                                 self.highlight_side], 5)

        self.index = 0
        self.m_count = 0

    def highlight_digit_to_be_swapped(self, x, y, key, puzzle):
        self.index = int(((self.highlight_digit.y - 100) / 100) * 3 + ((self.highlight_digit.x / 100)) )


        self.highlight_x = int(self.highlight_digit.x + x)
        self.highlight_y = int(self.highlight_digit.y + y)


        if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
            self.screen.fill(self.black)
            self.highlight_digit = self.highlight_digit.move(x, y)

            pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
            if key == "LEFT":
                return self.swap(int(self.index), int(self.index - 1), puzzle),int(self.index - 1),int(self.index)
            elif key == "RIGHT":
                return self.swap(int(self.index), int(self.index + 1), puzzle),int(self.index + 1),int(self.index)
            elif key == "UP":
                return self.swap(int(self.index), int(self.index - 3), puzzle),int(self.index - 3),int(self.index)
            elif key == "DOWN":
                return self.swap(int(self.index), int(self.index + 3), puzzle),int(self.index + 3),int(self.index)
            else:
                pass
        return False,0,0

    def swap(self, index, index2, puzzle):

        if puzzle[index2] == 8:
            temp = puzzle[index]
            puzzle[index] = puzzle[index2]
            puzzle[index2] = temp
            self.m_count += 1
        self.move_count("Moves: %s" % str(self.m_count))
        if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print("You Win !!!")
            return True
        else:
            pass

        return False

    def highlight_digit_to_be_swapped_click(self,posx,posy, puzzle):

        if posx>100 and posx<200 and posy>100 and posy<200:
            x=-100
            y=-100

            self.highlight_digit.x =198
            self.highlight_digit.y= 198

            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)

            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)
                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)

                if(puzzle[1]==8):
                    return self.swap(0, 1, puzzle),1,0,"Right"
                elif(puzzle[3]==8):
                    return self.swap(0, 3, puzzle),3,0,"Down"




        elif posx>200 and posx<300 and posy>100 and posy<200:
            x=0
            y=-100

            self.highlight_digit.x =198
            self.highlight_digit.y= 198

            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)

            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)

                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[0] == 8):
                    return self.swap(1, 0, puzzle),0,1,"Left"
                elif (puzzle[2] == 8):
                    return self.swap(1, 2, puzzle),2,1,"Right"
                elif (puzzle[4] ==8):
                    return self.swap(1,4,puzzle),4,1,"Down"
        elif posx>300 and posx<400 and posy>100 and posy<200:
            x=100
            y=-100

            self.highlight_digit.x = 198
            self.highlight_digit.y = 198
            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)
            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)

                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[1] == 8):
                    return self.swap(2, 1, puzzle),1,2,"Left"
                elif (puzzle[5] == 8):
                    return self.swap(2, 5, puzzle),5,2,"Down"

        ####################2rd row ############
        if posx>100 and posx<200 and posy>200 and posy<300:
            x=-100
            y=0

            self.highlight_digit.x =198
            self.highlight_digit.y= 198

            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)

            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)
                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[0] == 8):
                    return self.swap(3, 0, puzzle),0,3,"Up"
                elif (puzzle[6] == 8):
                    return self.swap(3, 6, puzzle),6,3,"Down"
                elif (puzzle[4] ==8):
                    return self.swap(3,4,puzzle),4,3,"Right"

        elif posx>200 and posx<300 and posy>200 and posy<300:
            x=0
            y=0

            self.highlight_digit.x =198
            self.highlight_digit.y= 198

            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)

            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)

                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[1] == 8):
                    return self.swap(4, 1, puzzle),1,4,"Up"
                elif (puzzle[3] == 8):
                    return self.swap(4, 3, puzzle),3,4,"Left"
                elif (puzzle[5] ==8):
                    return self.swap(4,5,puzzle),5,4,"Right"
                elif (puzzle[7]==8):
                    return self.swap(4,7,puzzle),7,4,"Down"
        elif posx>300 and posx<400 and posy>200 and posy<300:
            x=100
            y=0

            self.highlight_digit.x = 198
            self.highlight_digit.y = 198
            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)
            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)

                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[2] == 8):
                    return self.swap(5, 2, puzzle),2,5,"Up"
                elif (puzzle[4] == 8):
                    return self.swap(5, 4, puzzle),4,5,"Left"
                elif (puzzle[8] ==8):
                    return self.swap(5,8,puzzle),8,5,"Down"
        ################3rd row ################
        if posx>100 and posx<200 and posy>300 and posy<400:
            x=-100
            y=100

            self.highlight_digit.x =198
            self.highlight_digit.y= 198

            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)

            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)
                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[3] == 8):
                    return self.swap(6, 3, puzzle),3,6,"Up"
                elif (puzzle[7] == 8):
                    return self.swap(6, 7, puzzle),7,6,"Right"


        elif posx>200 and posx<300 and posy>300 and posy<400:
            x=0
            y=100

            self.highlight_digit.x =198
            self.highlight_digit.y= 198

            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)

            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)

                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[6] == 8):
                    return self.swap(7, 6, puzzle),6,7,"Left"
                elif (puzzle[4] == 8):
                    return self.swap(7, 4, puzzle),4,7,"Up"
                elif (puzzle[8] ==8):
                    return self.swap(7,8,puzzle),8,7,"Right"
        elif posx>300 and posx<400 and posy>300 and posy<400:
            x=100
            y=100

            self.highlight_digit.x = 198
            self.highlight_digit.y = 198
            self.highlight_x = int(self.highlight_digit.x + x)
            self.highlight_y = int(self.highlight_digit.y + y)
            if self.highlight_x < 390 and self.highlight_x >= 98 and self.highlight_y >= 98 and self.highlight_y < 300:
                self.screen.fill(self.black)
                self.highlight_digit = self.highlight_digit.move(x, y)

                pygame.draw.rect(self.screen, self.white, self.highlight_digit, 5)
                if (puzzle[5] == 8):
                    return self.swap(8, 5, puzzle),5,8,"Up"
                elif (puzzle[7] == 8):
                    return self.swap(8, 7, puzzle),7,8,"Left"




        return False,0,0,None




    def move_count(self, text, x=50, y=400):
        try:
            self.hfont.render(text, True, self.white)
            self.htextsurface = self.hfont.render(text, True, self.white)
            self.screen.blit(self.htextsurface, (x, y))

        except Exception as e:
            # print 'Font Error, saw it coming'
            raise e

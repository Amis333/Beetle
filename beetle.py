from random import randint
import pygame


class Beetle:
    def __init__(self):
        self.beetle_position_x = randint(5, 10)
        self.beetle_position_y = randint(2, 7)
        self.beetle_direction_right = 1
        self.beetle_direction_left = 2
        self.beetle_direction_up = 3
        self.beetle_direction_down = 4
        self.beetle_direction = self.beetle_direction_up
        self.pause = False
        self.last_beetle_direction = self.beetle_direction

    def make_move(self):
        if self.step < len(self.path):
            self.field[self.path[self.step][0]][self.path[self.step][1]] = self.cell_type_beetle
            self.field[self.path[self.step - 1][0]][self.path[self.step - 1][1]] = self.cell_type_none
            self.step += 1
        else:
            return True
        self.last_beetle_direction = self.beetle_direction
        if self.step < len(self.path):
            if self.path[self.step][0] < self.path[self.step - 1][0]:
                self.beetle_direction = self.beetle_direction_left
            elif self.path[self.step][0] > self.path[self.step - 1][0]:
                self.beetle_direction = self.beetle_direction_right
            else:
                if self.path[self.step][1] < self.path[self.step - 1][1]:
                    self.beetle_direction = self.beetle_direction_up
                elif self.path[self.step][1] > self.path[self.step - 1][1]:
                    self.beetle_direction = self.beetle_direction_down

        match self.beetle_direction:
            case self.beetle_direction_right:
                if self.last_beetle_direction == self.beetle_direction_up:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
                elif self.last_beetle_direction == self.beetle_direction_down:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, 90)
            case self.beetle_direction_down:
                if self.last_beetle_direction == self.beetle_direction_right:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
                elif self.last_beetle_direction == self.beetle_direction_left:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, 90)
            case self.beetle_direction_left:
                if self.last_beetle_direction == self.beetle_direction_up:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, 90)
                elif self.last_beetle_direction == self.beetle_direction_down:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
            case self.beetle_direction_up:
                if self.last_beetle_direction == self.beetle_direction_right:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, 90)
                elif self.last_beetle_direction == self.beetle_direction_left:
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)




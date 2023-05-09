from parametrs import *
import pygame


class Beetle:
    def __init__(self):
        self.beetle_position_x = cell_count_x // 2
        self.beetle_position_y = cell_count_y // 2
        self.beetle_direction_right = 1
        self.beetle_direction_left = 2
        self.beetle_direction_up = 3
        self.beetle_direction_down = 4
        self.beetle_direction = self.beetle_direction_up
        self.pause = False

    def make_move(self):
        match self.beetle_direction:
            case self.beetle_direction_up:
                self.beetle_position_y -= 1
                if self.beetle_position_y - 1 == 0:
                    self.beetle_direction = self.beetle_direction_right
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
                else:
                    if self.field[self.beetle_position_x][self.beetle_position_y - 1] == self.cell_type_wall:
                        self.pause = True

            case self.beetle_direction_right:
                self.beetle_position_x += 1
                if self.beetle_position_x + 1 == cell_count_x - 1:
                    self.beetle_direction = self.beetle_direction_down
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
                else:
                    if self.field[self.beetle_position_x + 1][self.beetle_position_y] == self.cell_type_wall:
                        self.pause = True

            case self.beetle_direction_down:
                self.beetle_position_y += 1
                if self.beetle_position_y + 1 == cell_count_y - 1:
                    self.beetle_direction = self.beetle_direction_left
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
                else:
                    if self.field[self.beetle_position_x][self.beetle_position_y + 1] == self.cell_type_wall:
                        self.pause = True

            case self.beetle_direction_left:
                self.beetle_position_x -= 1
                if self.beetle_position_x - 1 == 0:
                    self.beetle_direction = self.beetle_direction_up
                    self.beetle_image = pygame.transform.rotate(self.beetle_image, -90)
                else:
                    if self.field[self.beetle_position_x - 1][self.beetle_position_y] == self.cell_type_wall:
                        self.pause = True


        for i in range(cell_count_x):
            for j in range(cell_count_y):
                if self.field[i][j] > self.cell_type_none:
                    self.field[i][j] -= 1
        self.field[self.beetle_position_x][self.beetle_position_y] = self.cell_type_beetle



import pygame
from parametrs import *
from field import Field
import sys
from time import sleep


class Graphics(Field):
    def __init__(self):
        pygame.init()
        super(Graphics, self).__init__()
        self.window = pygame.display.set_mode((cell_count_x * cell_size, cell_count_y * cell_size))
        self.none_image = pygame.image.load('images/none.png')
        self.none_rect = self.none_image.get_rect()
        self.wall_image = pygame.image.load('images/wall.png')
        self.wall_rect = self.wall_image.get_rect()
        self.beetle_image = pygame.image.load('images/beetle.png')
        self.beetle_rect = self.beetle_image.get_rect()
        pygame.display.set_caption('Beetle')
        self.timer = pygame.time.Clock()
        self.fps = 8

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(pygame.quit())

    def algorithm_cycle(self):
        self.clear_field()
        print(self.path)
        self.step = 0

        while True:
            self.draw_graphics()
            pygame.display.flip()
            if self.make_move():
                sleep(2)
                exit()
            self.check_events()
            self.window.fill(field_color)
            self.timer.tick(self.fps)

    def draw_graphics(self):
        for i in range(cell_count_y):
            for j in range(cell_count_x):
                match(self.field[j][i]):
                    case self.cell_type_none:
                        self.none_rect.x = j * cell_size
                        self.none_rect.y = i * cell_size
                        self.window.blit(self.none_image, self.none_rect)
                    case self.cell_type_wall:
                        self.wall_rect.x = j * cell_size
                        self.wall_rect.y = i * cell_size
                        self.window.blit(self.wall_image, self.wall_rect)
                    case self.cell_type_beetle:
                        self.beetle_rect.x = j * cell_size
                        self.beetle_rect.y = i * cell_size
                        self.window.blit(self.beetle_image, self.beetle_rect)

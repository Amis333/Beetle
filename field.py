from parametrs import *
from beetle import Beetle
from random import choice, randint


class Field(Beetle):
    def __init__(self):
        super(Field, self).__init__()
        self.field_size_x, self.field_size_y = cell_count_x, cell_count_y
        self.cell_type_none = 0
        self.cell_type_beetle = 1
        self.cell_type_wall = -1
        self.cell_type_exit = 2
        self.field = [[self.cell_type_none for _ in range(self.field_size_x)
                       ] for _ in range(self.field_size_y)]
        self.path = list()
        self.step = 0

    def add_object(self, obj):
        while True:
            j = choice(range(2, len(self.field) - 2))
            i = choice(range(2, len(self.field[j]) - 2))
            if self.field[j][i] == self.cell_type_none and self.field[j][i] != self.cell_type_beetle:
                self.field[j][i] = obj
                break

    def add_exit(self):
        exit_x = randint(1, 13)
        exit_y = randint(1, 13)
        if exit_x < exit_y:
            exit_x = 0
            self.field[exit_x][exit_y] = self.cell_type_none
        else:
            exit_y = 0
            self.field[exit_x][exit_y] = self.cell_type_none

    def clear_field(self):
        for i in range(self.field_size_y):
            for j in range(self.field_size_x):
                if i == 0 or j == 0 or i == self.field_size_x - 1 or j == self.field_size_y -1:
                    self.field[j][i] = self.cell_type_wall
                else:
                    self.field[j][i] = self.cell_type_none
        self.add_exit()

        for i in range(20):
            self.add_object(self.cell_type_wall)
        while True:
            if self.field[self.beetle_position_x][self.beetle_position_y] != self.cell_type_wall:
                self.path = self.find_exit()
                break
            else:
                self.beetle_position_x = randint(2, 13)
                self.beetle_position_y = randint(2, 13)

    def find_exit(self):
        queue = [(self.beetle_position_x, self.beetle_position_y, [])]
        visited = set()
        while queue:
            x, y, path = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if self.field[x][y] == 0:
                if x == 0 or x == len(self.field) - 1 or y == 0 or y == len(self.field[0]) - 1:
                    return path + [(x, y)]
                queue.append((x + 1, y, path + [(x, y)]))
                queue.append((x - 1, y, path + [(x, y)]))
                queue.append((x, y + 1, path + [(x, y)]))
                queue.append((x, y - 1, path + [(x, y)]))
        return []

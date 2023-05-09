from parametrs import *
from beetle import Beetle
from random import choice


class Field(Beetle):
    def __init__(self):
        super(Field, self).__init__()
        self.field_size_x, self.field_size_y = cell_count_x, cell_count_y
        self.cell_type_none = 0
        self.cell_type_beetle = 1
        self.cell_type_wall = -1
        self.field = [[self.cell_type_none for _ in range(self.field_size_x)
                       ] for _ in range(self.field_size_y)]
    def add_object(self, obj):
        self.field[14][13] = 0 # нормальное добавление выхода(случайное)
        while True:
            j = choice(range(len(self.field)))
            i = choice(range(len(self.field[j])))
            if self.field[j][i] == self.cell_type_none:
                self.field[j][i] = obj
                break
    def clear_field(self):
        for i in range(self.field_size_y):
            for j in range(self.field_size_x):
                if i == 0 or j == 0 or i == self.field_size_x - 1 or j == self.field_size_y -1:
                    self.field[j][i] = self.cell_type_wall
                else:
                    self.field[j][i] = self.cell_type_none
        self.field[self.beetle_position_x][self.beetle_position_y] = \
            self.cell_type_beetle
        for i in range(10):
            self.add_object(self.cell_type_wall)
        self.add_object(self.cell_type_beetle)
        for e in self.field:
            print(e)

    def find_exit(self):
        queue = [(5, 5, [])] # queue должен получать начальные координаты, а не захардкоженные
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
        return None
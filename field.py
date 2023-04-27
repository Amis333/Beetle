from parametrs import *
from beetle import Beetle


class Field(Beetle):
    def __init__(self):
        super(Field, self).__init__()
        self.field_size_x, self.field_size_y = cell_count_x, cell_count_y
        self.cell_type_none = 0
        self.cell_type_beetle = 1
        self.cell_type_wall = -1
        self.field = [[self.cell_type_none for _ in range(self.field_size_x)
                       ] for _ in range(self.field_size_y)]

    def clear_field(self):
        for i in range(self.field_size_y):
            for j in range(self.field_size_x):
                if i == 0 or j == 0 or i == self.field_size_x - 1 or j == self.field_size_y -1:
                    self.field[j][i] = self.cell_type_wall
                else:
                    self.field[j][i] = self.cell_type_none
        self.field[self.beetle_position_x][self.beetle_position_y] = \
            self.cell_type_beetle
        for e in self.field:
            print(e)


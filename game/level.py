level_data = [
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,1],
            [1,0,0,1,0,0,0,0,0,1],
            [1,0,0,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,1],
            [1,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,1,0,1],
            [1,0,0,0,0,0,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1]
]
class Level:

    def __init__(self):
        self.level_data = level_data

    def get_level_data(self):
        return self.level_data

    def set_level_data(self,level_x,level_y,value):
        self.level_data[level_y][level_x] = value




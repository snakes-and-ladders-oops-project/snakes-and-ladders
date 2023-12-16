from cell import Cell

class JumperCell(Cell):
    def __init__(self, cellValue, cellHeight, isFirst=False, isLast=False, jump_to=None):
        super().__init__(cellValue, cellHeight, isFirst, isLast)
        self.jump_to = jump_to

    def jump(self):
        if self.jump_to:
            return self.jump_to
        else:
            return self.cellValue

class SnakeCell(JumperCell):
    def __init__(self, cellValue, cellHeight, isFirst=False, isLast=False, jump_to=None):
        super().__init__(cellValue, cellHeight, isFirst, isLast, jump_to)
        self.color = (220, 20, 60) 

class LadderCell(JumperCell):
    def __init__(self, cellValue, cellHeight, isFirst=False, isLast=False, jump_to=None):
        super().__init__(cellValue, cellHeight, isFirst, isLast, jump_to)
        self.color = (127, 255, 212) 

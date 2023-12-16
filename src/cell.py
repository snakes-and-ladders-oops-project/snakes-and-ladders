import pygame

class Cell:
    
    def __init__(self, cellValue, cellHeight, isFirst = False, isLast = False): 

        self.cellValue = cellValue
        self.CellHeight = cellHeight
        self.isFirst = isFirst
        self.isLast = isLast

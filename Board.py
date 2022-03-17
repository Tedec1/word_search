import pygame

class Cell(pygame.sprite.Sprite):
    """sprite to hold rect and text objects"""

    #constructor
    def __init__(self, y, x, rows, cols, surface ):
        
        #calls the parent constructor
        pygame.sprite.Sprite.__init__(self)
        
        #set the coords of the cell
        self.x = 0
        self.y = 0

        #set the text of the cell
        self.text = " "        
        
        #set the rect to the proper coords and dimensions
        w = surface.get_width()
        h = surface.get_height()
        self.cols = cols
        self.rows = rows
        self.rectangle = pygame.Rect((w / cols) * x, (h / rows) * y, w / cols, h / rows)
        #self.rectangle.fill(0,0,0)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,0), self.rectangle)
        #surface
    
    def print(self):
        print("x: ", self.x, "y: ", self.y)

class Board:
    """a class that handles the grid"""
    def __init__(self, r, c, surface):
        self.cols = c
        self.rows = r
        self.grid = [[None] * self.cols] * self.rows

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
               self.grid[i][j] = Cell(i , j, r, c, surface)
    def getCell(self,r,c):
        r = int(r)
        c = int(c)
        if(r > 0 and r < self.rows and c > 0 and c < self.cols):
            return self.grid[r][c]
        return False
    def setCell(self,r,c,v):
        r = int(r)
        c = int(c)
        v = str(v)
        if(r > 0 and r < self.rows and c > 0 and c < self.cols):
            self.grid[r][c] = v
            return True
        return False



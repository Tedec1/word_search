from Board import Board
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def main():
    height = 500
    width = 500

    screen_ratio = height / width
    screen = init_pygame(width, height)
    running = True
    b = Board( 8, 8, screen)
    while running:
        #has the close button been pressed
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
        draw_grid(screen, b)
    pygame.quit()

def init_pygame(w,h):
    pygame.init()
    return pygame.display.set_mode([w,h])
    
def draw_grid(screen, b):
    #screen.unlock()
    for drawable in b.draw_group:
       pygame.draw.rect(screen, (255,255,255), drawable.rectangle)
    #drawable.draw(screen)
    #for col in range(len(grid)):
    #    for row in range(len(grid[col])):
    #        grid[row][col].draw(screen)
    #        grid[row][col].print()
    #screen.lock()
    return;



main()

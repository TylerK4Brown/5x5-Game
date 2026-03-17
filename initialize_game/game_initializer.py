# Initializes pygame requirements in order for the game to run properly

import pygame
from time import sleep
import random

def pygame_initialize():
    pygame.init()
    # set the size of the screen
    # SCALED flag allows the game resolution to scale to any computer resolution
    # it looks ugly but it does work!
    flags = pygame.SCALED
    screen = pygame.display.set_mode(size=(640,480), flags=flags)
    # creates a Clock object which will later be responsible for setting up the FPS of the game
    clock = pygame.time.Clock()
    return screen, clock

def draw_5x5_grid(screen):
    middle = [screen.get_width() / 2, screen.get_height() / 2]
    # essentially, to keep this rectangle centered, we need to subtract half the width and height
    # the width/height for our rect is (275, 250), so we subtract 137.5 from x and 125 from y
    rect_pos = pygame.Rect(middle[0] - 137.5, middle[1] - 125, 275, 250)
    pygame.draw.rect(screen, "white", rect_pos, width=5)

    # loops across the circle positions list
    # prints each circle in a vertical fashion by displaying a circle at position -100 -> 100 for each pos_horizontal
    # TODO: O(n^2) solution we must kill him
    # Maybe not TODO: actually - this solution is optimal for this methinks
    circle_positions = [-100, -50, 0, 50, 100]
    for pos_horizontal in circle_positions:
        for pos_vertical in circle_positions:
            pygame.draw.circle(screen, "white", [middle[0] + pos_horizontal, middle[1] + pos_vertical], 5)
    
    # update the display
    pygame.display.flip()


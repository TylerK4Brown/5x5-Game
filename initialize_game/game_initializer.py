import pygame
from time import sleep
import random

def pygame_initialize():
    pygame.init()
    # set the size of the screen
    screen = pygame.display.set_mode(size=(600,400))
    # set the FPS of the screen
    clock = pygame.time.Clock()
    return screen, clock

def draw_5x5_grid(screen):
    middle = [screen.get_width() / 2, screen.get_height() / 2]
    # essentially, to keep this rectangle centered, we need to subtract half the width and height from the middle point
    # the middle point is (275, 250), so we subtract 150 from x and 100 from y
    rect_pos = pygame.Rect(middle[0] - 137.5, middle[1] - 125, 275, 250)

    pygame.draw.rect(screen, "white", rect_pos, width=5)

    circle_positions = [-100, -50, 0, 50, 100]
    for pos in circle_positions:
        pygame.draw.circle(screen, "white", [middle[0] + pos, middle[1]], 5)
        pygame.draw.circle(screen, "white", [middle[0], middle[1] + pos], 5)
        pygame.draw.circle(screen, "white", [middle[0] + pos, middle[1] + pos], 5)
        pygame.draw.circle(screen, "white", [middle[0] + pos, middle[1] - pos], 5)
        
    # NEGATIVE VALUES MOVE LEFT/UP, POSITIVE VALUES MOVE RIGHT/DOWN
    # I'm so sure there's a better way to do this but idgaf it is what it is    
    # top of screen
    pygame.draw.circle(screen, "white", [middle[0] - 50, middle[1] - 100], 5)
    pygame.draw.circle(screen, "white", [middle[0] + 50, middle[1] - 100], 5)
    # bottom of screen
    pygame.draw.circle(screen, "white", [middle[0] + 50, middle[1] + 100], 5)
    pygame.draw.circle(screen, "white", [middle[0] - 50, middle[1] + 100], 5)
    # right of screen
    pygame.draw.circle(screen, "white", [middle[0] + 100, middle[1] - 50], 5)
    pygame.draw.circle(screen, "white", [middle[0] + 100, middle[1] + 50], 5)
    # left of screen
    pygame.draw.circle(screen, "white", [middle[0] - 100, middle[1] - 50], 5)
    pygame.draw.circle(screen, "white", [middle[0] - 100, middle[1] + 50], 5)
    pygame.display.flip()


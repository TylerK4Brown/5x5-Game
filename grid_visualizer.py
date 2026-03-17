import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("5x5 Grid Coordinate Visualizer")
font = pygame.font.SysFont("consolas", 11)

center = (320, 240)
offsets = [-100, -50, 0, 50, 100]

screen.fill((0, 0, 0))

# draw bounding rect
rect_pos = pygame.Rect(center[0] - 137.5, center[1] - 125, 275, 250)
pygame.draw.rect(screen, "white", rect_pos, width=2)

# draw grid points and labels
for ox in offsets:
    for oy in offsets:
        x = center[0] + ox
        y = center[1] + oy
        label = font.render(f"{x},{y}", True, (255, 255, 100))
        screen.blit(label, (x - 20, y - 8))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

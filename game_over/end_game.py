# Function that posts the end game screen
# This function will be updated to be more creative, but for now, this will do
import pygame
from time import sleep

def game_over(screen, player_hurtbox):
    # stop the music when the user encounters an obstacle
    # sleep the console for 5 seconds
    pygame.mixer.music.stop()
    
    # plays a pingas death sound and spawns a red square on the grid space where the user died
    pygame.mixer.music.load("sounds\\death_sounds\\pingas_death.mp3")
    pygame.mixer.music.play(start=0.1)
    pygame.draw.rect(screen, "red", player_hurtbox)
    pygame.display.flip()
    sleep(0.8)
    
    # fill the screen with a black color
    # create a new text object, get the rect definition of the text
    # print the text to the screen at the middle of the screen
    screen.fill("black")
    text = pygame.font.SysFont('timesnewroman', 35)
    text_surface = text.render("GAME OVER", True, (255,255,255), None)
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, (300 - (text_rect[2] // 2), 200 - (text_rect[3] // 2)))
    
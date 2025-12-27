import pygame, initialize_game.music as music, player_movement
import initialize_game.game_initializer as initializer

# uses game_initializer module to define the screen dimensions, FPS, and draws the grid to the screen
screen, clock = initializer.pygame_initialize()
initializer.draw_5x5_grid(screen)

# starts playing a song
songpath = ["songs\\pygamesong.mp3", "songs\\pygamesong2.mp3"]
music.song_playback(songpath)
# player position will be set to the middle of the screen
player_pos = [screen.get_width() / 2, screen.get_height() / 2]
running = True
img_surface = pygame.image.load("speedsuprised.png", namehint="png")
img_surface = pygame.transform.scale(img_surface, (30, 30))
# naming the window and setting the icon
pygame.display.set_caption("IShowSpeed on a 5x5 grid")
pygame.display.set_icon(img_surface)

font = pygame.font.Font(None, 36)

# game running logic
while running:
    # user clicked the X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw the player icon at the middle of the screen
    screen.blit(img_surface, (player_pos[0] - 12.5, player_pos[1] - 12.5))
    #pygame.draw.rect(screen, "red", pygame.Rect(player_pos[0] - 12.5, player_pos[1] - 12.5, 25, 25), width=0)
    # move the player with WASD controls
    player_movement.move_player(player_pos, screen)
    # update the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame, initialize_game.music as music, player_movement
import obstacle_info.obstacle_queues as obstacle_queues
import initialize_game.game_initializer as initializer
import obstacle_info.obstacles as obstacles

# uses game_initializer module to define the screen dimensions, FPS, and draw the grid to the screen
screen, clock = initializer.pygame_initialize()
initializer.draw_5x5_grid(screen)

# select which song to play
# (this used to be randomized but I synced up the appearing speeds with this song)
songpath = ["songs\\pygamesong2.mp3"]
music.song_playback(songpath)
# player position will be set to the middle of the screen
player_pos = [screen.get_width() / 2, screen.get_height() / 2]

# load speed, transform speed so that he fits onto the grid
img_surface = pygame.image.load("speedsuprised.png", namehint="png")
img_surface = pygame.transform.scale(img_surface, (30, 30))

# naming the window and setting the icon
pygame.display.set_caption("IShowSpeed on a 5x5 grid")
pygame.display.set_icon(img_surface)

# obstacles are defined by the timestamp in milliseconds and which grid space it should appear on
# this is then added to a queue of obstacles that should appear
obstacle_def = obstacle_queues.queue_storage("hiiiii")
obstacle_queue = obstacles.queue_item(obstacle_def)
# FPS of the game
clock.tick(60)

# game running logic
running = True
while running:
    # user clicked the X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw the player icon at the middle of the screen
    screen.blit(img_surface, (player_pos[0] - 15, player_pos[1] - 15))
    # old code for an icon that isn't IShowSpeed
    #pygame.draw.rect(screen, "red", pygame.Rect(player_pos[0] - 12.5, player_pos[1] - 12.5, 25, 25), width=0)
    
    # move the player with WASD controls
    player_movement.move_player(player_pos, screen)
    # check if an obstacle should spawn
    obstacles.check_obstacle(obstacle_queue, img_surface, screen)
    # checktime = music.check_playback_time()
    # print(checktime)
    
    # update the screen, 
    pygame.display.flip()

pygame.quit()

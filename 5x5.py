# test change to the branch
import pygame
import initialize_game.music as music
import player_movement
import obstacle_info.obstacle_queues as obstacle_queues
import initialize_game.game_initializer as initializer
from obstacle_info.Obstacle_oop import Obstacles

def main():
    # uses game_initializer module to define the screen dimensions, FPS, and draw the grid to the screen
    screen, clock = initializer.pygame_initialize()
    initializer.draw_5x5_grid(screen)

    # select which song to play
    # (this used to be randomized but I synced up the appearing speeds with this song)
    songpath = ["songs\\pygamesong2.mp3"]
    music.song_playback(songpath)
    # player position will be set to the middle of the screen
    player_pos = [screen.get_width() / 2, screen.get_height() / 2]
    
    # load speed icon, transform speed so that he fits onto the grid
    img_surface = pygame.image.load("speedsuprised.png", namehint="png")
    img_surface = pygame.transform.scale(img_surface, (30, 30))

    # eventually this function will be used to call the proper obstacle queue depending on the song that is playing
    obstacle_queue = obstacle_queues.create_queue("song_name")
    # create an obstacles object, constructor obstacle_queue
    # load the obstacle image so it can be displayed on screen
    obstacles = Obstacles(obstacle_queue)
    obstacles.load_obstacle_img()

    # naming the window and setting the icon
    pygame.display.set_caption("IShowSpeed on a 5x5 grid")
    pygame.display.set_icon(img_surface)
    
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
        
        # defines and draws the hitbox for Speed using a rect
        player_hurtbox = pygame.Rect(player_pos[0] - 15, player_pos[1] - 15, 30, 30)
        pygame.draw.rect(screen, "green", player_hurtbox, width=2)
        
        # move the player with WASD controls
        player_movement.move_player(player_pos, screen)
        # check if an obstacle should spawn
        obstacles.spawn_obstacle(screen)
        # check if speed is interacting with an obstacle
        running = obstacles.check_hitbox_interaction(player_hurtbox)
        
        # test code that I'm keeping here for now
        # checktime = music.check_playback_time()
        # print(checktime)
        # update the screen
        pygame.display.flip()
    
    close = False
    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
    
    pygame.quit()

if __name__ == "__main__":
    main()

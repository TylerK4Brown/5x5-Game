# This branch takes an object-oriented approach to the functional implementation in branch "main"
# The current functionality spawns pingas obstacles to the rhythm of a song and ends the game when the user runs into an obstacle
# This remains the same in this version, but the obstacles and player information are now defined in classes
# Last update: 1/5/2025
import pygame
import initialize_game.music as music
import obstacle_info.obstacle_queues as obstacle_queues
import initialize_game.game_initializer as initializer
from obstacle_info.Obstacle_oop import Obstacles
from player_info.Player_oop import Player

def main():
    # uses game_initializer module to define the screen dimensions, FPS, and draw the grid to the screen
    screen, clock = initializer.pygame_initialize()
    initializer.draw_5x5_grid(screen)

    # select which song to play
    # (this used to be randomized but I synced up the appearing obstacles with this song)
    songpath = ["songs\\pygamesong2.mp3"]
    music.song_playback(songpath)
    # TODO: view the below comment
    # eventually this function will be used to call the proper obstacle queue depending on the song that is playing
    obstacle_queue = obstacle_queues.create_queue("song_name")
    # player position will be set to the middle of the screen
    player_position = [screen.get_width() / 2, screen.get_height() / 2]
    player = Player(player_position, screen)
    # create an obstacles object, constructor obstacle_queue
    # load the obstacle image so it can be displayed on screen (updates the class variable)
    obstacles = Obstacles(obstacle_queue)
    obstacles.load_obstacle_img()

    # naming the window
    pygame.display.set_caption("IShowSpeed on a 5x5 grid") 
    
    # FPS of the game
    clock.tick(60)
    # game running logic
    running = True
    while running:
        # user clicked the X to close the window
        # TODO: this is currently bugged - you have to click X twice to exit the game successfully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # continuously draw the player to the screen
        player_hurtbox = player.draw_player()
        # move the player with WASD controls, redraw spaces that have been traced over by the player
        player.move_player(obstacles.get_warning_list())
        # check if an obstacle should spawn
        obstacles.spawn_obstacle(screen)
        # check if speed is interacting with an obstacle
        keep_running = obstacles.check_hitbox_interaction(player_hurtbox, screen)
        
        # exit the running loop if the user encounters an obstacle
        if keep_running == False:
            running = False
        # update the screen
        pygame.display.flip()
    
    # TODO: this works for when the user encounters an obstacle
    # does not work when the user tries to exit normally (requires two clicks of the X button)
    # fix this pl0x
    close = False
    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
    pygame.quit()

if __name__ == "__main__":
    main()

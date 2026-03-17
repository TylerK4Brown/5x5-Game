# This branch takes an object-oriented approach to the functional implementation in branch "main"
# The current functionality spawns pingas obstacles to the rhythm of a song and ends the game when the user runs into an obstacle
# This remains the same in this version, but the obstacles and player information are now defined in classes
import pygame
import initialize_game.music as music
import obstacle_info.obstacle_queues as obstacle_queues
import initialize_game.game_initializer as initializer
from obstacle_info.Obstacle_oop import Obstacles
from player_info.Player_oop import Player
from game_over import end_game
import os, time
    
def main():
    running, initialize_game = True, True
    while running:
        # initializes the game if the game has not been initialized already
        # this only happens when the game starts up or when the user wishes to restart the game
        if initialize_game:
            os.system('cls')
            screen, clock = initializer.pygame_initialize()
            initializer.draw_5x5_grid(screen)

            # select which song to play
            # (this used to be randomized but I synced up the appearing obstacles with this song)
            songpath = ["sounds\\songs\\pygamesong2.mp3"]
            music.song_playback(songpath)
            # TODO: eventually this function will be used to call the proper obstacle queue depending on the song that is playing
            obstacle_queue = obstacle_queues.create_queue("song_name")
            # player position will be set to the middle of the screen
            player_position = [screen.get_width() / 2, screen.get_height() / 2]
            player = Player(player_position, screen)
            # create an obstacles object, constructor obstacle_queue
            # load the obstacle image so it can be displayed on screen (updates the class member)
            obstacles = Obstacles(obstacle_queue)
            obstacles.load_obstacle_img()

            # naming the window
            pygame.display.set_caption("IShowSpeed on a 5x5 grid") 
            
            # FPS of the game
            clock.tick(60)
            initialize_game = False
        # user clicked the X to close the window
        # TODO: this closes with an error since the running loop closes unexpectly - causes the game to close ungracefully
        # figure out how to make this graceful
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        player_hurtbox = player.draw_player()
        # move the player with WASD controls, redraw spaces that have been traced over by the player
        player.move_player(obstacles.get_warning_list())
        # check if an obstacle should spawn
        obstacles.spawn_obstacle(screen)
        # check if speed is interacting with an obstacle
        keep_running = obstacles.check_hitbox_interaction(player_hurtbox, screen)
        # update the screen
        pygame.display.flip()
        
        # exit the running loop if the user encounters an obstacle
        # calls the game_over function in end_game to print a game over screen
        # currently uses the terminal to determine whether the game should continue or not
        if not keep_running:
            end_game.game_over(screen, player_hurtbox)
            os.system('cls')
            user_in = int(input("Would you like to continue?\n1.) Yes\n2.) No\nInput: "))
            
            # if the user selects 1, continue the game and clear all obstacle hitboxes from their corresponding lists
            if user_in == 1:
                obstacles.obstacle_list.clear()
                obstacles.warning_list.clear()
                initialize_game = True
            # if the user selects 2, exit the game and display a rude message for 2 seconds before closing
            elif user_in == 2:
                screen.fill("black")
                pygame.display.flip()
                text = pygame.font.SysFont('timesnewroman', 35)
                middle = [screen.get_width() / 2, screen.get_height() / 2]
                text_surface = text.render("fuck you then. LEAVE.", True, (255,255,255), None)
                text_rect = text_surface.get_rect()
                screen.blit(text_surface, (middle[0] - (text_rect[2] // 2), middle[1] - (text_rect[3] // 2)))
                pygame.display.flip()
                time.sleep(2)
                running = False
            
    pygame.quit()
    
if __name__ == "__main__":
    main()

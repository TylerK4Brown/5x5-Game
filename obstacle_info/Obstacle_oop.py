# Object-oriented implementation of the obstacles that appear on screen
# In the functional implementation, the obstacle_queue and obstacle_list were propegated through main
# This pushes those variables into a class structure instead
# Both implementations work, this might be better?

import pygame
from collections import deque
from initialize_game import music
from game_over import end_game

class Obstacles:
    # obstacle_list and obstacle_image defined as class variables
    obstacle_list = []
    obstacle_img_surface = None
    
    # idea:
    # have a function that defines the queue items depending on which song is called
    # ^ this is in a TODO in obstacle_queues.py
    # pass that queue into this class as a constructor
    def __init__(self, obstacle_queue: deque):
        self.obstacle_queue = obstacle_queue
    
    # function that loads the obstacle image
    # updates the obstacle_img_surface class variable to be used in spawn_obstacle
    def load_obstacle_img(self):
        image = "pingas_obstacle.png"
        self.obstacle_img_surface = pygame.image.load(image, namehint="png")
        self.obstacle_img_surface = pygame.transform.scale(self.obstacle_img_surface, (30, 30))
    
    # function that spawns the obstacles on the correct grid space based on the playback of the song
    def spawn_obstacle(self, screen):
        if len(self.obstacle_queue) == 0:
            return

        current_time = music.check_playback_time()
        if current_time >= self.obstacle_queue[0][0]:
            # dequeue the top most element, get the grid space information from the 1st index in the tuple
            obstacle_definition = self.obstacle_queue.popleft()
            grid_space = obstacle_definition[1]
            # add the obstacle to the screen, create a hitbox rect at that grid space
            screen.blit(self.obstacle_img_surface, (grid_space[0] - 15, grid_space[1] - 15))
            obstacle_hitbox = pygame.Rect(grid_space[0] - 15, grid_space[1] - 15, 30, 30)
            # draws the hitbox to the screen (not necessary later on - just for visuals rn)
            pygame.draw.rect(screen, "red", obstacle_hitbox, width=2)
            self.obstacle_list.append(obstacle_hitbox)
    
    # checks to see if the player's current position interacts with the current list of obstacles
    # if there are no obstacles in the obstacle list at the moment, return True
    # if any hitboxes overlap, return False to kill the program's running loop
    # if there is no overlap, return True
    def check_hitbox_interaction(self, player_hurtbox, screen):
        if len(self.obstacle_list) == 0:
            return True
        
        if pygame.Rect.collidelist(player_hurtbox, self.obstacle_list) != -1:
            print(f"Collision detected at {player_hurtbox}")
            end_game.game_over(screen)
            return False
    
        return True
    
    
        
        
    
           
    
    
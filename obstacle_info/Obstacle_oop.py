# Object-oriented implementation of the obstacles that appear on screen
# In the functional implementation, the obstacle_queue and obstacle_list were propegated through main
# This pushes those variables into a class structure instead
# Both implementations work, this might be better?
import pygame
import pygame.gfxdraw
from collections import deque
from initialize_game import music
from game_over import end_game

class Obstacles:
    # obstacle_list and obstacle_image defined as class variables
    obstacle_list = []
    warning_list = []
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
        image = "images\\pingas_obstacle.png"
        self.obstacle_img_surface = pygame.image.load(image, namehint="png")
        self.obstacle_img_surface = pygame.transform.scale(self.obstacle_img_surface, (30, 30))
    
    # function that spawns the obstacles on the correct grid space based on the playback of the song
    def spawn_obstacle(self, screen):
        if len(self.obstacle_queue) == 0:
            return

        current_time = music.check_playback_time()
        if current_time >= self.obstacle_queue[0][0]:
            # dequeue the top most element, get the grid space information from the 1st index in the tuple
            # obstacle_definition looks like [x, y]
            obstacle_definition = self.obstacle_queue.popleft()
            grid_space = obstacle_definition[2]
            
            # NEW IMPLEMENTATION:
            # queue now holds a "warning", "obstacle" or  indicator
            # if the current "obstacle_definition" is "obstacle", draw a pingas obstacle - draw a yellow square otherwise
            # there's also a despawn case that hasn't been implemented yet
            # UPDATE: queue now holds a nested list at index 2
            # ^^^ this allows for multiple obstacles to be spawned from one queue entry
            if len(grid_space) > 1:
                for coordinates in grid_space:
                    obstacle_space = pygame.Rect(coordinates[0] - 15, coordinates[1] - 15, 30, 30)
                    if obstacle_definition[1] == 'obstacle':
                        screen.blit(self.obstacle_img_surface, (coordinates[0] - 15, coordinates[1] - 15))
                        pygame.gfxdraw.rectangle(screen, obstacle_space, (255, 0, 0, 255))
                        self.obstacle_list.append(obstacle_space)
                        
                    elif obstacle_definition[1] == 'warning':
                        pygame.gfxdraw.box(screen, obstacle_space, (255, 255, 0, 128))
                        self.warning_list.append(obstacle_space)
                    # Else - obstacle_definitions = 'despawn', so draw a regular box back onto the screen
                    # Remove the hitbox and warning Rects from the obstacle/warning_lists
                    # TODO: code is repetitive, this will need to be refactored
                    else:
                        pygame.draw.rect(screen, "black", obstacle_space, width=0)
                        pygame.draw.circle(screen, "white", [coordinates[0], coordinates[1]], 5)
                        remove_obstacle = pygame.Rect(coordinates[0] - 15, coordinates[1] - 15, 30, 30)
                        self.obstacle_list.remove(remove_obstacle)
                        self.warning_list.remove(remove_obstacle)
            # If the grid space isn't greater than 1, then spawn only one obstacle.
            else:
                obstacle_space = pygame.Rect(grid_space[0] - 15, grid_space[1] - 15, 30, 30)
                if obstacle_definition[1] == 'obstacle':
                    screen.blit(self.obstacle_img_surface, (grid_space[0] - 15, grid_space[1] - 15))
                    pygame.gfxdraw.rectangle(screen, obstacle_space, (255, 0, 0, 255))
                    self.obstacle_list.append(obstacle_space)
                
                elif obstacle_definition[1] == 'warning':
                    pygame.gfxdraw.box(screen, obstacle_space, (255, 255, 0, 128))
                    self.warning_list.append(obstacle_space)
                # Else - obstacle_definitions = 'despawn', so draw a regular box back onto the screen
                # Remove the hitbox and warning Rects from the obstacle/warning_lists
                # TODO: code is repetitive, this will need to be refactored
                else:
                    pygame.draw.rect(screen, "black", obstacle_space, width=0)
                    pygame.draw.circle(screen, "white", [coordinates[0], coordinates[1]], 5)
                    print(self.obstacle_list)
                    remove_obstacle = pygame.Rect(coordinates[0] - 15, coordinates[1] - 15, 30, 30)
                    self.obstacle_list.remove(remove_obstacle)
                    self.warning_list.remove(remove_obstacle)
            
    # checks to see if the player's current position interacts with the current list of obstacles
    # if there are no obstacles in the obstacle list at the moment, return True
    # if any hitboxes overlap, return False to kill the program's running loop
    # if there is no overlap, return True
    def check_hitbox_interaction(self, player_hurtbox, screen):
        if len(self.obstacle_list) == 0:
            return True
        
        if pygame.Rect.collidelist(player_hurtbox, self.obstacle_list) != -1:
            print(f"Collision detected at {player_hurtbox}")
            return False
    
        return True
    
    def get_warning_list(self):
        return self.warning_list
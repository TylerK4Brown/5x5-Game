import pygame
from collections import deque
from initialize_game import music

class Obstacles:
    obstacle_list = []
    obstacle_img_surface = None
    
    # idea:
    # have a function that defines the queue items depending on which song is called
    # pass that queue into this class as a constructor
    def __init__(self, obstacle_queue: deque):
        self.obstacle_queue = obstacle_queue
    
    def load_obstacle_img(self):
        image = "pingas_obstacle.png"
        self.obstacle_img_surface = pygame.image.load(image, namehint="png")
        self.obstacle_img_surface = pygame.transform.scale(self.obstacle_img_surface, (30, 30))
        
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
            #print(self.obstacle_list)
    
    def check_hitbox_interaction(self, player_hurtbox):
        if len(self.obstacle_list) == 0:
            return True
        
        if pygame.Rect.collidelist(player_hurtbox, self.obstacle_list) != -1:
            print(f"Collision detected at {player_hurtbox}")
            return False
        
        return True
    
    
        
        
    
           
    
    
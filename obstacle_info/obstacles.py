# every queue item should follow this exact format (eventually)
# (timestamp, type_of_obstacle, obstacle_stage, [x,y])

from obstacle_info import end_game
from collections import deque
from initialize_game import music
import pygame

# queued elements that follow this format (for right now):
# [(timestamp(ms), [x,y])]
# this is just to test if it works
def queue_item(obstacle_def: list) -> deque: 
    # eventual implementation I'm tryna figure it out
    queue = deque(obstacle_def)
    return queue

# Checks if an obstacle should spawn on the screen based on the song playback
# If an obstacle should spawn, add it to the screen and append its pygame.Rect object definition to the obstacle_list
def check_obstacle(obstacle_queue: deque, obstacle_img_surface, screen, obstacle_list: list) -> list:
    # if there's nothing in the queue, don't proceed
    if len(obstacle_queue) == 0:
        return obstacle_list
    
    # checks the playback time - if the playback time matches the top queue element:
    # 1. remove that element from the queue
    # 2. draw the specific obstacle at the specified grid space
    # 3. append the rect of the hitbox to a running list of rects - this will be used to detect collision
    current_time = music.check_playback_time()
    if current_time >= obstacle_queue[0][0]:
        # dequeue the top most element, get the grid space information from the 1st index in the tuple
        obstacle_def = obstacle_queue.popleft()
        grid_space = obstacle_def[1] 
        # add the obstacle to the screen, create a hitbox rect at that grid space
        screen.blit(obstacle_img_surface, (grid_space[0] - 15, grid_space[1] - 15))
        hitbox = pygame.Rect(grid_space[0] - 15, grid_space[1] - 15, 30, 30)
        # draws the hitbox to the screen (not necessary later on - just for visuals rn)
        pygame.draw.rect(screen, "red", hitbox, width=2)
        obstacle_list.append(hitbox)
        
    return obstacle_list

# Checks if the player hitbox is currently interacting with another hitbox on screen
# Rect.collidelist holds all the obstacles currently on screen
# hitbox holds the player's position as a Rect
def check_hitbox_interaction(hitbox, obstacle_list: list, screen, running) -> list:
    # if the obstacle_list is empty, return
    if len(obstacle_list) == 0:
        return obstacle_list

    if pygame.Rect.collidelist(hitbox, obstacle_list) != -1:
        print(f"Collision detected at {hitbox}")
        obstacle_list.remove(hitbox)
        # redraw the screen as black
        screen.fill("black")
        pygame.mixer.music.stop()
        i = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if i == 0:
                print("Game over!")
                #end_game.game_over()
                i += 1
                    
    return obstacle_list
# every queue item should follow this exact format (eventually)
# (timestamp, type_of_obstacle, obstacle_stage, [x,y])

from collections import deque
from initialize_game import music
import pygame

# queued elements that follow this format (for right now):
# [(timestamp(ms), [x,y])]
# this is just to test if it works
def queue_item(obstacle_def: list): 
    # eventual implementation I'm tryna figure it out
    queue = deque(obstacle_def)
    return queue

def check_obstacle(obstacle_queue, obstacle_img_surface, screen):
    # if there's nothing in the queue, don't proceed
    if len(obstacle_queue) == 0:
        return None
    
    # checks the playback time - if the playback time matches the top queue element:
    # 1. remove that element from the queue
    # 2. draw the specific obstacle at the specified grid space
    current_time = music.check_playback_time()
    if current_time >= obstacle_queue[0][0]:
        obstacle_def = obstacle_queue.popleft()
        grid_space = obstacle_def[1] # this holds the coordinates of the obstacle
        screen.blit(obstacle_img_surface, (grid_space[0] - 15, grid_space[1] - 15))
        #pygame.draw.rect(screen, "red", pygame.Rect(grid_space[0] - 15, grid_space[1] - 15, 30, 30), width=0)



# obstacle_def = [1100, "hi"]
# obstacle_queue = queue_item(obstacle_def)

# text = check_obstacle(obstacle_queue)
# print(text)

# old logic that I'm keeping for now in case this shit breaks
    # queue = deque([(obstacle_def[0], obstacle_def[1])])
    
    # queue.append((737, [200, 100]))
    # queue.append((1164, [200, 300]))
    # queue.append((1680, [400, 100]))
    # queue.append((1930, [400, 200]))
    # queue.append((2200, [400, 300]))
    # queue.append((2328, [300, 100]))
    # queue.append((2856, [250, 150]))
    # queue.append((3293, [350, 250]))
    # queue.append((3780, [350, 150]))
    # queue.append((3940, [250, 250]))
    # queue.append((4170, [300, 300]))
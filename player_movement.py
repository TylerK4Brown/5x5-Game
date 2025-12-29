# MAXIMUM DIMENSIONS ARE AS FOLLOWS:
# up (w) = 100
# down (s) = 300
# left (a) = 200
# right (d) = 400

import pygame

# refresh the grid space so that the icon does not leave a trail
def redraw(player_pos, screen):
    pygame.draw.rect(screen, "black", pygame.Rect(player_pos[0] - 15, player_pos[1] - 15, 30, 30), width=0)
    pygame.draw.circle(screen, "white", [player_pos[0], player_pos[1]], 5)

def move_player(player_pos, screen):
    # NEGATIVE VALUES MOVE LEFT/UP, POSITIVE VALUES MOVE RIGHT/DOWN
    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_w]:
        if player_pos[1] <= 100:
            pass
        else:
            redraw(player_pos, screen)
            player_pos[1] -= 50
            print(player_pos)
            pygame.display.flip()
    
    if keys[pygame.K_s]:
        if player_pos[1] >= 300:
            pass
        else:
            redraw(player_pos, screen)
            player_pos[1] += 50
            print(player_pos)
            pygame.display.flip()
        
    if keys[pygame.K_a]:
        if player_pos[0] <= 200:
            pass
        else:
            redraw(player_pos, screen)
            player_pos[0] -= 50
            print(player_pos)
            pygame.display.flip()
            
    if keys[pygame.K_d]:
        if player_pos[0] >= 400:
            pass
        else:
            redraw(player_pos, screen)
            player_pos[0] += 50
            print(player_pos)
            pygame.display.flip()

    return player_pos
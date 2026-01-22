# Object-oriented implementation of the player information
# In the functional implementation, variables such as player_position and the hurtbox were defined in main
# This creates a class that makes it so that this information is contained in one space

import pygame
import pygame.gfxdraw

class Player:
    # class variable that defines the player's icon image
    player_img_surface = None
    
    # constructor for the class Player
    def __init__(self, player_position: list, screen):
        self.player_position = player_position
        self.screen = screen
    
    # function that draws the player to the screen
    # this function is called in the game's running loop so that the player's position and hurtbox locations are updated frequently
    def draw_player(self):
        image = "speedsuprised.png"
        self.player_img_surface = pygame.image.load(image, namehint="png")
        self.player_img_surface = pygame.transform.scale(self.player_img_surface, (30, 30))
         # draw the player icon at the middle of the screen
        self.screen.blit(self.player_img_surface, (self.player_position[0] - 15, self.player_position[1] - 15))
        
        # defines and draws the hitbox for Speed using a rect
        player_hurtbox = pygame.Rect(self.player_position[0] - 15, self.player_position[1] - 15, 30, 30)
        pygame.gfxdraw.rectangle(self.screen, player_hurtbox, (0, 255, 0, 255))
        return player_hurtbox
    
    # moves the player across the grid spaces, updates the player_position
    # MAXIMUM DIMENSIONS ARE AS FOLLOWS:
    # up (w) = 100
    # down (s) = 300
    # left (a) = 200
    # right (d) = 400
    def move_player(self):
        # NEGATIVE VALUES MOVE LEFT/UP, POSITIVE VALUES MOVE RIGHT/DOWN
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_w]:
            if self.player_position[1] <= 100:
                pass
            else:
                Player.redraw(self)
                self.player_position[1] -= 50
                pygame.display.flip()
        
        if keys[pygame.K_s]:
            if self.player_position[1] >= 300:
                pass
            else:
                Player.redraw(self)
                self.player_position[1] += 50
                pygame.display.flip()
            
        if keys[pygame.K_a]:
            if self.player_position[0] <= 200:
                pass
            else:
                Player.redraw(self)
                self.player_position[0] -= 50
                pygame.display.flip()
                
        if keys[pygame.K_d]:
            if self.player_position[0] >= 400:
                pass
            else:
                Player.redraw(self)
                self.player_position[0] += 50
                pygame.display.flip()
    
    # redraws a grid space after the player moves off of it
    def redraw(self):
        pygame.draw.rect(self.screen, "black", pygame.Rect(self.player_position[0] - 15, self.player_position[1] - 15, 30, 30), width=0)
        pygame.draw.circle(self.screen, "white", [self.player_position[0], self.player_position[1]], 5)
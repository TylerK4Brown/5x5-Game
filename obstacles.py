# creating a class that defines how an obstacle should spawn
# each obstacle will have coordinates and timestamps along with them
#
# obstacle_coords: a nested list ([[]]), where:
# - the inner list contains x,y coordinates of where the obstacle should be placed
# - the outer list contains the listing of these x,y coordinates
# 
# timestamps: a single list with 3 values:
# - warning_timestamp: the first value in this list, which spawns a warning box around the grid spaces that will be impacted
# - active_timestamp – the second value in this list, which spawns the hitbox to the screen at this timestamp
# - fadeout_timestamp - the final value in this list to determine when the hitbox should fade off the screen

class Obstacles:
    def __init__(self, obstacle_coords: list, timestamps: list):
        self.occupied_spaces = obstacle_coords
        self.timestamps = timestamps
    
    # TODO: add obstacles to the screen based on the input coordinates for any given object
    def add_obstacle(self, occupied_spaces):
        pass
    
obstacle = Obstacles([[200,150], [100, 150]], [1, 1.5, 2])
print(obstacle.timestamps)
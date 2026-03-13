# Creates a queue out of the listing of obstacles that should appear at a given time
# Each queue element operates as follows:
# (time_in_milliseconds, [coordinate x, coordinate y])
#
# TODO: eventually, queue elements will look like this:
# (time_in_milliseconds, obstacle_type, obstacle_stage, [coordinate x, coordinate y])
from collections import deque

def create_queue(song_name):
    # song_name is not used yet since we only have obstacles appearing for one song
    py_game_song_1_queue = [(100, "warning", [200, 200]), (737, "obstalce", [200, 100]), (1164, "warning", [200, 300]), (1680, "warning", [400, 100]), 
    (1930, "warning", [400, 200]), (2200, "obstacle", [400, 300]), (2328, "warning", [300, 100]), (2856, "warning", [250, 150]), 
    (3293, "warning", [350, 250]), (3780, "warning", [350, 150]), (3940, "warning", [250, 250]), (4170, "warning", [300, 300])]
    
    queue = deque(py_game_song_1_queue)
    return queue
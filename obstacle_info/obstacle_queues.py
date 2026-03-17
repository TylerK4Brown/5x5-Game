# Creates a queue out of the listing of obstacles that should appear at a given time
# Each queue element operates as follows:
# (time_in_milliseconds, [coordinate x, coordinate y])
#
# TODO: eventually, queue elements will look like this:
# (time_in_milliseconds, obstacle_type, obstacle_stage, [coordinate x, coordinate y])
from collections import deque

def create_queue(song_name):
    # song_name is not used yet since we only have obstacles appearing for one song
    # THIS QUEUE USED TO WORK WITH 600,400 RESOLUTION
    # WE ARE NOW SWITCHING TO 640x480
    py_game_song_1_queue = [
        (100, "warning", [[220, 240], [220, 190], [220, 140], [270, 140]]),
        (737, "warning", [[370, 340], [420, 340], [420, 290], [420, 240]]),
        (1164, "obstacle", [[370, 340], [420, 340], [420, 290], [420, 240], [220, 240], [220, 190], [220, 140], [270, 140]]),
        (1660, "despawn", [[370, 340], [420, 340], [420, 290], [420, 240], [220, 240], [220, 190], [220, 140], [270, 140]]),
        (1680, "warning", [[270, 340], [270, 140], [370, 340], [370, 140]]),
        (1930, "warning", [[270, 290], [270, 190], [370, 290], [370, 190]]),
        (2200, "warning", [[220, 190], [220, 290], [420, 190], [420, 290]]),
        (2328, "warning", [[220, 240], [420, 240]]),
        (2856, "obstacle", [[270, 190], [220, 190], [370, 190], [420, 190], [270, 290], [220, 290], [370, 290], [420, 290]]),
        (3293, "obstacle", [[270, 140], [220, 240], [270, 340], [370, 140], [420, 240], [370, 340]]),
        (3750, "despawn", [[270, 190], [220, 190], [370, 190], [420, 190], [270, 290], [220, 290], [370, 290], [420, 290], [270, 140], [220, 240], [270, 340], [370, 140], [420, 240], [370, 340]]),
        (3780, "warning", [[220, 190], [420, 190]]), 
        (3940, "obstacle", [[370, 240], [270, 240]]), 
        (4170, "warning", [[220, 290], [420, 290]])
    ]
    # py_game_song_1_queue = [
    # (100, "warning", [200, 100]), 
    # (100, "warning", [200, 150]),
    # (100, "warning", [200, 200]), 
    # (100, "warning", [250, 100]), 
    # (737, "warning", [400, 200]),
    # (737, "warning", [400, 250]),
    # (737, "warning", [400, 300]),
    # (737, "warning", [350, 300]),
    # (1164, "obstacle", [200, 100]), 
    # (1164, "obstacle", [200, 150]),
    # (1164, "obstacle", [200, 200]), 
    # (1164, "obstacle", [250, 100]), 
    # (1164, "obstacle", [400, 200]),
    # (1164, "obstacle", [400, 250]),
    # (1164, "obstacle", [400, 300]),
    # (1164, "obstacle", [350, 300]),
    # (1680, "warning", [350, 150]),
    # (1680, "warning", [250, 250]),
    # (1930, "warning", [400, 100]),
    # (1930, "warning", [200, 300]),
    # (2200, "warning", [400, 150]),
    # (2200, "warning", [350, 100]),
    # (2200, "warning", [200, 250]),
    # (2200, "warning", [250, 300]),
    # (2328, "obstacle", [350, 150]),
    # (2328, "obstacle", [250, 250]),
    # (2856, "obstacle", [400, 100]),
    # (2856, "obstacle", [200, 300]),
    # (3293, "obstacle", [200, 250]),
    # (3293, "obstacle", [250, 300]),
    # (3293, "obstacle", [400, 150]),
    # (3293, "obstacle", [350, 100]),
    # ] 
    #  
    #  
    # (3293, "warning", [350, 250]), 
    # (3780, "warning", [350, 150]), 
    # (3940, "warning", [250, 250]), 
    # (4170, "warning", [300, 300])
    
    queue = deque(py_game_song_1_queue)
    return queue
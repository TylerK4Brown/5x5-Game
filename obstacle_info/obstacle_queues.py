from collections import deque
# returns an ordered list of queue items for each song
def create_queue(song_name):
    # song_name is not used yet since we only have obstacles appearing for one song
    py_game_song_1_queue = [(100, [200, 200]), (737, [200, 100]), (1164, [200, 300]), (1680, [400, 100]), 
    (1930, [400, 200]), (2200, [400, 300]), (2328, [300, 100]), (2856, [250, 150]), 
    (3293, [350, 250]), (3780, [350, 150]), (3940, [250, 250]), (4170, [300, 300])]
    
    queue = deque(py_game_song_1_queue)
    return queue
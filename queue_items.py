# VERY barebones scaffolding for how queuing obstacles will work for execution
# What needs to be implemented is sorting so that queue objects can be ordered by ms
from collections import deque

running = True
# create the new queue to start appending items to
obstacle_queue = deque()

# current obstacle definition before we get too crazy:
# (time_in_ms, [coordinate_1, coordinate_2])
while running == True:
    # input all the relevant information
    time_in_ms = input("Please input time in ms: ")
    coordinate_1 = input("Enter coordinate 1: ")
    coordinate_2 = input("Enter coordinate 2: ")
    
    # queue that information 
    obstacle_queue.append((time_in_ms, [coordinate_1, coordinate_2]))
    print(f"Current queue: {obstacle_queue}")
    
    # TODO: implement sorting so that queue items that are out of order in terms of the ms value can be sorted by their ms value
    user_in = input("Would you like to add more obstacles? \nPlease enter \"Yes\" or \"No\"")
    if user_in.lower() == "no":
        running = False

# create a file to store that queue information
with open("queued_items.txt", "a") as file:
    file.write(str(obstacle_queue))

print("queue has been written to a file")

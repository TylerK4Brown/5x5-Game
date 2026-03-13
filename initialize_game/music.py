# initializes the song for the game and starts playing it
import pygame, random

# TODO: this function will be updated soon to select the proper music file to play depending on the obstacle queue that is loaded
# keeping this in mind for now
def song_playback(song_path):
    song = random.choice(song_path)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1, start=1)

# get the current playback time in milliseconds
# this was mostly used for debugging but may be used for a level creation implementation later on
def check_playback_time():
    playback_time = pygame.mixer.music.get_pos()
    return playback_time 
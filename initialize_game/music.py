import pygame, random

def song_playback(song_path):
    song = random.choice(song_path)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1, start=1)

def check_playback_time():
    # get the current playback time in milliseconds
    playback_time = pygame.mixer.music.get_pos()
    return playback_time 
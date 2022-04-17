import pygame
from pygame import mixer
pygame.init()

class Engine:

    def __init__(self):
        mixer.init()

    def load(self, file: str):
       """
       Loading a music file and playing for ingame music purposes
       :param file: file path to the sound file
       """
       mixer.music.load(file)

    def playback(self, volume: float):
        mixer.music.set_volume(volume)
        mixer.music.play()
import pygame
pygame.mixer.init()
#no lugar de music.mp3, indicar o caminho do arquivo 
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()
import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((800,800)) #Skapar fönster : Manipulera inte variabeln, det gör ingenting
pygame.display.set_caption("Test")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): #Skickar tillbaka en lista med events?
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
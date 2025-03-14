import pygame,sys

""""""
pygame.init()

wight = 200
hight = 500

screen = pygame.display.set_mode((wight,hight))
# pygame.display.set_icon('icon_game.png')
game_ran = True


while game_ran :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
import pygame

class plaer ():
    def __init__(self,Screen,Skin):

        self.Screen = Screen
        self.Skin = pygame.image.load(Skin)

        self.Screen_rect = self.Screen.get_rect()
        self.rect = self.Skin.get_rect()
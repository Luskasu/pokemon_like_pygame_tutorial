from settings import *
from os.path import join


class Object(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        self.image = pygame.Surface((100, 100))
        self.image.fill('blue')
        self.rect = self.image.get_frect(center = pos)
    
    
    
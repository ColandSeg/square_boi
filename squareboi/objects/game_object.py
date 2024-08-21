from pygame import Surface
from pygame.sprite import Sprite

class GameObject(Sprite):
    def __init__(self, surface: Surface, pos: tuple[int, int], speed=0):
        super(GameObject, self).__init__()
        self.surf = surface
        self.rect = self.surf.get_rect(topleft = pos)
        self.speed = speed

    def draw(self, screen: Surface):
        screen.blit(self.surf, self.rect)

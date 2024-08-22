from pygame import Surface
from pygame.sprite import Sprite
from pygame.math import Vector2

class GameObject(Sprite):
    def __init__(self, surface: Surface, pos: tuple[int, int], speed=0):
        super(GameObject, self).__init__()
        self.surf = surface
        self.rect = self.surf.get_rect(topleft = pos)
        self.speed = speed

        self.direction = Vector2(0, 0)

    def draw(self, screen: Surface):
        screen.blit(self.surf, self.rect)

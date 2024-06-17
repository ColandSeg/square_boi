from pygame import Surface

class GameObject:
    def __init__(self, surface: Surface, pos: tuple[int, int]):
        self.surf = surface
        self.rect = self.surf.get_rect(topleft = pos)

    def draw(self, screen: Surface):
        screen.blit(self.surf, self.rect)

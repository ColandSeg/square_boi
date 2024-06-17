import pygame as pyg

class GameObject:
    def __init__(self, img_path: str, pos: tuple[int, int]):
        pass

    def draw(self, screen: pyg.Surface):
        screen.blit(self.surf, self.rect)

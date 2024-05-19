import pygame as pyg

class Player:
    def __init__(self):
        self.surfaces = {
            "front":    pyg.image.load("assets/player_front.png").convert(),
            "up":       pyg.image.load("assets/player_up.png").convert(),
            "left":     pyg.image.load("assets/player_left.png").convert(),
            "down":     pyg.image.load("assets/player_down.png").convert(),
            "right":    pyg.image.load("assets/player_right.png").convert()
        }
        self.surf = self.surfaces["front"]
        self.rect = self.surf.get_rect(center = (480, 240))

    def move(self):
        keys = pyg.key.get_pressed()
        if keys[pyg.K_w]:
            self.rect.y -= 8
        if keys[pyg.K_a]:
            self.rect.x -= 8
        if keys[pyg.K_s]:
            self.rect.y += 8
        if keys[pyg.K_d]:
            self.rect.x += 8
    
    def stay_on_screen(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= 480:
            self.rect.bottom = 480
        if self.rect.right >= 960:
            self.rect.right = 960
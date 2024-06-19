from pygame.math import Vector2
from objects.game_object import GameObject
from objects.wall import Wall
from utils import load_img, load_audio

class Saw(GameObject):
    def __init__(self, pos: tuple[int, int], movement_dir: str):
        super().__init__(load_img("obstacles/saw1.png", True), pos)
        self.speed = 2
        self.movement_dir = movement_dir
        self.direction = Vector2(0, 0)
        self.hit = load_audio("hit.wav")
        
    def move(self, walls: list[Wall]):
        self.direction *= 0

        if self.movement_dir == "h":
            self.direction.x += 1
        if self.movement_dir == "v":
            self.direction.y -= 1

        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)
        # turn around
        if any(self.rect.colliderect(wall.rect) for wall in walls):
            self.speed *= -1
            self.hit.play()
    
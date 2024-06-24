from objects.game_object import GameObject
from objects.wall import Wall
from utils import load_img, load_audio

SAW_SPEED = 2
FAST_SAW_SPEED = 4

class Saw(GameObject):
    def __init__(self, pos: tuple[int, int], facing: str):
        super().__init__(load_img("obstacles/saw1.png", True), pos, SAW_SPEED)

        self.facing = facing # N, S, E, W
        self.movement = ""   # h: horizontal; v: vertical

        if facing == "W" or facing == "E":
            self.movement = "h"
        elif facing == "N" or facing == "S":
            self.movement = "v"

        self.wall_hit = load_audio("hit.wav")
        
    def move(self, walls: list[Wall], width: int, height: int):
        self.direction *= 0

        if self.movement == "h":
            self.direction.x += 1 if self.facing == "E" else -1
        if self.movement == "v":
            self.direction.y += 1 if self.facing == "S" else -1

        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        # Turn around
        if any(self.rect.colliderect(wall.rect) for wall in walls) or (
        #     self.rect.x <= 0 or self.rect.x >= height - self.rect.width
        # ) or (
            self.rect.y <= 0 or self.rect.y >= height - self.rect.height
        ):
            self.speed *= -1
            self.wall_hit.play()
    
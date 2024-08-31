from pygame.sprite import Group, spritecollideany
from objects.game_object import GameObject
from utils import load_png

SAW_SPEED = 3

class Saw(GameObject):
    def __init__(self, pos: tuple[int, int], facing: str):
        super().__init__(load_png("obstacles/saw", True), pos, SAW_SPEED, facing)

    def update(self, width: int, height: int, solids: Group):
        self.direction *= 0 # Reset direction

        if self.facing == "N":
            self.direction.y -= 1
        elif self.facing == "S":
            self.direction.y += 1
        elif self.facing == "E":
            self.direction.x += 1
        elif self.facing == "W":
            self.direction.x -= 1

        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

        # Turn around
        if spritecollideany(self, solids) or (
            self.rect.x <= 0 or self.rect.x >= width - self.rect.width
        ) or (
            self.rect.y <= 0 or self.rect.y >= height - self.rect.height
        ):
            self.speed *= -1

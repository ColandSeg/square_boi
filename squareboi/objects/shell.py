from objects.game_object import GameObject
from objects.wall import Wall
from utils import load_img, load_audio

SHELL_SPEED = 3
FAST_SHELL_SPEED = 6

class Shell(GameObject):
    def __init__(self, pos: tuple[int, int], facing: str):
        super().__init__(load_img("obstacles/shell.png", True), pos, SHELL_SPEED)
        self.set_direction(facing)
        self.crash_wav = load_audio("crash.wav")

    
    def set_direction(self, facing: str):
        match facing:
            case "N":
                self.direction.y -= 1
            case "S":
                self.direction.y += 1
            case "E":
                self.direction.x += 1
            case "W":
                self.direction.x -= 1
    
    def move(self):
        self.rect.move_ip(self.direction.x * self.speed, self.direction.y * self.speed)

    def crash_with(self, walls: list[Wall], width: int, height: int):
        if self.rect.collidelist(walls) != -1 or (
            self.rect.x <= 0 or self.rect.x >= width - self.rect.width
        ) or (
            self.rect.y <= 0 or self.rect.y >= height - self.rect.height
        ):
            self.crash_wav.play()
            return True
        else:
            return False
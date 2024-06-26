import pygame as pyg
from objects.game_object import GameObject
from objects.shell import Shell
from utils import load_img, load_audio

class Cannon(GameObject):
    next_event_id = pyg.USEREVENT + 1

    def __init__(self, pos: tuple[int, int], facing: str):
        super().__init__(load_img("obstacles/cannon.png", True), pos)
        self.facing = facing # N, S, E, W

        match self.facing:
            case "N":
                self.surf = pyg.transform.rotate(self.surf, 0)
                self.shell_pos = (self.rect.x, self.rect.y - 48)
            case "S":
                self.surf = pyg.transform.rotate(self.surf, 180)
                self.shell_pos = (self.rect.x, self.rect.y + 48)
            case "E":
                self.surf = pyg.transform.rotate(self.surf, 270)
                self.shell_pos = (self.rect.x + 48, self.rect.y)
            case "W":
                self.surf = pyg.transform.rotate(self.surf, 90)
                self.shell_pos = (self.rect.x - 48, self.rect.y)
        
        self.event_type = Cannon.next_event_id
        Cannon.next_event_id += 1

        # Set a timer for this cannon to fire every 3 seconds (3000 milliseconds)
        pyg.time.set_timer(self.event_type, 2500)

        self.fire_wav = load_audio("fire.wav")

    def fire(self) -> Shell:
        shell = Shell(self.shell_pos, self.facing)
        self.fire_wav.play()

        return shell

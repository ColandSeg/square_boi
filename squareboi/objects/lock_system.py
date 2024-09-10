from objects.game_object import GameObject
from utils import load_png, load_sound

class LockSystem(GameObject):
    def __init__(self, pos: tuple[int, int], system_id: int, color: str, part: str):
        super().__init__(load_png(f"obstacles/{part}_{color}", True), pos)
        self.system_id = system_id

    def open_lock(self):
        open_lock_sound = load_sound("open_lock.wav")
        open_lock_sound.play()
        self.kill()

import pygame as pyg

def load_png(file_path: str, alpha=False) -> pyg.Surface:
    surface = pyg.image.load(f"assets/sprites/{file_path}.png")
    return surface.convert_alpha() if alpha else surface.convert()
    
def load_wav(file_name: str) -> pyg.mixer.Sound:
    return pyg.mixer.Sound(f"assets/audio/{file_name}.wav")

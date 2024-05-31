import pygame as pyg

def load_png(directory: str, file_name: str, alpha=False) -> pyg.Surface:
    surface = pyg.image.load(f"assets/sprites/{directory}/{file_name}.png")
    if alpha:
        return surface.convert_alpha()
    else:
        return surface.convert()
    
def load_wav(file_name: str) -> pyg.mixer.Sound:
    return pyg.mixer.Sound(f"assets/audio/{file_name}.wav")
